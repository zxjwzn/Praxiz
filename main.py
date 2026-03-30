from __future__ import annotations

import json
import os
import sys
from typing import Any
from urllib import request

from models.perfectworld.api.requests import GetCurrentSeasonInfoRequest
from models.perfectworld.api.requests import GetCurrentUserInfoRequest
from models.perfectworld.api.requests import GetUserSeasonStatsRequest
from models.perfectworld.api.requests import LoginRequest
from models.perfectworld.api.requests import RequestModel
from models.perfectworld.api.responses import CurrentSeasonInfoResponse
from models.perfectworld.api.responses import CurrentUserInfoResponse
from models.perfectworld.api.responses import GetUserSeasonStatsResponse
from models.perfectworld.api.responses import LoginResponse

BASE_URL = os.getenv("PWHOOK_BASE_URL", "http://127.0.0.1:28888")
sys.stdout.reconfigure(encoding="utf-8")


def require_env(name: str) -> str:
    """读取必需环境变量。"""

    value = os.getenv(name)
    if value:
        return value
    raise SystemExit(f"Missing required environment variable: {name}")


def post_json(path: str, payload: RequestModel) -> dict[str, Any]:
    """向本地 PWHook 服务发送 JSON POST 请求。"""

    body = json.dumps(payload.model_dump(by_alias=True)).encode("utf-8")
    http_request = request.Request(
        f"{BASE_URL}{path}",
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    with request.urlopen(http_request) as response:
        return json.loads(response.read().decode("utf-8"))


def main() -> None:
    login_request = LoginRequest(
        type="logined",
        token=require_env("PWHOOK_TOKEN"),
        uid=require_env("PWHOOK_LOGIN_UID"),
        login_method=os.getenv("PWHOOK_LOGIN_METHOD", "0"),
    )
    target_steam_id = os.getenv("PWHOOK_TARGET_STEAM_ID", "76561198314958323")
    target_season = os.getenv("PWHOOK_TARGET_SEASON", "S23")

    login_response = LoginResponse.model_validate(
        post_json("/api/call/login", login_request)
    )
    current_user_response = CurrentUserInfoResponse.model_validate(
        post_json("/api/call/get_current_user_info", GetCurrentUserInfoRequest())
    )
    current_season_response = CurrentSeasonInfoResponse.model_validate(
        post_json("/api/call/get_current_season_info", GetCurrentSeasonInfoRequest())
    )
    season_stats_response = GetUserSeasonStatsResponse.model_validate(
        post_json(
            "/api/call/get_user_season_stats",
            GetUserSeasonStatsRequest(
                uid=target_steam_id,
                season=target_season,
                current_season=target_season,
            ),
        )
    )

    if login_response.data is None:
        raise SystemExit("login response missing data")
    if current_user_response.data is None:
        raise SystemExit("current user response missing data")
    if current_season_response.data is None or current_season_response.data.data is None:
        raise SystemExit("current season response missing payload data")
    if season_stats_response.data is None or season_stats_response.data.data is None:
        raise SystemExit("season stats response missing payload data")

    season_payload = season_stats_response.data.data
    summary = {
        "login_fired": login_response.data.fired,
        "current_user": {
            "steam_id": current_user_response.data.id,
            "nickname": current_user_response.data.nickname,
            "login_method": current_user_response.data.login_method,
        },
        "current_season": {
            "is_on": current_season_response.data.data.is_on,
            "summary_title": current_season_response.data.data.propaganda_info.summary_title,
        },
        "season_stats": {
            "steam_id": season_payload.ladder.steam_id,
            "season": season_payload.ladder.season,
            "score": season_payload.ladder.score,
            "win_rate": season_payload.ladder.win_rate,
            "map_count": len(season_payload.map),
            "weapon_count": len(season_payload.weapon),
            "radar_description": season_payload.radar_new.description,
        },
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
