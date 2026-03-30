from __future__ import annotations

from typing import Any

from pydantic import AliasChoices
from pydantic import ConfigDict
from pydantic import Field

from .base import ModelBase


class SeasonStatsMapInfo(ModelBase):
    """地图静态信息。"""

    id: str = Field(..., description="地图 ID。")
    name_en: str = Field(..., description="地图英文名。")
    name_cn: str = Field(..., description="地图中文名。")
    logo: str = Field(..., description="地图 Logo URL。")
    image: str = Field(..., description="地图图片 URL。")
    bp_color: str = Field(..., description="BP 彩色图 URL。")
    bp_gray: str = Field(..., description="BP 灰色图 URL。")
    bp_ladder: str = Field(..., description="天梯图标 URL。")
    bp_ladder_ban: str = Field(..., description="天梯禁用图标 URL。")
    bp_camp: str = Field(..., description="阵营图标 URL。")
    background: str = Field(..., description="背景图 URL。")
    download_type: str = Field(..., description="下载类型代码。")
    workshop_id: str = Field(..., description="创意工坊 ID。")
    url: str = Field(..., description="附加 URL，当前样本为空。")
    md5: str = Field(..., description="资源 MD5，当前样本为空。")
    practice_type: str = Field(..., description="练习类型代码。")
    tips: str = Field(..., description="提示信息，当前样本为空。")


class LadderTeamPlayer(ModelBase):
    """天梯房间玩家信息。"""

    player_id: str = Field(..., description="玩家 ID。")
    is_lord: bool = Field(..., description="是否为房主。")
    slot_id: int = Field(..., description="槽位 ID。")
    nick_name: str = Field(..., description="玩家昵称。")
    player_type: int = Field(..., description="玩家类型代码。")
    ready_flag: bool = Field(..., description="是否已准备。")
    in_anchor_whitelist: bool = Field(..., description="是否在主播白名单中。")
    game_version: int = Field(..., description="游戏版本代码。")
    speciality: int = Field(..., description="特长代码。")
    game_target: int = Field(..., description="目标模式代码。")
    role_card_id: int = Field(..., description="角色卡 ID。")
    specialities: list[Any] = Field(..., description="特长列表。")


class TeamSlotInfo(ModelBase):
    """队伍槽位信息。"""

    slot_id: int = Field(..., description="槽位 ID。")
    anchor_ticket_count: int = Field(..., description="主播票数量。")
    player_id: str = Field(..., description="槽位占用玩家 ID。")


class TeamAdvancedSetup(ModelBase):
    """自定义高级设置。"""

    team_a_count: int = Field(..., description="A 队人数上限。")
    team_b_count: int = Field(..., description="B 队人数上限。")
    need_demo: bool = Field(..., description="是否需要 Demo。")
    need_friendly_fire_vote: bool = Field(..., description="是否需要友伤投票。")
    need_knife_round_vote: bool = Field(..., description="是否需要刀局投票。")


class CustomTeamSetting(ModelBase):
    """自定义房间设置。"""

    team_mode: int = Field(..., description="队伍模式代码。")
    ob_max_limits: int = Field(..., description="观战人数上限。")
    custom_advanced_setup: TeamAdvancedSetup = Field(..., alias="custom_advanced_setup", description="高级设置。")


class LadderTeamInfo(ModelBase):
    """天梯房间信息。"""

    team_id: int = Field(..., description="队伍 ID。")
    map_names: list[str] = Field(..., description="地图列表。")
    players: list[LadderTeamPlayer] = Field(..., description="玩家列表。")
    zone_ids: list[int] = Field(..., description="大区 ID 列表。")
    match_mode: int = Field(..., description="匹配模式代码。")
    is_single: bool = Field(..., description="是否单排。")
    custom_team_setting: CustomTeamSetting = Field(..., description="自定义房间设置。")
    is_abs_green: bool = Field(..., description="是否绝对绿色。")
    play_type: int = Field(..., description="玩法类型代码。")
    rounds_number: int = Field(..., description="总回合数配置。")
    is_abs_balance: bool = Field(..., description="是否绝对平衡。")
    room_setting: str = Field(..., description="房间设置字符串。")
    red_packets_type: int = Field(..., description="红包类型。")
    red_packets_data: list[Any] = Field(..., description="红包数据。")
    anchor_ticket_count: int = Field(..., description="主播票数量。")
    slot_infos: list[TeamSlotInfo] = Field(..., description="槽位信息列表。")
    cur_anchor_recruit_count: int = Field(..., description="当前主播招募数量。")
    recruit_room_type: int = Field(..., description="招募房类型。")
    no_demo: bool = Field(..., description="是否不保存 Demo。")
    bp_modes: list[int] = Field(..., description="BP 模式列表。")
    me_match_mode: int = Field(..., description="ME 匹配模式。")
    me_begin_time: int = Field(..., description="ME 开始时间。")
    me_end_time: int = Field(..., description="ME 结束时间。")


class WeaponInfo(ModelBase):
    """武器静态信息。"""

    name_en: str = Field(..., description="武器英文名。")
    name_cn: str = Field(..., description="武器中文名。")
    image: str = Field(..., description="武器图片 URL。")
    user_page_image: str = Field(..., description="用户页展示图 URL。")


class RadarSection(ModelBase):
    """雷达评分分区。"""

    score: str | None = Field(..., description="当前分区得分，可能为空。")
    score_base: str | None = Field(..., description="基准分，可能为空。")
    level: str | None = Field(..., description="评级，可能为空。")
    detail: dict[str, str] = Field(..., description="分区明细键值对。")


class RadarNew(ModelBase):
    """新版雷达数据。"""

    fire_power: RadarSection = Field(..., description="火力维度评分。")
    marksmanship: RadarSection = Field(..., description="枪法维度评分。")
    follow_up_shot: RadarSection = Field(..., description="补枪维度评分。")
    first: RadarSection = Field(..., description="首杀维度评分。")
    item: RadarSection = Field(..., description="道具维度评分。")
    one_v_n: RadarSection = Field(..., validation_alias=AliasChoices("1vn"), serialization_alias="1vn", description="残局维度评分。")
    sniper: RadarSection = Field(..., description="狙击维度评分。")
    description: str = Field(..., description="综合评价描述。")
    app: RadarSection = Field(..., description="附加评分维度。")


class SeasonStatsMapItem(ModelBase):
    """单张地图赛季统计。"""

    user_id: str = Field(..., description="用户 SteamID。")
    map: str = Field(..., description="地图英文标识。")
    season: str = Field(..., description="赛季标识。")
    season_show_name: str = Field(..., description="赛季展示名称。")
    win_num: str = Field(..., description="胜场数。")
    total_num: str = Field(..., description="总场次。")
    t_win_rounds: str = Field(..., description="T 方胜利回合数。")
    t_rounds_num: str = Field(..., description="T 方总回合数。")
    ct_win_rounds: str = Field(..., description="CT 方胜利回合数。")
    ct_rounds_num: str = Field(..., description="CT 方总回合数。")
    pw_rating_avg: str = Field(..., description="完美评级平均值。")
    rws_avg: str = Field(..., description="RWS 平均值。")
    adpr: str = Field(..., description="场均伤害 ADPR。")
    kill_num: str = Field(..., description="击杀数。")
    sniper_kill_num: str = Field(..., description="狙击枪击杀数。")
    team_kill_num: str = Field(..., description="队友击杀数。")
    death_num: str = Field(..., description="死亡数。")
    first_kill_num: str = Field(..., description="首杀次数。")
    first_death_num: str = Field(..., description="首死次数。")
    headshot_kill_num: str = Field(..., description="爆头击杀数。")
    sniper_headshot_kill_num: str = Field(..., description="狙击爆头击杀数。")
    match_mvp_num: str = Field(..., description="比赛 MVP 次数。")
    two_kill_num: str = Field(..., description="双杀次数。")
    three_kill_num: str = Field(..., description="三杀次数。")
    four_kill_num: str = Field(..., description="四杀次数。")
    five_kill_num: str = Field(..., description="五杀次数。")
    one_v_one_num: str = Field(..., validation_alias=AliasChoices("1v1_num"), serialization_alias="1v1_num", description="1v1 残局获胜次数。")
    one_v_two_num: str = Field(..., validation_alias=AliasChoices("1v2_num"), serialization_alias="1v2_num", description="1v2 残局获胜次数。")
    one_v_three_num: str = Field(..., validation_alias=AliasChoices("1v3_num"), serialization_alias="1v3_num", description="1v3 残局获胜次数。")
    one_v_four_num: str = Field(..., validation_alias=AliasChoices("1v4_num"), serialization_alias="1v4_num", description="1v4 残局获胜次数。")
    one_v_five_num: str = Field(..., validation_alias=AliasChoices("1v5_num"), serialization_alias="1v5_num", description="1v5 残局获胜次数。")
    round_count: str = Field(..., description="总回合数。")
    dmg_health_total: str = Field(..., description="总生命伤害。")
    kill_round: str = Field(..., description="有击杀的回合数。")
    win_round_kill: str = Field(..., description="获胜回合击杀数。")
    win_round_count: str = Field(..., description="获胜回合数。")
    win_dmg_health: str = Field(..., description="获胜回合造成的生命伤害。")
    pistol_we_sum: str = Field(..., description="手枪局 WE 累积值。")
    pri_avg: str = Field(..., description="PRI 平均值。")
    update_time: str = Field(..., description="更新时间戳。")
    hs_kill_rate: str = Field(..., description="爆头击杀率。")
    fire_power: str = Field(..., description="火力值。")
    map_info: SeasonStatsMapInfo = Field(..., description="地图静态信息。")


class SeasonStatsWeaponItem(ModelBase):
    """单武器赛季统计。"""

    damage_sum: int = Field(..., description="总伤害。")
    weapon_rapid_stop_shot_count: int = Field(..., description="急停射击总次数。")
    rapid_stop_success_rate: float = Field(..., description="急停成功率。")
    first_shot_accuracy: float = Field(..., description="首发命中率。")
    first_shot_hit_count: int = Field(..., description="首发命中次数。")
    avg_damage: int = Field(..., description="平均伤害。")
    spray_hit_count: int = Field(..., description="扫射命中次数。")
    time_to_kill_count: int = Field(..., description="计入击杀耗时的样本次数。")
    time_to_kill_total: int = Field(..., description="击杀耗时总和。")
    spray_accuracy: float | None = Field(None, description="扫射命中率，部分武器可能缺失。")
    first_shot_shot_count: int = Field(..., description="首发射击次数。")
    match_num: int = Field(..., description="使用该武器的比赛数。")
    weapon_rapid_stop_hit_count: int = Field(..., description="急停命中次数。")
    kill_num: int = Field(..., description="击杀数。")
    avg_time_to_kill: int = Field(..., description="平均击杀耗时。")
    headshot_rate: float = Field(..., description="爆头率。")
    avg_kill_num: float = Field(..., description="平均击杀数。")
    name: str = Field(..., description="武器内部名称。")
    spray_shot_count: int = Field(..., description="扫射射击次数。")
    headshot_sum: int = Field(..., description="爆头数。")
    level_avg_time_to_kill: str = Field(..., description="平均击杀耗时评级。")
    level_accuracy: str = Field(..., description="命中评级。")
    level_avg_damage: str = Field(..., description="平均伤害评级。")
    level_headshot_rate: str = Field(..., description="爆头率评级。")
    level_avg_kill_num: str = Field(..., description="平均击杀评级。")
    level_avg_kills_per_round: str = Field(..., description="每回合平均击杀评级，可能为空。")
    level_rapid_stop_success_rate: str = Field(..., description="急停成功率评级。")
    accuracy_type: int = Field(..., description="精度类型代码，具体含义待补充。")
    total_rounds_kpr: int | None = Field(None, description="KPR 总回合数样本，部分武器存在。")
    total_rounds: int | None = Field(None, description="总回合数，部分武器存在。")
    total_kills_kpr: int | None = Field(None, description="KPR 统计击杀数，部分武器存在。")
    avg_kills_per_round: float | None = Field(None, description="每回合平均击杀数，部分武器存在。")
    weapon_info: WeaponInfo = Field(..., description="武器静态信息。")


class SeasonStatsLadder(ModelBase):
    """赛季天梯总览。"""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id: str = Field(..., description="赛季统计记录 ID。")
    steam_id: str = Field(..., description="SteamID。")
    user_id: str = Field(..., description="用户 ID。")
    season: str = Field(..., description="赛季标识。")
    season_show_name: str = Field(..., description="赛季展示名称。")
    score: int = Field(..., description="当前分数。")
    score_change: int = Field(..., description="分数变化。")
    max_score: int = Field(..., description="赛季最高分。")
    max_star: int | None = Field(..., description="赛季最高星数，样本中为 null。")
    all_season_max_score: int | None = Field(..., description="历史赛季最高分，样本中为 null。")
    all_season_max_star: int | None = Field(..., description="历史赛季最高星数，样本中为 null。")
    rank: int = Field(..., description="排名。")
    match_count: int = Field(..., description="比赛场次。")
    win_num: int = Field(..., description="胜场数。")
    win_rate: float = Field(..., description="胜率。")
    pw_rating_avg: float = Field(..., description="完美评级平均值。")
    rws_avg: float = Field(..., description="RWS 平均值。")
    adpr: float = Field(..., description="场均伤害 ADPR。")
    pri_avg: float = Field(..., description="PRI 平均值。")
    hs_kill_rate: float = Field(..., description="爆头击杀率。")
    kill_num: int = Field(..., description="击杀数。")
    death_num: int = Field(..., description="死亡数。")
    assist_num: int = Field(..., description="助攻数。")
    round_count: int = Field(..., description="总回合数。")
    win_round_count: int = Field(..., description="获胜回合数。")
    kill_round: int = Field(..., description="有击杀回合数。")
    win_round_kill: int = Field(..., description="获胜回合击杀数。")
    dmg_health_total: int = Field(..., description="总生命伤害。")
    win_dmg_health: int = Field(..., description="获胜回合生命伤害。")
    first_kill_num: int = Field(..., description="首杀次数。")
    first_death_num: int = Field(..., description="首死次数。")
    headshot_kill_num: int = Field(..., description="爆头击杀数。")
    sniper_kill_num: int = Field(..., description="狙击击杀数。")
    sniper_headshot_kill_num: int = Field(..., description="狙击爆头击杀数。")
    match_mvp_num: int = Field(..., description="比赛 MVP 次数。")
    mvp_num: int = Field(..., description="MVP 次数。")
    team_kill_num: int = Field(..., description="队友击杀数。")
    fire_count_total: int = Field(..., description="开火总次数。")
    hit_count_total: int = Field(..., description="命中总次数。")
    one_v_one_num: int = Field(..., validation_alias=AliasChoices("1v1_num"), serialization_alias="1v1_num", description="1v1 残局获胜次数。")
    one_v_one_total: int = Field(..., validation_alias=AliasChoices("1v1_total"), serialization_alias="1v1_total", description="1v1 残局总次数。")
    one_v_two_num: int = Field(..., validation_alias=AliasChoices("1v2_num"), serialization_alias="1v2_num", description="1v2 残局获胜次数。")
    one_v_two_total: int = Field(..., validation_alias=AliasChoices("1v2_total"), serialization_alias="1v2_total", description="1v2 残局总次数。")
    one_v_three_num: int = Field(..., validation_alias=AliasChoices("1v3_num"), serialization_alias="1v3_num", description="1v3 残局获胜次数。")
    one_v_three_total: int = Field(..., validation_alias=AliasChoices("1v3_total"), serialization_alias="1v3_total", description="1v3 残局总次数。")
    one_v_four_num: int = Field(..., validation_alias=AliasChoices("1v4_num"), serialization_alias="1v4_num", description="1v4 残局获胜次数。")
    one_v_four_total: int = Field(..., validation_alias=AliasChoices("1v4_total"), serialization_alias="1v4_total", description="1v4 残局总次数。")
    one_v_five_num: int = Field(..., validation_alias=AliasChoices("1v5_num"), serialization_alias="1v5_num", description="1v5 残局获胜次数。")
    one_v_five_total: int = Field(..., validation_alias=AliasChoices("1v5_total"), serialization_alias="1v5_total", description="1v5 残局总次数。")