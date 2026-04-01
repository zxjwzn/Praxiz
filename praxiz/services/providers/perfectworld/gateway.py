"""基于类型化请求/响应模型的异步 Perfectworld API 网关。"""

from __future__ import annotations

import httpx
from pydantic import BaseModel

from praxiz.models.perfectworld.api.requests import (
    AddFriendRequest,
    CreateLadderTeamRequest,
    GetCurrentSeasonInfoRequest,
    GetCurrentUserInfoRequest,
    GetFriendListRequest,
    GetMatchDetailRequest,
    GetMatchZoneRequest,
    GetUserCommentListRequest,
    GetUserMatchCalendarRequest,
    GetUserMatchHistoryRequest,
    GetUserSeasonStatsRequest,
    LeaveLadderTeamRequest,
    LoginRequest,
    SaveReactionResultRequest,
    SearchFriendRequest,
    SendFriendMsgRequest,
    SendTeamMsgRequest,
)
from praxiz.models.perfectworld.api.responses import (
    AddFriendResponse,
    CreateLadderTeamResponse,
    ResponseModel,
    GetCurrentSeasonInfoResponse,
    GetCurrentUserInfoResponse,
    GetFriendListResponse,
    GetMatchDetailResponse,
    GetMatchZoneResponse,
    GetUserCommentListResponse,
    GetUserMatchCalendarResponse,
    GetUserMatchHistoryResponse,
    GetUserSeasonStatsResponse,
    LeaveLadderTeamResponse,
    LoginResponse,
    SaveReactionResultResponse,
    SearchFriendResponse,
    SendFriendMsgResponse,
    SendTeamMsgResponse,
)

from praxiz.services.providers.gateway_base import AsyncJsonGatewayBase
from praxiz.services.providers.perfectworld.errors import (
    PerfectWorldGatewayError,
    PerfectworldApiError,
    PerfectworldNetworkError,
    PerfectworldValidationError,
)


class PerfectWorldGateway(AsyncJsonGatewayBase):
    """面向选定 Perfectworld API 路由的类型化异步网关。"""

    def __init__(
        self,
        *,
        base_url: str = "http://127.0.0.1:28888",
        timeout_seconds: float = 10.0,
        client: httpx.AsyncClient | None = None,
    ) -> None:
        super().__init__(
            base_url=base_url,
            timeout_seconds=timeout_seconds,
            client=client,
        )

    def _build_network_error(self, *, message: str) -> PerfectWorldGatewayError:
        return PerfectworldNetworkError(message)

    def _build_validation_error(self, *, message: str) -> PerfectWorldGatewayError:
        return PerfectworldValidationError(message)

    def _raise_for_api_error(self, *, url: str, response: BaseModel) -> None:
        if not isinstance(response, ResponseModel):
            raise PerfectworldValidationError(f"{url} 的响应结构校验失败")
        if not response.ok:
            if response.error is None:
                raise PerfectworldApiError(
                    code="UNKNOWN_ERROR",
                    message="缺少错误数据载荷",
                )
            raise PerfectworldApiError(
                code=response.error.code,
                message=response.error.message,
            )

    async def login(self, *, request: LoginRequest) -> LoginResponse:
        """通过 api 触发完美世界对战平台登录/登出事件"""

        return await self.post_json(
            path="/api/call/login",
            payload=request,
            response_model=LoginResponse,
        )

    async def get_current_user_info(
        self,
        *,
        request: GetCurrentUserInfoRequest,
    ) -> GetCurrentUserInfoResponse:
        """获取当前登录用户信息"""

        return await self.post_json(
            path="/api/call/get_current_user_info",
            payload=request,
            response_model=GetCurrentUserInfoResponse,
        )

    async def get_current_season_info(
        self,
        *,
        request: GetCurrentSeasonInfoRequest,
    ) -> GetCurrentSeasonInfoResponse:
        """获取当前赛季数据"""

        return await self.post_json(
            path="/api/call/get_current_season_info",
            payload=request,
            response_model=GetCurrentSeasonInfoResponse,
        )

    async def get_user_season_stats(
        self,
        *,
        request: GetUserSeasonStatsRequest,
    ) -> GetUserSeasonStatsResponse:
        """获取指定用户在指定赛季的统计数据"""

        return await self.post_json(
            path="/api/call/get_user_season_stats",
            payload=request,
            response_model=GetUserSeasonStatsResponse,
        )

    async def get_user_match_history(
        self,
        *,
        request: GetUserMatchHistoryRequest,
    ) -> GetUserMatchHistoryResponse:
        """获取目标用户的比赛历史记录"""
        return await self.post_json(
            path="/api/call/get_user_match_history",
            payload=request,
            response_model=GetUserMatchHistoryResponse,
        )

    async def get_match_detail(
        self,
        *,
        request: GetMatchDetailRequest,
    ) -> GetMatchDetailResponse:
        """获取指定比赛的详情数据"""

        return await self.post_json(
            path="/api/call/get_match_detail",
            payload=request,
            response_model=GetMatchDetailResponse,
        )

    async def add_friend(self, *, request: AddFriendRequest) -> AddFriendResponse:
        """添加好友。"""

        return await self.post_json(
            path="/api/call/add_friend",
            payload=request,
            response_model=AddFriendResponse,
        )

    async def create_ladder_team(
        self,
        *,
        request: CreateLadderTeamRequest,
    ) -> CreateLadderTeamResponse:
        """创建天梯房间。"""
        return await self.post_json(
            path="/api/call/create_ladder_team",
            payload=request,
            response_model=CreateLadderTeamResponse,
        )

    async def get_friend_list(
        self,
        *,
        request: GetFriendListRequest,
    ) -> GetFriendListResponse:
        """获取好友列表。"""

        return await self.post_json(
            path="/api/call/get_friend_list",
            payload=request,
            response_model=GetFriendListResponse,
        )

    async def get_match_zone(
        self,
        *,
        request: GetMatchZoneRequest,
    ) -> GetMatchZoneResponse:
        """获取匹配区域网络测速信息。"""

        return await self.post_json(
            path="/api/call/get_match_zone",
            payload=request,
            response_model=GetMatchZoneResponse,
        )

    async def get_user_comment_list(
        self,
        *,
        request: GetUserCommentListRequest,
    ) -> GetUserCommentListResponse:
        """获取用户评论列表。"""

        return await self.post_json(
            path="/api/call/get_user_comment_list",
            payload=request,
            response_model=GetUserCommentListResponse,
        )

    async def get_user_match_calendar(
        self,
        *,
        request: GetUserMatchCalendarRequest,
    ) -> GetUserMatchCalendarResponse:
        """获取用户比赛日历。"""

        return await self.post_json(
            path="/api/call/get_user_match_calendar",
            payload=request,
            response_model=GetUserMatchCalendarResponse,
        )

    async def leave_ladder_team(
        self,
        *,
        request: LeaveLadderTeamRequest,
    ) -> LeaveLadderTeamResponse:
        """离开当前天梯房间。"""

        return await self.post_json(
            path="/api/call/leave_ladder_team",
            payload=request,
            response_model=LeaveLadderTeamResponse,
        )

    async def save_reaction_result(
        self,
        *,
        request: SaveReactionResultRequest,
    ) -> SaveReactionResultResponse:
        """保存反应测试结果。"""

        return await self.post_json(
            path="/api/call/save_reaction_result",
            payload=request,
            response_model=SaveReactionResultResponse,
        )

    async def search_friend(
        self,
        *,
        request: SearchFriendRequest,
    ) -> SearchFriendResponse:
        """按昵称搜索好友。"""

        return await self.post_json(
            path="/api/call/search_friend",
            payload=request,
            response_model=SearchFriendResponse,
        )

    async def send_friend_msg(
        self,
        *,
        request: SendFriendMsgRequest,
    ) -> SendFriendMsgResponse:
        """发送好友私信。"""

        return await self.post_json(
            path="/api/call/send_friend_msg",
            payload=request,
            response_model=SendFriendMsgResponse,
        )

    async def send_team_msg(
        self,
        *,
        request: SendTeamMsgRequest,
    ) -> SendTeamMsgResponse:
        """发送队伍聊天消息。"""

        return await self.post_json(
            path="/api/call/send_team_msg",
            payload=request,
            response_model=SendTeamMsgResponse,
        )
