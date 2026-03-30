from __future__ import annotations

from typing import Any

from pydantic import ConfigDict
from pydantic import Field

from .base import GenericApiResponse
from .base import ModelBase


class MatchDetailPlayer(ModelBase):
    """比赛详情中的玩家统计。"""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    match: str = Field(..., description="比赛 ID。")
    steam_id: str = Field(..., description="玩家 Steam 数值 ID。")
    user_id: str = Field(..., description="玩家 SteamID。")
    steam_nick: str = Field(..., description="Steam 昵称。")
    kill: str = Field(..., description="击杀数。")
    death: str = Field(..., description="死亡数。")
    assist: str = Field(..., description="助攻数。")
    rating: str = Field(..., description="Rating。")
    pw_rating: str = Field(..., description="完美评级。")
    mm_score: str = Field(..., description="结算分数。")
    mm_change_score: str = Field(..., description="分数变化。")
    perfect_power: int = Field(..., alias="perfectPower", description="完美战力。")
    perfect_power_increment: int = Field(..., alias="perfectPowerIncrement", description="完美战力变化值。")


class MatchDetailRoundResult(ModelBase):
    """单回合结果。"""

    round: str = Field(..., description="回合序号。")
    win_camp: str = Field(..., description="获胜阵营。")
    win_type: str = Field(..., description="胜利类型代码。")
    bomb_planter: str | None = Field(..., description="下包玩家 ID。")
    bomb_defuser: str | None = Field(..., description="拆包玩家 ID。")
    win_team_id: str = Field(..., description="胜方队伍 ID。")
    lose_team_id: str = Field(..., description="负方队伍 ID。")
    half_match_type: str | None = Field(..., description="半场类型标识。")


class MatchDetailReport(ModelBase):
    """比赛详情报告。"""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ticket_id: str = Field(..., description="票据 ID。")
    no_demo: str = Field(..., description="是否无 Demo 标识。")
    win_camp: str = Field(..., description="获胜阵营。")
    t_win_times: str = Field(..., description="T 方胜利回合数。")
    ct_win_times: str = Field(..., description="CT 方胜利回合数。")
    map: str = Field(..., description="地图英文名。")
    match_id: str = Field(..., description="比赛 ID。")
    zone_id: str = Field(..., description="大区 ID。")
    match_type: str = Field(..., description="比赛类型代码。")
    game_mode: str = Field(..., description="游戏模式代码。")
    players: list[MatchDetailPlayer] = Field(..., description="玩家统计列表。")
    results: list[MatchDetailRoundResult] = Field(..., description="逐回合结果列表。")
    team_data: list[Any] = Field(..., alias="teamData", description="队伍统计列表，样本为空。")
    avg_data: list[Any] = Field(..., alias="avgData", description="平均统计列表，样本为空。")


class DemoInfo(ModelBase):
    """比赛 Demo 信息。"""

    demo_is_available: bool = Field(..., description="Demo 是否可下载。")
    demo_id: int = Field(..., description="Demo ID。")
    demo_url: str = Field(..., description="Demo 下载地址。")
    expire_soon: int = Field(..., description="是否即将过期。")
    expired: bool = Field(..., description="是否已过期。")
    is_disabled: bool = Field(..., description="是否被禁用。")
    has_demo: bool | None = Field(..., description="是否存在 Demo，样本中为 null。")


class MatchDetailPayload(ModelBase):
    """比赛详情主载荷。"""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    game_abbr: str = Field(..., description="游戏简称。")
    match_id: str = Field(..., description="比赛 ID。")
    match_winner_id: str = Field(..., description="获胜队伍 ID。")
    report: MatchDetailReport = Field(..., description="比赛报告。")
    cup: list[Any] = Field(..., description="杯赛信息列表，样本为空。")
    teams: list[Any] = Field(..., description="队伍信息列表，样本为空。")
    match_prize: list[Any] = Field(..., description="奖励信息列表，样本为空。")
    match: list[Any] = Field(..., description="附加比赛信息，样本为空。")
    pre_rank_data: list[Any] = Field(..., description="赛前排行数据，样本为空。")
    trump_plan_data: list[Any] = Field(..., description="王牌计划数据，样本为空。")
    recommend_teams: list[Any] = Field(..., description="推荐队伍数据，样本为空。")
    demo_info: DemoInfo = Field(..., description="Demo 信息。")


class MatchDetailEnvelope(ModelBase):
    """比赛详情接口内部响应。"""

    code: int = Field(..., description="业务状态码。")
    msg: str = Field(..., description="业务状态说明。")
    data: MatchDetailPayload = Field(..., description="比赛详情载荷。")


class GetMatchDetailResponse(GenericApiResponse[MatchDetailEnvelope]):
    """获取比赛详情响应。"""