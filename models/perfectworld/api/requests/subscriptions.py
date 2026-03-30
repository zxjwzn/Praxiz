from __future__ import annotations

from pydantic import Field

from .base import EmptyRequest
from .base import RequestModel


class SubscriptionChannelGroup(RequestModel):
    """订阅通道分组。"""

    forwardChannels: list[str] = Field(..., description="仅转发的通道列表。")
    interceptChannels: list[str] = Field(..., description="需要拦截决策的通道列表。")


class SubscriptionConfigRequest(RequestModel):
    """设置订阅配置请求。"""

    upstream: SubscriptionChannelGroup = Field(..., description="上行消息订阅配置。")
    downstream: SubscriptionChannelGroup = Field(..., description="下行消息订阅配置。")
    timeoutMs: int = Field(..., description="拦截超时时间，单位毫秒。")
    onTimeout: str = Field(..., description="超时后的处理动作，例如 allow。")


class ClearSubscriptionsRequest(EmptyRequest):
    """清空订阅配置请求。"""