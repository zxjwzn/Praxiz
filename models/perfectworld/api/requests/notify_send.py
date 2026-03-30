from __future__ import annotations

from pydantic import Field

from .base import RequestModel


class NotifySendRequest(RequestModel):
    """主动发送下行通知请求。"""

    channel: str = Field(..., description="下行通知通道名。")
    payload: dict[str, object] = Field(
        ...,
        description="通知载荷，具体结构依赖目标通道。",
    )