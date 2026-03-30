from __future__ import annotations

from pydantic import Field

from .base import GenericApiResponse
from .base import ModelBase


class SubscriptionChannelGroup(ModelBase):
    """订阅通道分组。"""

    forward_channels: list[str] = Field(..., alias="forwardChannels", description="仅转发的通道列表。")
    intercept_channels: list[str] = Field(..., alias="interceptChannels", description="需要拦截的通道列表。")


class SubscriptionConfigData(ModelBase):
    """订阅配置数据。"""

    upstream: SubscriptionChannelGroup = Field(..., description="上行订阅配置。")
    downstream: SubscriptionChannelGroup = Field(..., description="下行订阅配置。")
    timeout_ms: int = Field(..., alias="timeoutMs", description="拦截超时时间，单位毫秒。")
    on_timeout: str = Field(..., alias="onTimeout", description="超时处理动作。")


class SubscriptionConfigResponse(GenericApiResponse[SubscriptionConfigData]):
    """获取或设置订阅配置响应。"""


class ClearSubscriptionsResponse(GenericApiResponse[SubscriptionConfigData]):
    """清空订阅配置响应。"""