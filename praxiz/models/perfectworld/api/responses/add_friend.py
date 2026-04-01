from __future__ import annotations

from pydantic import Field

from .base import ResponseModel
from .base import ModelBase


class AddFriendResponseData(ModelBase):
    """添加好友响应数据。"""

    err_code: int = Field(..., alias="errCode", description="错误码，0 通常表示成功。")


class AddFriendResponse(ResponseModel[AddFriendResponseData]):
    """添加好友响应。"""