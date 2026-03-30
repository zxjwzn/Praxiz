from __future__ import annotations

from typing import Literal

from pydantic import Field

from .base import RequestModel


class InterceptRespondRequest(RequestModel):
    """响应拦截事件请求。"""

    eventId: str = Field(..., description="待处理拦截事件 ID。")
    action: Literal["allow", "block", "modify"] = Field(
        ...,
        description="拦截决策动作。",
    )
    payload: dict[str, object] | None = Field(
        default=None,
        description="当 action 为 modify 时用于替换原消息体的新载荷。",
    )
    reason: str | None = Field(default=None, description="决策原因说明。")