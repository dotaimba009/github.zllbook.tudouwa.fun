## Python特点

> Python3源码文件默认UTF-8编码，所有字符串都是unicode字符串，也可以指定不同的编码。
>
> Python最具特色的就是使用缩进来表示代码块，不需要使用大括号。缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数。

## 程序运行路径

```
获取命令行参数可以满足需求：
sys.argv[0] 
# 在当前文件夹下运行  python .\pythontest.py -> .\pythontest.py
# 在其他文件夹下运行	 python .\pythontest\pythontest.py -> .\pythontest\pythontest.py
# 编成exe双击运行 pythontest.exe -> D:\Pro\pythontest\dist\pythontest.exe
# 编成exe当前文件夹命令行 pythontest.exe->D:\Pro\pythontest\dist\pythontest.exe
# 编成exe其他文件夹命令行 .\dist\pythontest.exe->D:\Pro\pythontest\dist\pythontest.exe
  
获取其绝对路径
os.path.abspath(sys.argv[0])
可以通过路径操作函数处理路径
current_exec_dirname, current_exec_filename = os.path.split(current_exec_abspath)
```

## JSON 组装与解析

| Python 编码为 Json对应的 Json类型                  | Json解码为Python对应的Python类型            |
| -------------------------------------------------- | :------------------------------------------ |
| dict 对应 object                                   | object 对应 dict                            |
| list,tuple 对应 array                              | array 对应 list                             |
| str 对应 string                                    | string 对应 str                             |
| int, float, int- & float-derived Enums 对应 number | number(int) 对应 int                        |
| True 对应 true   False 对应 false                  | number(real) 对应 float                     |
| None 对应 null                                     | true -- True  false -- False   null -- None |

```
import json
json.dumps ： 将 Python 对象编码成 JSON 字符串
json.loads ： 将已编码的JSON字符串解码为Python对象。用于解码JSON数据，该函数返回Python字段的数据类型。

# Python 字典类型转换为 JSON 对象
data = {
    'no' : 1,
    'name' : 'Runoob',
    'url' : 'http://www.runoob.com'
}

json_str = json.dumps(data)
print ("Python 原始数据：", repr(data))
print ("JSON 对象：", json_str)

# 将 JSON 对象转换为 Python 字典
data2 = json.loads(json_str)
print ("data2['name']: ", data2['name'])
print ("data2['url']: ", data2['url'])

如果你要处理的是文件而不是字符串，你可以使用json.dump() 和json.load()来编码和解码JSON数据。例如：
# 写入 JSON 数据
with open('data.json', 'w') as f:
    json.dump(data, f)
 
# 读取数据
with open('data.json', 'r') as f:
    data = json.load(f)
```



```
{
	"cmd": "FoodParse", //固定字段
	"errorCode": 0,
	"errorMessage": "成功",
	"data": {
		"result_num": 1,
		"result": [{
			"location": {},
			"dishes": [{}, {}]
		}]
	}
}

{
	"cmd": "FoodParse",
	"errorCode": 0,
	"errorMessage": "成功",
	"data": {
		"result_num": 3,
		"result": [{
			"location": {
				"height": 500,
				"left": 100,
				"top": 20,
				"width": 466
			},
			"dishes": [{
					"dishName": "包子",
					"score": 0.98
				},
				{
					"dishName": "包子",
					"score": 0.98
				}
			]
		}]
	}
}
// 组装以上的Json串
def dishsearch():
    resultList = []
    n = 0
    while n < 3:
        topn = {'location': {'left': 100, 'top': 20, 'width': 466, 'height': 500}, 'dishes': []}
        dishesList = []
        m = 0
        while m < 2:
            dishN = {'score': 0.98, 'dishName': '包子'}
            dishesList.append(dishN)
            m = m + 1

        topn['dishes'] = dishesList

        resultList.append(topn)
        n = n + 1

    errorCode = 0
    errorMessage = '成功'
    result_num = len(resultList)

    result = {}
    resultObj = json.loads(json.dumps(result))
    resultObj['cmd'] = 'FoodParse'
    resultObj['errorCode'] = errorCode
    resultObj['errorMessage'] = errorMessage
    resultObj['data'] = {'result_num': result_num, 'result': []}
    resultObj['data']['result'] = resultList

    # data = json.dumps(resultObj, ensure_ascii=False)
    return resultObj
```

## QA

```
1. 字符串前面加上'r'是防止字符转义的，如果路径中出现'\t' '\n'等，加了 r 就能保留原有的样子。
2. #当行注释，多行注释用：单引号 '''注释'''  或 双引号 """注释"""
```



## 字符串格式化

```
f-Strings 是 python3.6 加入标准库的一种改进python格式字符串的新方法
用法1：
	name = "ll"
	age = 75
	f/F "hello, {name}. You are {age}."
用法2：任意表达式
	f"{2 * 37} --> '74'
	f"{name.lower()} is funny."

message = (f"Hi {name}. "
        f"You are a {profession}. "
        f"You were in {affiliation}.")
        ==> 'Hi Eric. You are a comedian. You were in Monty Python.'
message = (f"Hi {name}. "
        "You are a {profession}. "
        "You were in {affiliation}.")
        ==> 'Hi Eric. You are a {profession}. You were in {affiliation}.'
```

