from __future__ import annotations

from pydantic import Field

from .base import RequestModel


class AddFriendRequest(RequestModel):
    """添加好友请求。"""

    uid: str = Field(..., description="目标用户的 SteamID。")