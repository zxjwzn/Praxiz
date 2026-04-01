"""Perfectworld 数据源相关异常定义。"""

from __future__ import annotations

from praxiz.models.domain.errors import PraxizError


class PerfectWorldGatewayError(PraxizError):
    """Perfectworld 网关操作的基异常。"""


class PerfectworldNetworkError(PerfectWorldGatewayError):
    """与 Perfectworld 的 HTTP 传输失败时抛出。"""


class PerfectworldValidationError(PerfectWorldGatewayError):
    """响应解码或结构校验失败时抛出。"""


class PerfectworldApiError(PerfectWorldGatewayError):
    """Perfectworld 返回业务级失败时抛出。"""

    def __init__(self, code: str, message: str) -> None:
        self.code = code
        self.message = message
        super().__init__(f"{code}: {message}")
