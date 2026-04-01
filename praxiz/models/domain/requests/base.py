"""Praxiz 内部统一数据请求的基类。"""

from pydantic import BaseModel


class DomainRequestBase(BaseModel):
    """所有 Praxiz 内部业务请求的基类。"""

    platform: str
