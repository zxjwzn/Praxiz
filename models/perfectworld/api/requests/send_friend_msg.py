from __future__ import annotations

from pydantic import Field

from .base import RequestModel


class SendFriendMsgRequest(RequestModel):
    """发送好友私信请求。"""

    chatChannel: int = Field(..., description="聊天频道类型，具体含义待补充。")
    uid: str = Field(..., description="目标用户的 SteamID。")
    text: str = Field(..., description="私信文本内容。")