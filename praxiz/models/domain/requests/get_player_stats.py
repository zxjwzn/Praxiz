from __future__ import annotations

from .base import DomainRequestBase
from pydantic import Field


class GetPlayerStatsRequest(DomainRequestBase):
    """获取玩家战绩统计的通用请求模型。"""

    uid: str = Field(..., description="玩家的唯一标识符")
    season: str = Field(..., description="赛季标识符，默认为当前赛季")
