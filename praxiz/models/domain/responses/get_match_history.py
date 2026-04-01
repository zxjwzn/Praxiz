from __future__ import annotations

import builtins
from pydantic import BaseModel
from pydantic import Field

from .base import DomainResponseBase


class MatchHistoryItem(BaseModel):
    """单条历史比赛梗概。"""

    match_id: str = Field(..., description="源数据平台该局比赛的全局唯一编号。")
    map_name: str = Field(..., description="对战地图英文标识或中文名称。")
    start_time: str = Field(
        ..., description="对战开始时间的标准字符串（如 ISO 8601 或格式化文本）。"
    )
    kills: int = Field(default=0, description="本场该玩家总击杀值。")
    deaths: int = Field(default=0, description="本场该玩家总死亡值。")
    assists: int = Field(default=0, description="本场该玩家总助攻值。")
    is_win: bool = Field(
        default=False, description="本场该玩家所在阵营最终是否判定为胜利。"
    )
    rating: float = Field(default=0.0, description="本场比赛平台赋予该玩家的表现评分。")


class PlayerMatchHistoryResponse(DomainResponseBase):
    """玩家历史比赛列表响应。"""

    uid: str = Field(..., description="玩家的平台唯一标识符。")
    matches: builtins.list[MatchHistoryItem] = Field(
        default_factory=list, description="比赛明细列表，以时间降序下发"
    )
    total_results: int = Field(
        default=0, description="平台总计存储该玩家的历史场次数。"
    )
