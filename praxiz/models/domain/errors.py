"""Praxiz 领域核心异常基类。"""

from __future__ import annotations


class PraxizError(Exception):
    """所有项目内业务失败的基类。由底层的 provider 或 domain 抛出的异常都应该继承自它。"""
