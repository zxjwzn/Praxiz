"""HTML 渲染与快照生成的契约定义。"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any
from typing import Mapping
from typing import Protocol


@dataclass(frozen=True)
class RenderedImage:
    """由渲染流水线产出的二进制图片输出。"""

    file_name: str
    mime_type: str
    content: bytes


class TemplateEngine(Protocol):
    """模板渲染器契约。"""

    async def render(self, *, template_name: str, context: Mapping[str, Any]) -> str:
        """根据模板与上下文映射渲染 HTML。"""

        ...


class SnapshotEngine(Protocol):
    """用于图片输出的 HTML 快照契约。"""

    async def html_to_png(
        self,
        *,
        html: str,
        viewport_width: int,
        viewport_height: int,
    ) -> bytes:
        """将 HTML 内容捕获为 PNG 字节。"""

        ...
