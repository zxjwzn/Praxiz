from __future__ import annotations

import builtins

from pydantic import Field

from .base import ResponseModel
from .base import ModelBase
from .common import SeasonStatsMapInfo


class MatchHistoryScore(ModelBase):
    """比赛历史中的天梯分变化。"""

    match: str = Field(..., description="比赛 编号。")
    steam_id: str = Field(..., description="平台编号。")
    user_id: str = Field(..., description="用户 编号。")
    season: str = Field(..., description="赛季标识。")
    score: str = Field(..., description="结算后分数。")
    score_change: str = Field(..., description="本场分数变化。")
    keep_score: str = Field(..., description="保分值。")
    team_id: str = Field(..., description="队伍 编号。")
    group_type: str = Field(..., description="组队类型代码。")
    performance_score: str = Field(..., description="表现分。")
    timestamp: str = Field(..., description="结算时间戳。")


class MatchHistoryMatchStart(ModelBase):
    """比赛开始信息。"""

    date: str = Field(..., description="开始时间。")
    match: str = Field(..., description="比赛 编号。")
    map: str = Field(..., description="地图英文名。")
    game_mode: str = Field(..., description="游戏模式代码。")
    game_type: str = Field(..., description="比赛类型代码。")
    ip: str = Field(..., description="服务器 地址 整数表示。")
    zone_id: str = Field(..., description="大区 编号。")
    ticket_id: str = Field(..., description="票据 编号。")


class MatchHistoryResult(ModelBase):
    """比赛结果摘要。"""

    date: str = Field(..., description="结束时间。")
    match: str = Field(..., description="比赛 编号。")
    map: str = Field(..., description="地图英文名。")
    win_camp: str = Field(..., description="获胜阵营。")
    t_win_times: str = Field(..., description="T 方胜利回合数。")
    ct_win_times: str = Field(..., description="CT 方胜利回合数。")
    win_team_id: str = Field(..., description="胜方队伍 编号。")
    lose_team_id: str = Field(..., description="负方队伍 编号。")
    zone_id: str = Field(..., description="大区 编号。")
    game_mode: str = Field(..., description="游戏模式代码。")
    game_type: str = Field(..., description="比赛类型代码。")
    is_green: str = Field(..., description="是否绿色对局。")
    match_start: MatchHistoryMatchStart = Field(..., description="比赛开始信息。")


class MatchHistoryItem(ModelBase):
    """单场比赛历史记录。"""

    match: str = Field(..., description="比赛 编号。")
    steam_id: str = Field(..., description="平台编号。")
    user_id: str = Field(..., description="用户 编号。")
    date: str = Field(..., description="展示用时间区间。")
    camp: str = Field(..., description="所在阵营。")
    team_id: str = Field(..., description="队伍 编号。")
    svr_id: str = Field(..., description="服务器 编号。")
    steam_nick: str = Field(..., description="平台昵称。")
    kill: str = Field(..., description="击杀数。")
    death: str = Field(..., description="死亡数。")
    assist: str = Field(..., description="助攻数。")
    score: MatchHistoryScore = Field(..., description="天梯分变化。")
    match_result: MatchHistoryResult = Field(..., description="比赛结果摘要。")
    map: SeasonStatsMapInfo = Field(..., description="地图静态信息。")
    match_name: str = Field(..., description="比赛名称。")
    replay_expired: bool = Field(..., description="回放 是否已过期。")
    replay_available: bool = Field(..., description="回放 是否可用。")
    replay_video_expired: bool = Field(..., description="录像视频是否已过期。")
    replay_video_available: bool = Field(..., description="录像视频是否可用。")


class MatchHistoryPayload(ModelBase):
    """比赛历史载荷。"""

    total: int = Field(..., description="总记录数。")
    total_page: int = Field(..., description="总页数。")
    list: builtins.list[MatchHistoryItem] = Field(..., description="比赛历史列表。")


class MatchHistoryEnvelope(ModelBase):
    """比赛历史接口内部响应。"""

    code: int = Field(..., description="业务状态码。")
    msg: str = Field(..., description="业务状态说明。")
    data: MatchHistoryPayload = Field(..., description="比赛历史载荷。")


class GetUserMatchHistoryResponse(ResponseModel[MatchHistoryEnvelope]):
    """获取比赛历史响应。"""