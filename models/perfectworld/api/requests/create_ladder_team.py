from __future__ import annotations

from pydantic import Field

from .base import RequestModel


class CreateLadderTeamRequest(RequestModel):
    """创建天梯房间请求。"""

    map_names: list[str] = Field(
        default=[
            "de_dust2",
            "de_inferno",
            "de_mirage",
            "de_nuke",
            "de_overpass",
            "de_train",
            "de_vertigo",
            "de_ancient",
            "de_anubis",
        ],
        description="地图英文名列表。",
    )
    zone_ids: list[int] = Field(
        default=[612, 604, 605, 603, 609, 601, 611], description="匹配区域 ID 列表。"
    )
    bp_modes: list[int] = Field(
        default=[0], description="BP 模式列表，具体枚举含义待补充。"
    )
    game_target: int = Field(
        default=0, description="目标游戏模式或目标类型，具体含义待补充。"
    )
    specialities: list[str] = Field(
        default=[], description="特性或标签列表，具体内容待补充。"
    )
    role_card_id: int = Field(default=0, description="无意义")
