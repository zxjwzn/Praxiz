from __future__ import annotations

from typing import Literal

from pydantic import Field

from .base import RequestModel


class LoginRequest(RequestModel):
    """伪触发登录/登出事件请求。"""

    type: Literal["logined", "logout"] = Field(
        ...,
        description="登录事件类型，支持 logined 或 logout。",
    )
    token: str = Field(..., description="登录令牌，登录态下由平台返回。")
    uid: str = Field(..., description="当前登录用户的 SteamID。")
    login_method: str = Field(
        ...,
        description="登录方式标识，示例值为 0，具体含义待补充。",
    )