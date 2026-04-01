from __future__ import annotations

from pydantic import Field

from .base import RequestModel


class GetUserMatchHistoryRequest(RequestModel):
    """获取比赛列表请求。"""

    uid: str = Field(..., description="目标用户的 平台编号。")
    page: str = Field(default="1", description="分页页码。接口文档示例为字符串。")
    page_size: str = Field(default="15", description="每页数量。接口文档示例为字符串。")
    game_types: str = Field(
        default="10,12,14,16,27,20,33,40,41,44,51",
        description="比赛类型列表，使用逗号分隔。",
    )
    start_time: str = Field(..., description="开始时间，格式待补充，可为空字符串。")
    end_time: str = Field(..., description="结束时间，格式待补充，可为空字符串。")
    season: str = Field(..., description="赛季标识，可为空字符串。")
    ticket_id: str = Field(default="", description="无意义")
