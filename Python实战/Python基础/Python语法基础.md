- 默认情况下，Python 3 源码文件以 **UTF-8** 编码，所有字符串都是 unicode 字符串

# 数字

	int,bool,float(浮点数),complex(复数)

# 字符串

- python中单引号和双引号使用完全相同

- 使用三引号可以指定一个多行字符串

- 转义符 ` '\'`，反斜杠可以用来转义，使用 r 可以让反斜杠不发生转义。如：

  ```
  r"this is a line whit \n"，则\n会显示，不是换行`
  ```

- 字符串可以用 + 运算符连接在一起，用 * 运算符重复

- python中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始

- 字符串的截取的语法格式如下：**变量[头下标:尾下标:步长]**

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

# 列表list

```
- 列表可以完成大多数集合类的数据结构实现，列表中元素的类型可以不相同，支持数字，字符串甚至可以包含里列表。
- 列表是写在方括号 [] 之间，用逗号分隔开的元素列表。
- 和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。
#!/usr/bin/python3

list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
tinylist = [123, 'runoob']
 
print (list)            # 输出完整列表
print (list[0])         # 输出列表第一个元素
print (list[1:3])       # 从第二个开始输出到第三个元素
print (list[2:])        # 输出从第三个元素开始的所有元素
print (tinylist * 2)    # 输出两次列表
print (list + tinylist) # 连接列表
```

# 元组Tuple

```
元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。
元组中的元素类型也可以不相同： 
#!/usr/bin/python3
tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )
tinytuple = (123, 'runoob')
print (tuple)             # 输出完整元组
print (tuple[0])          # 输出元组的第一个元素
print (tuple[1:3])        # 输出从第二个元素开始到第三个元素
print (tuple[2:])         # 输出从第三个元素开始的所有元素
print (tinytuple * 2)     # 输出两次元组
print (tuple + tinytuple) # 连接元组

虽然tuple的元素不可改变，但它可以包含可变的对象，比如list列表。
构造包含 0 个或 1 个元素的元组比较特殊，所以有一些额外的语法规则： 
tup1 = ()    # 空元组
tup2 = (20,) # 一个元素，需要在元素后添加逗号
string、list 和 tuple 都属于 sequence（序列）。

1、与字符串一样，元组的元素不能修改。
2、元组也可以被索引和切片，方法一样。
3、注意构造包含 0 或 1 个元素的元组的特殊语法规则。
4、元组也可以使用+操作符进行拼接。
```

# 集合Set

```
集合（set）是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员。基本功能是进行成员关系测试和删除重复元素。可以使用大括号{ }或者set()函数创建集合，注意：创建一个空集合必须用set()而不是{},因为{}是用来创建一个空字典。

#!/usr/bin/python3
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(student)   # 输出集合，重复的元素被自动去掉
# 成员测试
if 'Rose' in student :
    print('Rose 在集合中')
else :
    print('Rose 不在集合中')
# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
print(a)
print(a - b)     # a 和 b 的差集
print(a | b)     # a 和 b 的并集
print(a & b)     # a 和 b 的交集
print(a ^ b)     # a 和 b 中不同时存在的元素
```

# 字典Dictionary

```
列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。字典是一种映射类型，字典用{}标识，它是一个无序的 键（key）：值（value）的集合。键必须使用不可变类型，在同一个字典中，键必须是唯一的。
#!/usr/bin/python3
dict = {}
dict['one'] = "1 - 教程"
dict[2]     = "2 - 工具"

tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}

print (dict['one'])       # 输出键为 'one' 的值
print (dict[2])           # 输出键为 2 的值
print (tinydict)          # 输出完整的字典
print (tinydict.keys())   # 输出所有键
print (tinydict.values()) # 输出所有值
{
    '包子': array([[2.9554849,..,0.45501372],[1.6043618,0.,...,0.]], dtype=float32), 
    '鱼头': array([[1.6043618,..., 0.]], dtype=float32), 
    '米饭': array([[0., 0., 2.9554849 , ..., 0., 0.,0.45501372]], dtype=float32)
}
```

































