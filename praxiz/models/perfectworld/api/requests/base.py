from __future__ import annotations

from pydantic import BaseModel
from pydantic import ConfigDict


class RequestModel(BaseModel):
    """所有请求模型的基类。"""

    model_config = ConfigDict(populate_by_name=True, extra="forbid")


class EmptyRequest(RequestModel):
    """空请求体。"""