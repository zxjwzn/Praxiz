from __future__ import annotations

from pydantic import Field

from .base import GenericApiResponse
from .base import ModelBase


class SaveReactionResultEnvelope(ModelBase):
    """保存反应测试结果接口内部响应。"""

    code: int = Field(..., description="业务状态码。")
    msg: str = Field(..., description="业务状态说明。")
    data: bool = Field(..., description="是否保存成功。")


class SaveReactionResultResponse(GenericApiResponse[SaveReactionResultEnvelope]):
    """保存反应测试结果响应。"""