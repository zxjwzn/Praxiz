from __future__ import annotations

from pydantic import Field

from .base import RequestModel


class SearchFriendRequest(RequestModel):
    """搜索好友请求。"""

    name: str = Field(..., description="要搜索的玩家昵称。")
    page: int = Field(default=1, description="分页页码，从 1 开始。")