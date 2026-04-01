"""编排模板与快照引擎的渲染服务。"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any
from typing import Mapping

from .contracts import RenderedImage
from .contracts import SnapshotEngine
from .contracts import TemplateEngine


@dataclass(frozen=True)
class RenderRequest:
    """HTML 转图片渲染的输入契约。"""

    template_name: str
    context: Mapping[str, Any]
    output_file_name: str
    viewport_width: int = 1280
    viewport_height: int = 720


class HtmlImageRenderer:
    """渲染 HTML 模板并捕获 PNG 输出。"""

    def __init__(
        self, *, template_engine: TemplateEngine, snapshot_engine: SnapshotEngine
    ) -> None:
        self._template_engine = template_engine
        self._snapshot_engine = snapshot_engine

    async def render(self, request: RenderRequest) -> RenderedImage:
        """执行完整渲染流水线。"""

        html = await self._template_engine.render(
            template_name=request.template_name,
            context=request.context,
        )
        image_bytes = await self._snapshot_engine.html_to_png(
            html=html,
            viewport_width=request.viewport_width,
            viewport_height=request.viewport_height,
        )
        return RenderedImage(
            file_name=request.output_file_name,
            mime_type="image/png",
            content=image_bytes,
        )
