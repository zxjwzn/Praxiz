from __future__ import annotations

from pydantic import Field

from .base import RequestModel


class GetUserMatchCalendarRequest(RequestModel):
    """获取比赛日历请求。"""

    uid: str = Field(..., description="目标用户的 平台编号。")
    start_time: str = Field(..., description="开始日期，示例格式为 YYYY-MM-DD。")
    end_time: str = Field(..., description="结束日期，示例格式为 YYYY-MM-DD。")