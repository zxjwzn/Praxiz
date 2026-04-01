import asyncio
from pprint import pprint

from praxiz.models.domain.requests import GetPlayerStatsRequest
from praxiz.services.providers.factory import ProviderFactory

async def main():
    # 1. 构造 Praxiz 系统内部标准的领域请求模型
    # 只要改 platform="wanmei" 还是 platform="faceit"，往下走代码一字不用换
    request = GetPlayerStatsRequest(
        platform="wanmei",
        uid="76561198314958323",    # 测试用的模拟用户 ID
        season="S23"       # 放权给 Provider 内部自动匹配并缓存当前赛季
    )
    
    # 2. 调出数据工厂
    print(f"[*] 正在初始化 {request.platform} 平台的数据源...")
    provider = ProviderFactory.create_provider(request.platform)
    
    # 3. 发送请求
    # 内部将自动走：发起API网络请求 -> 取得API乱七八糟响应字段 -> 映射成规整的 PlayerStatsResponse
    print(f"[*] 正在进行业务调用与数据映射...")
    response = await provider.get_player_stats(request)
    
    # 4. 拿到非常纯净的数据，可以送给任何分析函数或渲染模板处理！
    print("\n====== [ 最终处理好的 Praxiz Domain Response ] ======")
    # 这里直接打印 pydantic 导出的结构化字典
    pprint(response.model_dump(mode="json"))
    print("=====================================================")


if __name__ == "__main__":
    asyncio.run(main())
