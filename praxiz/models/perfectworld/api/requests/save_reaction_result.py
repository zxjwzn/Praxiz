from __future__ import annotations

from pydantic import Field

from .base import RequestModel


class SaveReactionResultRequest(RequestModel):
    """保存反应测试结果请求。"""

    avgReactMs: int = Field(..., description="平均反应时间，单位毫秒。")
    bstReactMs: int = Field(..., description="最佳反应时间，单位毫秒。")
    hitCnt: int = Field(..., description="命中次数。")
    lv: int = Field(..., description="结果等级。")