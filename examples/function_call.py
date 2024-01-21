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
