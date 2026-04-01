from __future__ import annotations

from pydantic import Field

from .base import ResponseModel
from .base import ModelBase


class MatchCalendarItem(ModelBase):
    """比赛日历项。"""

    date: str = Field(..., description="日期，格式为 YYYY-MM-DD。")
    match_count: str = Field(..., description="当日比赛数量。")
    win_num: str = Field(..., description="当日胜场数。")
    draw_num: str = Field(..., description="当日平局数。")


class MatchCalendarEnvelope(ModelBase):
    """比赛日历接口内部响应。"""

    code: int = Field(..., description="业务状态码。")
    msg: str = Field(..., description="业务状态说明。")
    data: list[MatchCalendarItem] = Field(..., description="按日期聚合的比赛统计列表。")


class GetUserMatchCalendarResponse(ResponseModel[MatchCalendarEnvelope]):
    """获取比赛日历响应。"""