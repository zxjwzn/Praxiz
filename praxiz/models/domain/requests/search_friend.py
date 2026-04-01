from __future__ import annotations

from .base import DomainRequestBase
from pydantic import Field


class SearchFriendRequest(DomainRequestBase):
    """搜索好友的通用请求模型。"""

    name: str = Field(..., description="要搜索的好友名称")
