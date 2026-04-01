"""可复用的异步 JSON 网关基类。"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from typing import Mapping
from typing import Self
from typing import TypeVar

import httpx
from pydantic import BaseModel
from pydantic import ValidationError

ResponseModelT = TypeVar("ResponseModelT", bound=BaseModel)


class AsyncJsonGatewayBase(ABC):
    """封装 HTTP 客户端生命周期与 JSON 请求流程的通用网关。"""

    def __init__(
        self,
        *,
        base_url: str,
        timeout_seconds: float = 10.0,
        client: httpx.AsyncClient | None = None,
    ) -> None:
        self._base_url = base_url.rstrip("/")
        self._owns_client = client is None
        self._client = (
            client
            if client is not None
            else httpx.AsyncClient(timeout=timeout_seconds)
        )

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: object, exc: object, tb: object) -> None:
        await self.close()

    async def close(self) -> None:
        """关闭当前实例持有的 HTTP 客户端资源。"""

        if self._owns_client:
            await self._client.aclose()

    async def post_json(
        self,
        *,
        path: str,
        payload: BaseModel,
        response_model: type[ResponseModelT],
        headers: Mapping[str, str] | None = None,
    ) -> ResponseModelT:
        url = self._build_url(path)
        try:
            response = await self._client.post(
                url,
                json=payload.model_dump(by_alias=True),
                headers=self._build_json_headers(headers),
            )
            response.raise_for_status()
        except httpx.HTTPStatusError as exc:
            raise self._build_network_error(
                message=f"请求 {url} 失败，状态码为 {exc.response.status_code}"
            ) from exc
        except httpx.HTTPError as exc:
            raise self._build_network_error(message=f"请求 {url} 时发生网络错误") from exc

        try:
            raw_body = response.json()
        except ValueError as exc:
            raise self._build_validation_error(
                message=f"{url} 的响应体不是有效的 结构化文本"
            ) from exc

        try:
            parsed_response = response_model.model_validate(raw_body)
        except ValidationError as exc:
            raise self._build_validation_error(
                message=f"{url} 的响应结构校验失败"
            ) from exc

        self._raise_for_api_error(url=url, response=parsed_response)
        return parsed_response

    def _build_url(self, path: str) -> str:
        normalized_path = path if path.startswith("/") else f"/{path}"
        return f"{self._base_url}{normalized_path}"

    def _build_json_headers(self, headers: Mapping[str, str] | None) -> dict[str, str]:
        merged_headers = {"Content-Type": "application/json"}
        if headers is not None:
            merged_headers.update(headers)
        return merged_headers

    @abstractmethod
    def _build_network_error(self, *, message: str) -> Exception:
        """构造网络层失败异常。"""

    @abstractmethod
    def _build_validation_error(self, *, message: str) -> Exception:
        """构造响应校验失败异常。"""

    def _raise_for_api_error(self, *, url: str, response: BaseModel) -> None:
        """子类可覆盖该方法实现业务失败判定。"""
