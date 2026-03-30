from __future__ import annotations

from pydantic import Field

from .base import RequestModel


class LeaveLadderTeamRequest(RequestModel):
    """离开天梯房间请求。"""

    leave_team_reason: int = Field(default=0, description="离队原因代码，具体枚举含义待补充。")