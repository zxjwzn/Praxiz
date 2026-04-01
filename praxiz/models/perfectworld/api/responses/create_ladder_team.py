from __future__ import annotations

from pydantic import Field

from .base import ResponseModel
from .base import ModelBase
from .common import LadderTeamInfo


class CreateLadderTeamResponseData(ModelBase):
    """创建天梯房间响应数据。"""

    error_code: int = Field(..., description="错误码。")
    team_info: LadderTeamInfo = Field(..., description="创建后的队伍信息。")
    match_mode: int = Field(..., description="匹配模式代码。")
    in_anchor_whitelist: bool = Field(..., description="是否在主播白名单。")


class CreateLadderTeamResponse(ResponseModel[CreateLadderTeamResponseData]):
    """创建天梯房间响应。"""