from __future__ import annotations

from pydantic import Field

from .base import RequestModel


class GetUserCommentListRequest(RequestModel):
    """获取评论列表请求。"""

    uid: str = Field(..., description="目标用户的 SteamID。")