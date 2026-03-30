from __future__ import annotations

from pydantic import Field

from .base import GenericApiResponse
from .base import ModelBase
from .common import LadderTeamInfo


class LeaveLadderTeamResponseData(ModelBase):
    """离开天梯房间响应数据。"""

    leaved_player_id: str = Field(..., description="离开的玩家 ID。")
    team_info: LadderTeamInfo = Field(..., description="离开后的队伍信息。")


class LeaveLadderTeamResponse(GenericApiResponse[LeaveLadderTeamResponseData]):
    """离开天梯房间响应。"""