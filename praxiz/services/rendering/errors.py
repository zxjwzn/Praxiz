"""渲染服务相关异常定义。"""

from __future__ import annotations

from praxiz.models.domain.errors import PraxizError


class RenderPipelineError(PraxizError):
    """渲染流水线执行失败时抛出。"""


class RenderTemplateNotReadyError(RenderPipelineError):
    """模板文件尚未实现时抛出。"""
