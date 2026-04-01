"""Jinja2 模板引擎实现。"""

from __future__ import annotations

from pathlib import Path
from typing import Any
from typing import Mapping

from jinja2 import Environment
from jinja2 import FileSystemLoader
from jinja2 import TemplateNotFound
from jinja2 import select_autoescape

from .errors import RenderTemplateNotReadyError


class Jinja2TemplateEngine:
    """从文件系统中的 Jinja2 模板渲染 HTML。"""

    def __init__(self, *, template_dir: Path) -> None:
        self._template_dir = template_dir
        self._environment = Environment(
            loader=FileSystemLoader(str(template_dir)),
            autoescape=select_autoescape(enabled_extensions=("html", "xml")),
        )

    async def render(self, *, template_name: str, context: Mapping[str, Any]) -> str:
        """使用给定上下文映射渲染模板。"""

        try:
            template = self._environment.get_template(template_name)
        except TemplateNotFound as exc:
            raise RenderTemplateNotReadyError(
                f"模板文件尚未就绪：{self._template_dir / template_name}"
            ) from exc
        return template.render(**dict(context))
