"""基于 Playwright 的 HTML 快照实现。"""

from __future__ import annotations

from playwright.async_api import Error as PlaywrightError
from playwright.async_api import async_playwright

from .errors import RenderPipelineError


class PlaywrightSnapshotEngine:
    """使用无头 Chromium 捕获 HTML 截图。"""

    async def html_to_png(
        self,
        *,
        html: str,
        viewport_width: int,
        viewport_height: int,
    ) -> bytes:
        """在无头浏览器中渲染 HTML 并捕获 PNG 字节。"""

        try:
            async with async_playwright() as playwright:
                browser = await playwright.chromium.launch(headless=True)
                context = await browser.new_context(
                    viewport={"width": viewport_width, "height": viewport_height}
                )
                page = await context.new_page()
                await page.set_content(html, wait_until="networkidle")
                png_bytes = await page.screenshot(type="png", full_page=True)
                await context.close()
                await browser.close()
                return png_bytes
        except PlaywrightError as exc:
            raise RenderPipelineError("Playwright 快照失败") from exc
