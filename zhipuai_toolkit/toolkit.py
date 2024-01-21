import inspect
from typing import List, Dict, Any, Callable

class Tool:
    ZHIPUAI_TOOLS = []  # 类变量，用于存储工具信息

    @classmethod
    def dispatch(cls, func_name: str, params: Dict[str, Any], raise_error: bool = True) -> Any:
        # 在ZHIPUAI_TOOLS中查找具有给定名称的函数
        for tool in cls.ZHIPUAI_TOOLS:
            if tool['meta']['function']['name'] == func_name:
                # 检查所有必需的参数是否都已提供
                required_params = tool['meta']['function']['parameters']['required']
                for param in required_params:
                    if param not in params:
                        if raise_error:
                            raise ValueError(f"Missing required parameter: {param}")
                        else:
                            return f"Missing required parameter: {param}"

                # 执行找到的函数并返回结果
                try:
                    return tool['func'](**params)
                except Exception as e:
                    if raise_error:
                        raise
                    else:
                        return str(e)

        # 如果没有找到函数，则根据raise_error的值决定是否抛出异常或返回提示
        if raise_error:
            raise ValueError(f"Function '{func_name}' not found in ZHIPUAI_TOOLS")
        else:
            return f"Function '{func_name}' not found in ZHIPUAI_TOOLS"

    @classmethod
    def get_tools(cls) -> List[Dict[str, Any]]:
        return [tool["meta"] for tool in cls.ZHIPUAI_TOOLS]

    def __init__(self, name=None, description='', params=None, required_params=None):
        self.name = name
        self.description = description
        self.params = params or {}
        self.required_params = required_params or []

    def __call__(self, func):
        # 使用`self`中的参数创建参数的meta信息
        params_meta = {}
        for param_name, param_info in self.params.items():
            param_type = param_info.get('type', 'string')
            param_desc = param_info.get('description', '')
            params_meta[param_name] = {
                "type": param_type,
                "description": param_desc,
            }

        # 创建函数的meta信息
        meta = {
            "type": "function",
            "function": {
              "name": self.name or func.__name__,
              "description": self.description or func.__doc__,
              "parameters": {
                  "type": "object",
                  "properties": params_meta,
                  "required": self.required_params,
              },
            }
        }

        # 将meta信息和函数本身加入到ZHIPUAI_TOOLS列表中
        Tool.ZHIPUAI_TOOLS.append({"meta": meta, "func": func})

        # 返回原函数
        return func