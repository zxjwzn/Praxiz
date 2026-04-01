from __future__ import annotations

import builtins
from pydantic import BaseModel
from pydantic import Field

from .base import DomainResponseBase


class FriendInfoItem(BaseModel):
    """搜索好友的响应模型。"""

    uid: str = Field(..., description="玩家的平台唯一标识符。")
    nickname: str = Field(..., description="玩家外显昵称。")
    avatar_url: str = Field(
        default="", description="头像图的绝对网络链接，如果不存在则为空字符串。"
    )


class SearchFriendResponse(DomainResponseBase):
    """搜索好友响应模型。"""

    friends: builtins.list[FriendInfoItem] = Field(
        default_factory=list, description="搜索获取到的好友匹配列表。"
    )
    total_results: int = Field(default=0, description="命中该搜索条件的好友总量。")
