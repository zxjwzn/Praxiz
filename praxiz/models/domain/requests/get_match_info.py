from __future__ import annotations

from .base import DomainRequestBase
from pydantic import Field


class GetMatchInfoRequest(DomainRequestBase):
    """获取比赛详情的通用请求模型。"""

    match_id: str = Field(..., description="比赛的唯一标识符")
