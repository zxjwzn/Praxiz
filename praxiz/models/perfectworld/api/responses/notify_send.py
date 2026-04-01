from __future__ import annotations

from pydantic import Field

from .base import ResponseModel
from .base import ModelBase


class NotifySendResponseData(ModelBase):
    """主动下行通知响应数据。"""

    sent: bool = Field(..., description="是否发送成功。")
    channel: str = Field(..., description="目标通道名。")
    target_id: int = Field(..., alias="targetId", description="目标窗口或进程 编号。")
    bypass_interception: bool = Field(..., alias="bypassInterception", description="是否绕过拦截链路。")


class NotifySendResponse(ResponseModel[NotifySendResponseData]):
    """主动下行通知响应。"""