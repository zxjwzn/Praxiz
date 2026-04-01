"""提供第三方数据源实例的工厂。"""

from __future__ import annotations

from .base import BaseProvider
from .perfectworld.provider import PerfectWorldProvider


class ProviderFactory:
    """根据请求的平台特征，返回对应适配的 BaseProvider 子类。"""

    @classmethod
    def create_provider(cls, platform: str) -> BaseProvider:
        """实例化 Provider 对象。"""
        normalized = platform.lower()
        if normalized in ("pw", "perfectworld", "pwesports","wanmei"):
            return PerfectWorldProvider()
        
        # 后续可通过 elif 增加 FaceIt 等其它平台
        raise ValueError(f"不受支持的平台数据源: {platform}")
