"""Perfectworld 提供者实现，负责调用 API 并映射到业务领域模型。"""

from __future__ import annotations

from praxiz.models.domain.requests import SearchFriendRequest
from praxiz.models.domain.responses import (
    FriendInfoItem,
    SearchFriendResponse,
)
from praxiz.services.providers.base import BaseProvider
from praxiz.services.providers.perfectworld.gateway import PerfectWorldGateway
from praxiz.models.perfectworld.api.requests import (
    SearchFriendRequest as PerfectWorldSearchFriendRequest
)
from praxiz.models.perfectworld.api.responses import (
    SearchFriendResponse as PerfectWorldSearchFriendResponse
)


class PerfectWorldProvider(BaseProvider):
    """完美世界数据源。"""

    def __init__(self, gateway: PerfectWorldGateway | None = None) -> None:
        self._gateway = gateway or PerfectWorldGateway()

    async def search_friend(self, request: SearchFriendRequest) -> SearchFriendResponse:
        """根据用户输入的 UID 搜索并返回平台内部的玩家 ID。"""
        pw_request = PerfectWorldSearchFriendRequest(
            name=request.name,
            page=1,
        )
        pw_response: PerfectWorldSearchFriendResponse = await self._gateway.search_friend(
            request=pw_request,
        )
        if pw_response.data is None:
            return SearchFriendResponse(friends=[])

        pw_users = pw_response.data.data.users
        response = SearchFriendResponse(
            friends=[
                FriendInfoItem(
                    uid=user.zq_id,
                    nickname=user.nickname,
                    avatar_url=user.avatar or None,
                )
                for user in pw_users
            ]
        )
        return response
