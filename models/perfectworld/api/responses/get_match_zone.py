from __future__ import annotations

from pydantic import Field

from .base import GenericApiResponse
from .base import ModelBase


class MatchZoneItem(ModelBase):
    """匹配大区节点。"""

    index: int = Field(..., description="排序索引。")
    id: str = Field(..., description="节点 ID。")
    title: str = Field(..., description="大区标题。")
    ip: str = Field(..., description="服务器 IP。")
    port: str = Field(..., description="服务器端口。")
    zone_id: str = Field(..., description="大区 ID。")
    ping_ip: str | None = Field(..., description="用于测速的 IP。")
    status: str = Field(..., description="节点状态代码。")
    location: str = Field(..., description="地理分区。")
    name: str = Field(..., description="节点名称。")
    speed: str = Field(..., description="测速结果。")


class GetMatchZoneResponseData(ModelBase):
    """匹配大区响应数据。"""

    code: int = Field(..., description="业务状态码。")
    city_list: list[MatchZoneItem] = Field(..., alias="cityList", description="城市节点列表。")
    data: list[MatchZoneItem] = Field(..., description="节点列表。")


class GetMatchZoneResponse(GenericApiResponse[GetMatchZoneResponseData]):
    """获取匹配大区响应。"""