# ZhipuaiToolKit
ZhipuaiToolKit 是一个基于 GLM-4 模型开发的外部工具集合，旨在增强和扩展 ZhipuAI 的功能。这些工具简化了常见任务，提供了额外的功能，使 ZhipuAI 的使用更加直观和强大。

## 安装
要安装 ZhipuaiToolKit，请运行以下命令：
```bash
pip install zhipuai_toolkit
```

## 使用示例
以下是一个使用 ZhipuaiToolKit 的示例：
```python
from zhipuai_toolkit import Tool
from zhipuai import ZhipuAI
import json
YOUR_API_KEY = 'YOUR API KEY'
# 使用类装饰器，并传递参数
@Tool(
    name="my_function",
    description="函数描述",
    params={
        "参数1": {"type": "string", "description": "参数1描述"},
        "参数2": {"type": "string", "description": "参数2描述"},
        "参数3": {"type": "string", "description": "参数3描述"},
    },
    required_params=["参数1", "参数2"],
)
def my_function(参数1, 参数2, 参数3=None):
    """
    这是一个函数文档字符串。
    """
    print(f"调用 my_function，参数1：{参数1}, 参数2：{参数2}, 参数3：{参数3}")
    return 参数1, 参数2, 参数3
client = ZhipuAI(api_key=YOUR_API_KEY)
messages = [{"role": "user", "content": "请为我调用my_function函数"}]
response = client.chat.completions.create(
    model="glm-4", messages=messages, tools=Tool.get_tools()
)
messages.append(response.choices[0].message.model_dump())
if response.choices[0].message.tool_calls:
    tool_call = response.choices[0].message.tool_calls[0]
    args = tool_call.function.arguments
    func_result = Tool.dispatch(tool_call.function.name, json.loads(args))
    messages.append(
        {
            "role": "tool",
            "content": f"{json.dumps(func_result)}",
            "tool_call_id": tool_call.id,
        }
    )
response = client.chat.completions.create(
    model="glm-4", messages=messages, tools=Tool.get_tools()
)
print(response.choices[0].message.model_dump())
```

## 工具类
ZhipuaiToolKit 包含一个名为 `Tool` 的类，用于存储和管理工具。每个工具都有名称、描述、参数和必需的参数。您可以通过 `dispatch` 方法调用工具，并传入参数。如果参数缺失或工具未找到，`dispatch` 方法将抛出异常或返回一个有意义的错误消息。

## 许可证
ZhipuaiToolKit 在 MIT 许可证下发布。有关详细信息，请参阅 [LICENSE](LICENSE) 文件。

## 联系方式
如果您有任何问题或建议，请通过 [helio609.dev@outlook.com](mailto:helio609.dev@outlook.com) 联系我。

```
请根据您的具体需求和项目特点调整上述内容，例如添加实际的特性、安装指南、使用示例和联系方式。如果您计划将项目开源到 GitHub，确保您的描述清楚地传达了项目的目的和如何参与。
