from __future__ import annotations

from pydantic import Field

from .base import RequestModel


class SendTeamMsgRequest(RequestModel):
    """发送队伍聊天请求。"""

    text: str = Field(..., description="聊天文本内容。")
    type: int = Field(..., description="消息类型代码，具体含义待补充。")