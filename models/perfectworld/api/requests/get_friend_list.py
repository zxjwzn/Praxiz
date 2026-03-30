from __future__ import annotations

from pydantic import Field

from .base import RequestModel


class GetFriendListRequest(RequestModel):
    """获取好友列表请求。"""

    friendType: int = Field(..., description="好友列表类型代码，具体含义待补充。")