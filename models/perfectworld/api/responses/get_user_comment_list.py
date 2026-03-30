from __future__ import annotations

from pydantic import Field

from .base import GenericApiResponse
from .base import ModelBase


class UserCommentItem(ModelBase):
    """用户评论项。"""

    id: int = Field(..., description="评论 ID。")
    comment: str = Field(..., description="评论内容。")
    sender_nick_name: str = Field(..., alias="senderNickName", description="发送者昵称。")
    like_cnt: int = Field(..., alias="likeCnt", description="点赞数。")
    gmt_create: str = Field(..., alias="gmtCreate", description="评论创建时间。")


class UserCommentListEnvelope(ModelBase):
    """评论列表接口内部响应。"""

    code: int = Field(..., description="业务状态码。")
    msg: str = Field(..., description="业务状态说明。")
    data: list[UserCommentItem] = Field(..., description="评论列表。")


class GetUserCommentListResponse(GenericApiResponse[UserCommentListEnvelope]):
    """获取评论列表响应。"""