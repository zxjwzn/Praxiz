from __future__ import annotations

from typing import Literal

from pydantic import Field

from .base import EmptyRequest
from .base import RequestModel


class SubscriptionChannelGroup(RequestModel):
    """订阅通道分组。"""

    forwardChannels: list[str] = Field(..., description="仅转发的通道列表。")
    interceptChannels: list[str] = Field(..., description="需要拦截决策的通道列表。")


class SubscriptionConfigRequest(RequestModel):
    """设置订阅配置请求。"""

    mode: Literal["set", "patch"] = Field(..., description="配置模式，支持 set 或 patch。")
    upstream: SubscriptionChannelGroup = Field(..., description="上行消息订阅配置。")
    downstream: SubscriptionChannelGroup = Field(..., description="下行消息订阅配置。")
    timeoutMs: int = Field(
        ...,
        ge=100,
        le=10000,
        description="拦截超时时间，单位毫秒，范围 100 到 10000。",
    )
    onTimeout: Literal["allow", "block", "modify"] = Field(
        ...,
        description="超时后的处理动作，支持 allow、block、modify。",
    )


class ClearSubscriptionsRequest(EmptyRequest):
    """清空订阅配置请求。"""