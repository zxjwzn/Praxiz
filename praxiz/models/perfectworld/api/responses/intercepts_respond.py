from __future__ import annotations

from .base import ResponseModel
from .base import ModelBase


class InterceptRespondResponseData(ModelBase):
    """响应拦截事件响应数据。"""


class InterceptRespondResponse(ResponseModel[InterceptRespondResponseData]):
    """响应拦截事件响应。"""