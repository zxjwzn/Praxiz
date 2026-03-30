from __future__ import annotations

from pydantic import Field

from .base import RequestModel


class GetUserSeasonStatsRequest(RequestModel):
    """获取赛季统计数据请求。"""

    uid: str = Field(..., description="目标用户的 SteamID。")
    season: str = Field(..., description="查询的赛季标识，例如 S23。")
    current_season: str = Field(..., description="当前赛季标识，例如 S23。")