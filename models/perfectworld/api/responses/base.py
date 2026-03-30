from __future__ import annotations

from typing import Generic
from typing import TypeVar

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field

T = TypeVar("T")


class ModelBase(BaseModel):
    """响应模型基类。"""

    model_config = ConfigDict(populate_by_name=True, extra="allow")


class ApiError(ModelBase):
    """统一错误对象。"""

    code: str = Field(..., description="错误代码。")
    message: str = Field(..., description="错误说明。")


class GenericApiResponse(ModelBase, Generic[T]):
    """统一 HTTP 响应包装。"""

    ok: bool = Field(..., description="请求是否成功。")
    timestamp: str = Field(..., description="响应时间，ISO 8601 字符串。")
    data: T | None = Field(..., description="业务数据。")
    error: ApiError | None = Field(..., description="错误信息，成功时为 null。")