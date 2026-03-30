from __future__ import annotations

from pydantic import Field

from .base import RequestModel


class GetUserMatchHistoryRequest(RequestModel):
    """获取比赛列表请求。"""

    uid: str = Field(..., description="目标用户的 SteamID。")
    page: str = Field(..., description="分页页码。接口文档示例为字符串。")
    page_size: str = Field(..., description="每页数量。接口文档示例为字符串。")
    game_types: str = Field(..., description="比赛类型列表，使用逗号分隔。")
    start_time: str = Field(..., description="开始时间，格式待补充，可为空字符串。")
    end_time: str = Field(..., description="结束时间，格式待补充，可为空字符串。")
    season: str = Field(..., description="赛季标识，可为空字符串。")
    ticket_id: str = Field(..., description="票据或筛选标识，可为空字符串。")