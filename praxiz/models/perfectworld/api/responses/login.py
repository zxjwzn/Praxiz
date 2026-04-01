from __future__ import annotations

from pydantic import Field

from .base import ResponseModel
from .base import ModelBase


class LoginResponseData(ModelBase):
    """登录接口响应数据。"""

    fired: bool = Field(..., description="是否成功触发登录/登出事件。")


class LoginResponse(ResponseModel[LoginResponseData]):
    """登录接口响应。"""