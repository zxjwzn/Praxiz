from __future__ import annotations

from pydantic import Field

from .base import GenericApiResponse
from .base import ModelBase


class FriendListItem(ModelBase):
    """好友列表项。"""

    account_id: str = Field(..., alias="accountId", description="好友账号 ID。")
    nickname: str = Field(..., description="好友昵称。")
    avatar: str = Field(..., description="好友头像 URL。")
    head_frame_id: int = Field(..., alias="headFrameId", description="头像框 ID。")
    online_status: int = Field(..., alias="onlineStatus", description="在线状态代码。")
    apply_time: int = Field(..., alias="applyTime", description="申请时间戳。")
    apply_status: int = Field(..., alias="applyStatus", description="申请状态代码。")
    game_status: str = Field(..., alias="gameStatus", description="游戏状态 JSON 字符串。")
    viewer_status: str = Field(..., alias="viewerStatus", description="观战状态字符串。")


class FriendListResponseData(ModelBase):
    """好友列表响应数据。"""

    friend_type: int = Field(..., alias="friendType", description="好友列表类型。")
    friend_list: list[FriendListItem] = Field(..., alias="friendList", description="好友列表。")


class GetFriendListResponse(GenericApiResponse[FriendListResponseData]):
    """获取好友列表响应。"""