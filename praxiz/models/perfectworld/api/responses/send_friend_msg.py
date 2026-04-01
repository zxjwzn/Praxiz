from __future__ import annotations

from pydantic import Field

from .base import ResponseModel
from .base import ModelBase


class SendFriendMsgResponseData(ModelBase):
    """发送好友消息响应数据。"""

    message_id: str = Field(..., alias="messageId", description="消息 编号。")
    err_code: int = Field(..., alias="errCode", description="错误码。")
    target_online: bool = Field(..., alias="targetOnline", description="目标用户是否在线。")


class SendFriendMsgResponse(ResponseModel[SendFriendMsgResponseData]):
    """发送好友私信响应。"""