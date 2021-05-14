# 基本概念

> 包和模块的作用：造轮子，工具代码，供其他模块使用；划分了变量作用域，解决变量/函数重名的问题。

**模块：** 将一组功能相关的代码写入一个单独的 .py 文件，需要时进行导入，这个文件就是模块。

**包：** 有层次的文件目录结构，内部有多个模块或多个子包，一般要有 `__init__.py`这个文件（3.3+的版本不需要）。

**库：** 完成一定功能代码的集合，完成的功能一般更加广泛，可以是模块，也可以是包。

**框架：** 通过框架，可以快速实现解决某一个问题所需的代码股价，后期进行填充即可。

> 包和模块的分类：内建的模块:builtin，会自动导入；第三方包/模块：需要下载安装才能使用；自定义包/模块：自己写；

- 创建模块：就是创建一个 .py 文件
- 创建包：
  - 新建一个文件夹，为了兼容，添加一个 `__init__.py` 文件（当包被导入时，会运行这个文件）。
  - 在文件中设置 `__all__` 变量，可以限制能够通过 `from package import *` 所导出的模块。
  - 注意事项：
    - 多个关系密切的模块应该组织成一个包，以便于维护和使用，还能有效避免名字空间冲突。
    - 通常包总是一个目录，可以使用import导入包，或者from + import来导入包中的部分模块。
    - 无论一个包的哪个部分被导入，在文件`__init__.py`中的代码都会运行，这个文件的内容允许为空，不过通常情况下它用来存放包的初始化代码。导入过程遇到的所有`__init__.py` 文件都被运行。

# 包和模块的导入

> **import 模块**：导入一个模块；注：相当于导入的是一个文件夹，是个相对路径。
>
> **from…import**：导入了一个模块中的一个函数；注：相当于导入的是一个文件夹中的文件，是个绝对路径。

## 常规导入，导入了所有资源

```
import module  # 直接导入一个包，可以直接使用 __init__.py的内容
module.val # 访问变量
module.func() # 调用函数

# 模块在其他的包中
import p.module
p.module.val

# 一次导入多个模块
import p.module, module, module_2


使用from语句可将模块中的对象直接导入到当前名字空间，from语句不创建一个到模块名字空间的引用对象，而是把被导入模块的一个或多个对象直接放入当前的名字空间。
from socket import gethostname # 将gethostname放如当前名字空间
print gethostname()            # 直接调用  
socket.gethostname()           # 引发异常NameError: socket 
  
  
一个模块如果定义有列表__all__，则from module import * 语句只能导入__all__列表中存在的对象
```

## from 语句，只导入部分资源

```
# 从包中导入模块
from p import module
module.val

from p import module1, module2
from p import module1 as m1, module2 as m2
from p.sub_p import m # 正确写法
from p import sub_p.m # 错误写法

# 从模块中导入资源
from module import val, func
print(val) # 直接使用
func()

from p.mudule import val # 正确写法
from p import module.val #  错误写法

from p import * # 导入了 p 包下的所有模块，受到 __init__.py文件中__all__变量的约束
from module import * # 导入了 module下的所有资源，受到模块中 __all__变量的约束
# 使用 * 进行导入，容易产生同名冲突
```

## 示例

```
项目目录结构如下： -xx代表目录，.py代表文件
-pro
	-module_dir_2
		module2_1.py
		module2_2.py
	-module_dir_3
		module3.py
		module3_1.py
		module3_2.py
	main.py
	module1.py
	module1_2.py
	
main.py中的代码
    import module1  # 导入同级目录并运行模块module1，文件名即模块名
    from module1_2 import module1_2_func1 # 导入同级目录模块的函数
    import module_dir_2.module2_1 as module2___1
    import module_dir_2.module2_2 as module2___2
    from module_dir_2 import module2_1
    from module_dir_3 import module3_1
```

# 导入的本质

- 第一次导入
- 被导入的模块会在**自己的命名空间**中执行所有的代码。
- 代码执行完成后，会产生一个**模块对象**，模块中的所有属性都绑定到这个对象上，对象的名称就是模块名。
- 目标模块在**import**位置建立引用，就可以根据模块对象的**名称**来访问资源了。
- 第二次导入
- 直接建立到对象的引用，也就是第一次导入的第三步。
- **两种导入方式都会执行模块的所有代码，所以不存在第二种方式更省内存的说法，只是拿不同的部分来使用。**

# 模块检索路径

- 检索模块按照一定的顺序进行，优先在具有**较高优先级**的地方查找。
- 先在**内置模块**中查找，若自己定义了一个和内置模块重名的模块，进行导入时，会导入内置的那个模块。
- 然后在sys.path(是一个**路径列表**)中查找
- 当前目录
- 环境变量PYTHONPATH
- 特定路径下的.pth文件所指定的路径
- python安装目录下的lib
- 追加路径的方式 (在sys.path中**增加**自定义的路径)




