from __future__ import annotations

from pydantic import Field

from .base import RequestModel


class SendTeamMsgRequest(RequestModel):
    """发送队伍聊天请求。"""

    text: str = Field(..., description="聊天文本内容。")
    type: int = Field(default=1, description="消息类型代码,1为普通消息,2为系统消息,3呼出新手引导界面,4发送上一对局赛后总结,5发送表情包。3和4内容与text无关")