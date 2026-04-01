from __future__ import annotations

from .base import DomainRequestBase
from pydantic import Field


class GetMatchHistoryRequest(DomainRequestBase):
    """获取玩家历史比赛列表的通用请求模型。"""

    uid: str = Field(..., description="玩家的唯一标识符")
    season: str = Field(..., description="赛季标识符，默认为当前赛季")
    start_time: int = Field(..., description="查询的起始时间戳")
    end_time: int = Field(..., description="查询的结束时间戳")
