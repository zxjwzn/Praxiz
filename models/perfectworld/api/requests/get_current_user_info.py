from __future__ import annotations

from .base import EmptyRequest


class GetCurrentUserInfoRequest(EmptyRequest):
    """获取当前登录用户信息请求。"""