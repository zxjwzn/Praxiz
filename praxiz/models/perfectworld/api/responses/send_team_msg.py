from __future__ import annotations

from pydantic import Field

from .base import ResponseModel
from .base import ModelBase


class SendTeamMsgResponseData(ModelBase):
    """发送队伍消息响应数据。"""

    error_code: int = Field(..., description="错误码。")
    chat_text: str = Field(..., description="回显的聊天文本。")
    match_started: bool = Field(..., description="比赛是否已开始。")


class SendTeamMsgResponse(ResponseModel[SendTeamMsgResponseData]):
    """发送队伍聊天响应。"""