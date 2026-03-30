from __future__ import annotations

from pydantic import Field

from .base import GenericApiResponse
from .base import ModelBase


class SearchFriendUser(ModelBase):
    """搜索好友结果中的用户信息。"""

    steam_id: str = Field(..., description="用户 SteamID。")
    zq_id: str = Field(..., description="完美平台站内 ID。")
    nickname: str = Field(..., description="用户昵称。")
    avatar: str = Field(..., description="头像 URL。")
    valid_nickname: int = Field(..., description="昵称是否有效。")
    valid_avatar: int = Field(..., description="头像是否有效。")
    pw_level: int = Field(..., alias="pwLevel", description="完美平台等级。")


class SearchFriendPayload(ModelBase):
    """搜索好友业务数据。"""

    total: int = Field(..., description="搜索结果总数。")
    users: list[SearchFriendUser] = Field(..., description="用户结果列表。")


class SearchFriendEnvelope(ModelBase):
    """搜索好友接口内部响应。"""

    code: int = Field(..., description="业务状态码。")
    msg: str = Field(..., description="业务状态说明。")
    data: SearchFriendPayload = Field(..., description="搜索结果载荷。")


class SearchFriendResponse(GenericApiResponse[SearchFriendEnvelope]):
    """搜索好友响应。"""