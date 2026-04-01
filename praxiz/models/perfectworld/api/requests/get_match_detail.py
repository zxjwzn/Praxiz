from __future__ import annotations

from pydantic import Field

from .base import RequestModel


class GetMatchDetailRequest(RequestModel):
    """获取赛后战绩详情请求。"""

    match_id: str = Field(..., description="比赛 编号。")