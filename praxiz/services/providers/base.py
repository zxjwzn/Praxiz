"""业务网关与外部服务对接的 Provider 抽象。"""

from __future__ import annotations

from abc import ABC


class BaseProvider(ABC):
    """所有第三方游戏数据源（如 PerfectWorld, FaceIt）的基类协议。
    
    实现者必须拦截特定平台的 API 调用细节，并将其统一转换为 Praxiz 的内部 Domain 模型响应。
    """
