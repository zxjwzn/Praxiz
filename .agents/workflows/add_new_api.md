---
description: 如何在 Praxiz 系统中添加新的平台 API 并打通完整的数据获取流
---
# 添加新 API 接口的工作流指南 (Workflow for Adding a New API)

当前系统采用了严谨的“六边形/端口适配器”架构。如果需要接入一个新的第三方平台 API 并将数据提取至业务层渲染，**必须严格遵守** 领域层（Domain）与 平台实现层（Platform API）彻底隔离的原则。

当你作为 Agent 被指派“增加某个 API 并获取某某字段”的任务时，请**按顺序执行以下 5 个标准步骤**：

## Step 1: 编写领域层模型 (Domain Models)
**领域层模型是跨平台的，定义了系统内部最终需要哪些字段。不携带任何特定平台相关的冗余 JSON 结构。**

1. **请求模型**：在 `praxiz/models/domain/requests/` 目录下创建 `<api_name>.py`：
   - 类继承自 `DomainRequestBase`。
   - 定义请求所需的业务通用字段（如 `uid`, `platform`）。
   - 在 `praxiz/models/domain/requests/__init__.py` 中导入该类并加入 `__all__`。
2. **响应模型**：在 `praxiz/models/domain/responses/` 目录下创建 `<api_name>.py`：
   - 类继承自 `DomainResponseBase`。
   - 定义业务最终需要的精简数据字段（如 `ban_reason`, `end_time`）。
   - 在 `praxiz/models/domain/responses/__init__.py` 中导入该类并加入 `__all__`。

## Step 2: 编写平台原生 API 模型 (Platform API Models)
**这部分模型用于严格反序列化来自第三方 HTTP 接口的真实 JSON，包含平台特有字段。**

以 `perfectworld` 平台为例：
1. **请求结构**：在 `praxiz/models/perfectworld/api/requests/` 下创建 `<api_name>.py`，精确按照平台要求的 Body 编写 `pydantic` 模型。并更新其目录下的 `__init__.py`。
2. **响应结构**：在 `praxiz/models/perfectworld/api/responses/` 下创建 `<api_name>.py`。
   - **注意**：你需要在此解析 API 返回的复杂嵌套解构。通常这会用到带有 `data: List[xxx]` 的嵌套 Pydantic Model 模型。
   - 更新 `__init__.py`。

## Step 3: 在网关层增加网络通信方法 (Update Gateway)
**网关层只负责发送 HTTP 请求并将结果校验反序列化为 Platform API Response 模型，不得包含任何业务逻辑。**

1. 打开该平台对应的网关文件（如 `praxiz/services/providers/perfectworld/gateway.py`）。
2. 从 Step 2 导入刚创建的特定 API 的 Request/Response 模型。
3. 增加此 API 的类型化异步请求方法。例如：
   ```python
   async def get_user_ban_status(
       self,
       *,
       request: GetUserBanStatusRequest,
   ) -> GetUserBanStatusResponse:
       """获取用户封禁信息"""
       return await self.post_json(
           path="/api/call/get_ban_status",
           payload=request,
           response_model=GetUserBanStatusResponse,
       )
   ```

## Step 4: 在 Provider 中执行数据转换 (Update Provider)
**Provider 层负责将 Domain 和 Platform 两套模型缝合起来。**

1. 打开平台的业务提供者实现类（如 `praxiz/services/providers/perfectworld/provider.py`）。
2. 在类 `PerfectWorldProvider` 中增加新的异步方法。**该方法的入参和出参必须是 Step 1 创建的 Domain 模型。**
3. 遵循以下逻辑顺序编写方法：
   - **入参转换**：将 `Domain Request` 转化为该平台的 `Platform API Request`。
   - **调用网关**：触发网关 (`await self._gateway.xxx()`) 获取真实的 `Platform API Response`。
   - **响应处理**：遇到空数据/异常返回默认值。如果有数据，提取 `Platform API Response` 中层层嵌套的特定字段。
   - **出参转换**：将提取出的数据组装并赋值给 `Domain Response` 模型后返回。

## Step 5: 更新基类协议 (Update Base Provider)
**确保其他可能的平台在未来被调用相同的业务行为。**

1. 打开 `praxiz/services/providers/base.py` (`BaseProvider`)。
2. 将刚才在 `PerfectWorldProvider` 新增的方法提取为基类规范（如果没有严格要求接口类型，可酌情补充为抽象方法或仅作注释声明）。

---
**Agent 操作建议**：
接到 API 需求时，切忌在一个文件里解决战斗。始终梳理清楚：**你从平台 API (JSON) 要拿出的脏字段是什么**，以及 **系统 Domain 最终想要呈现的干净字段是什么**。按上述 5 步剥洋葱式地执行即可。
