from __future__ import annotations

from pydantic import Field

from .base import RequestModel


class CreateLadderTeamRequest(RequestModel):
    """创建天梯房间请求。"""

    map_names: list[str] = Field(..., description="地图英文名列表。")
    zone_ids: list[int] = Field(..., description="匹配区域 ID 列表。")
    bp_modes: list[int] = Field(..., description="BP 模式列表，具体枚举含义待补充。")
    game_target: int = Field(..., description="目标游戏模式或目标类型，具体含义待补充。")
    specialities: list[str] = Field(..., description="特性或标签列表，具体内容待补充。")
    role_card_id: int = Field(..., description="角色卡 ID，0 可能表示不使用。")