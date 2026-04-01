from typing import Any
from typing import Mapping

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field


class DomainResponseBase(BaseModel):
    """统一网关响应的基类。所有 Provider 必须隐式或显式返回此基类的子类。"""

    model_config = ConfigDict(extra="allow")
    raw_data: dict = Field(
        default_factory=dict, description="原始响应数据的完整记录，供后续调试和分析使用"
    )

    def to_template_context(self) -> Mapping[str, Any]:
        """渲染引擎调用的默认方法，将响应结构化为渲染模板参数。"""
        return self.model_dump(mode="json")
