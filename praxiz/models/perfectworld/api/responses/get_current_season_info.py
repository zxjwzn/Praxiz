from __future__ import annotations

from pydantic import Field

from .base import ResponseModel
from .base import ModelBase


class SeasonPropagandaInfo(ModelBase):
    """赛季宣传信息。"""

    start_time: str = Field(..., alias="startTime", description="宣传开始时间戳字符串，单位待补充。")
    end_time: str = Field(..., alias="endTime", description="宣传结束时间戳字符串，单位待补充。")
    summary_title: str = Field(..., alias="summaryTitle", description="宣传主标题。")
    summary_title1: str = Field(..., alias="summaryTitle1", description="宣传副标题。")
    propaganda_content: str = Field(..., alias="propagandaContent", description="宣传文案内容。")


class SeasonPropagandaPointInfo(ModelBase):
    """赛季宣传图点位信息。"""

    id: str = Field(..., description="点位 编号。")
    image1_url: str = Field(..., alias="image1Url", description="宣传图片 链接。")


class CurrentSeasonPayload(ModelBase):
    """当前赛季业务数据。"""

    is_on: bool = Field(..., alias="isOn", description="当前赛季活动是否开启。")
    propaganda_info: SeasonPropagandaInfo = Field(..., alias="propagandaInfo", description="赛季宣传信息。")
    propaganda_point_infos: list[SeasonPropagandaPointInfo] = Field(..., alias="propagandaPointInfos", description="赛季宣传图片点位列表。")
    on: bool = Field(..., description="是否开启，和 isOn 含义可能相近，待确认。")


class CurrentSeasonEnvelope(ModelBase):
    """赛季接口内部响应。"""

    code: int = Field(..., description="业务状态码。")
    msg: str = Field(..., description="业务状态说明。")
    data: CurrentSeasonPayload | None = Field(..., description="赛季业务载荷。")


class GetCurrentSeasonInfoResponse(ResponseModel[CurrentSeasonEnvelope]):
    """当前赛季信息响应。"""