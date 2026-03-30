from __future__ import annotations

from typing import Any

from pydantic import Field

from .base import GenericApiResponse
from .base import ModelBase
from .common import RadarNew
from .common import SeasonStatsLadder
from .common import SeasonStatsMapItem
from .common import SeasonStatsWeaponItem


class SeasonStatsPayload(ModelBase):
    """赛季统计业务数据。"""

    ladder: SeasonStatsLadder = Field(..., description="赛季天梯总览。")
    first: dict[str, Any] = Field(..., description="首杀相关旧版数据，当前样本为空对象。")
    map: list[SeasonStatsMapItem] = Field(..., description="地图维度统计列表。")
    weapon: list[SeasonStatsWeaponItem] = Field(..., description="武器维度统计列表。")
    all_season_max_score: int | None = Field(..., description="历史赛季最高分。")
    all_season_max_star: int | None = Field(..., description="历史赛季最高星数。")
    all_season_max_score_season: str | None = Field(..., description="历史最高分所在赛季。")
    radar: list[Any] = Field(..., description="旧版雷达数据，当前样本为空列表。")
    radar_new: RadarNew = Field(..., description="新版雷达数据。")
    recent_score_list: list[Any] = Field(..., description="最近分数变化列表，当前样本为空列表。")
    prize_peak: dict[str, Any] | None = Field(..., description="奖励峰值数据，当前样本为 null。")
    individual_peak: dict[str, Any] | None = Field(..., description="个人峰值数据，当前样本为 null。")


class SeasonStatsEnvelope(ModelBase):
    """赛季统计接口内部响应。"""

    code: int = Field(..., description="业务状态码。")
    msg: str = Field(..., description="业务状态说明。")
    data: SeasonStatsPayload | None = Field(..., description="赛季统计业务载荷。")


class GetUserSeasonStatsResponse(GenericApiResponse[SeasonStatsEnvelope]):
    """获取赛季统计响应。"""