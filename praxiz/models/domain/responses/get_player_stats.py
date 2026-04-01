from __future__ import annotations

from pydantic import Field

from .base import DomainResponseBase


class PlayerStatsResponse(DomainResponseBase):
    """玩家整体战绩统计。"""

    uid: str = Field(..., description="玩家的平台唯一标识符。")
    player_name: str = Field(..., description="玩家外显昵称。")
    avatar_url: str = Field(
        default="", description="头像图的绝对网络链接，如果不存在则为空字符串。"
    )

    # 核心战绩数据
    rating: float = Field(
        default=0.0,
        description="整体或赛季综合评分（如 PerfectWorld Rating 或 FaceIt ELO）。",
    )
    kd_ratio: float = Field(default=0.0, description="击杀与死亡的比值 (K/D)。")
    win_rate: float = Field(default=0.0, description="胜率（如 0.55 表示 55%）。")
    matches_played: int = Field(default=0, description="完成的有效比赛场次。")
    headshot_rate: float = Field(
        default=0.0, description="爆头击杀占总击杀的比例（如 0.45 表示 45%）。"
    )
    average_damage: float = Field(default=0.0, description="场均伤害参数 (ADR)。")
    average_rws: float = Field(default=0.0, description="场均回合参与贡献值 (RWS)。")
