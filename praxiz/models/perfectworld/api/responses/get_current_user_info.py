from __future__ import annotations

from pydantic import Field

from .base import ResponseModel
from .base import ModelBase


class CurrentUserInfoData(ModelBase):
    """当前登录用户信息。"""

    id: str = Field(..., description="当前登录用户的 平台编号。")
    nickname: str = Field(..., description="当前用户昵称。")
    avatar: str = Field(..., description="头像 链接。")
    zqid: str = Field(..., description="完美平台站内 编号，具体含义待补充。")
    token: str = Field(..., description="当前登录令牌。")
    jt: str = Field(..., description="会话令牌 或会话凭证字符串。")
    valid_nickname: str = Field(..., description="校验后的有效昵称。")
    user_type: str = Field(..., description="用户类型，当前样本为空字符串。")
    login_type: int = Field(..., description="登录类型代码，具体含义待补充。")
    ip_addr: str = Field(..., alias="ipAddr", description="当前登录 网络地址。")
    adult: int = Field(..., description="是否成年标识，具体枚举待补充。")
    real_name_valid: int = Field(..., description="实名认证是否有效。")
    real_name_valid_type: int = Field(..., description="实名认证类型代码，含义待补充。")
    first_charge_activity_start: int = Field(..., alias="firstChargeActivityStart", description="首充活动开始时间戳。")
    first_charge_activity_end: int = Field(..., alias="firstChargeActivityEnd", description="首充活动结束时间戳。")
    has_charged: bool | None = Field(..., alias="hasCharged", description="是否已充值，样本中为 空值。")
    has_used_discount: bool | None = Field(..., alias="hasUsedDiscount", description="是否已使用折扣，样本中为 空值。")
    login_method: str = Field(..., description="登录方式标识。")
    is_vip: bool = Field(..., alias="isVip", description="是否为 会员 用户。")
    vip_level: int = Field(..., alias="vipLevel", description="会员 等级。")
    member_sub_type: int = Field(..., alias="memberSubType", description="会员子类型代码。")
    is_subscription: int = Field(..., alias="isSubscription", description="是否订阅会员。")
    expire_time: int = Field(..., alias="expireTime", description="会员到期时间戳，0 表示无。")
    create_time: int = Field(..., description="账号创建时间戳。")


class GetCurrentUserInfoResponse(ResponseModel[CurrentUserInfoData]):
    """当前登录用户信息响应。"""