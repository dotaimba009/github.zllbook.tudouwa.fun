# 简介

> py2exe，Pyinstaller，Cx_freeze，Nuitka都可以完成python打包的任务，Pyinstaller和Nuitka都号称跨平台，但其实顶多只能算是工具本身跨平台，实际体验中不仅打包产生的文件不能跨平台，能否成功打包本身也不确定。
>
> Python唯二的难题运行速度和源代码反编译，一直是被众多语言所诟病，Nuitka项目就是解决这两个难题而生的。

# Pyinstaller介绍

python的打包工具很多，推荐使用 pyinstaller 来打包，能少走不少弯路。

官网地址：<http://www.pyinstaller.org/>

github 地址： <https://github.com/pyinstaller/pyinstaller>

> PyInstaller在Windows、GNU/Linux、Mac OS X、FreeBSD、Solaris和AIX下将Python应用程序打包为独立的可执行文件。
>
> PyInstaller 不是一个python包，也不是库，其相当于独立出来专门干打包 python 的工具，当然，PyInstaller依赖python环境。另外：不同的 PyInstaller 版本依赖，支持不同的 Python 版本，比如：Release 3.5 supports Python 2.7, 3.4–3.7，如果你的机器上装的不是这些python版本，则需要重新安装python和pyinstaller。不建议通过各种方法让其好用，可能有其它隐患。
>
> PyInstaller其实就是把python解析器和你自己的脚本打包成一个可执行的文件，和编译成真正的机器码完全是两回事，所以千万不要指望成打包成一个可执行文件会提高运行效率，相反可能会降低运行效率，好处就是在运行者的机器上不用安装python和你的脚本依赖的库。在Linux操作系统下，它主要用的binutil工具包里面的ldd和objdump命令。
>
> PyInstaller输入你指定的的脚本，首先分析脚本所依赖的其他脚本，然后去查找，复制，把所有相关的脚本收集起来，包括Python解析器，然后把这些文件放在一个目录下，或者打包进一个可执行文件里面。
>
> 可以直接发布输出的整个文件夹里面的文件，或者生成的可执行文件。你只需要告诉用户，你的应用App是自我包含的，不需要安装其他包，或某个版本的Python，就可以直接运行了。
>
> **需要注意的是，PyInstaller打包的执行文件，只能在和打包机器系统同样的环境下。也就是说，不具备可移植性，若需要在不同系统上运行，就必须针对该平台进行打包。**

## 安装

可以根据官网的提示，快速安装

```
安装命令：
	pip install pyinstaller
	或 pip install pyinstaller==3.1
更新新版本命令：
	pip install --upgrade pyinstaller
可以使用 pyinstaller -v 查看其版本
```

​	或者直接下载其安装包（比如可以在 github 上直接下载其压缩包），经过系列操作，比如编译、配置环境变量等，解压后，找到 setup.py 所在文件夹，运行 `python setup.py install`。

​	这里建议直接通过安装命令直接下载安装，能省去一堆麻烦事。如无特殊需要，不必刨根问底，这就像我们使用 ”碗“ 来吃饭一样，作为程序员我们需要了解和学习的东西太多太多，人生苦短，我们使用工具，仅仅是学会能更好的使用即可，我们可以探究 “碗” 除了吃饭，是不是还可以用来喝酒，用来喝酒是否适合场景、氛围。如无特殊需要，我们没必要去了解，碗的制作过程和工具，还是那句话，人生苦短。如果兴趣使然，而且还有空闲时间，多了解也无坏处。一般情况下，我们都是遇到问题了，采取刨根问底。

```
进入程序的目录运行：`pyinstaller xxxx.py` 会在程序目录下创建 build 和 dist 文件夹。
windows下查看python的安装路径，可以通过环境变量查看。

对于打包 flask ，打包成功，运行失败，提示找不到 falsk `ModuleNotFoundError: No module named 'flask'` 此时需要运行
pyinstaller -F .\main.py --hidden-import=flask
```

## 打包单个exe文件

```
-F 选项可以打出一个exe文件，默认是 -D，意思是打成一个文件夹。
pyinstaller -F TestDataGen.py

打出的桌面程序去掉命令行黑框
-w 选项可以打桌面程序，去掉命令行黑框
pyinstaller -F -w TestDataGen.py

修改程序默认图标
-i 可以设置图标路径，将图标放在根目录：
pyinstaller -F -w -i gen.ico TestDataGen.py
```

## 打包坑

```
1. 打开生成的spec文件，修改其默认脚本，完成自定义打包需要的配置。spec文件是一个python脚本.
	pyi-makespec -w xxx.py
 
递归深度设置：在打包导入某些模块时，常会出现"RecursionError: maximum recursion depth exceeded"的错误，这可能是打包时出现了大量的递归超出了python预设的递归深度。因此需要在spec文件上添加递归深度的设置，设置一个足够大的值来保证打包的进行，即
    import sys
    import os.path as osp
    sys.setrecursionlimit(5000)
去除不必要的模块import：有时需要让pyinstaller不打包某些用不到的模块，可通过在excludes=[]中添加此模块实现，如
	excludes=['zmq']
    
2. 使用spec执行打包命令
	pyinstaller -D xxx.spec
```

```

pyinstaller --paths  D:\Python\JDReminding\venv\Lib\site-packages\shiboken2 hello.py


```

# nuitka介绍

> 经测试，Nuitka打包后的exe比Pyinstaller打包后的exe运行速度提升30%，PyQT5的UI文件转换成py文件转换成C语言后，界面秒开。
>
> 从效率和编译的角度来看，系统的库直接让打包好的exe文件夹内的 python3x.dll 来执行，不用去理会各个模块的版本依赖，实现高度自治。
>
> 自己业务的部分，如UI界面和数据库连接以及函数和功能实现，需要加密和快速反应的，这部分借助 Nuitka 来实现。
>
> 以下是Nuitka的关键命令段
>
> - --nofollow-imports  #所有的import全部不使用，交给python3x.dll执行
> - --follow-import-to=need #need为你需要编译成C/C++的py文件夹
>
> 自建 need 文件夹，将自己的业务代码放进去，修改 from need.xxx import yyyy、import need.xxxx as x 等
>
> ```
> nuitka --standalone --mingw64 --show-memory --show-progress --nofollow-imports --plugin-enable=qt-plugins --follow-import-to=need  --output-dir=o 你的.py
> 
> nuitka --standalone --windows-disable-console --mingw64 --nofollow-imports --show-memory --show-progress --plugin-enable=qt-plugins --follow-import-to=need --recurse-all --output-dir=o 你的.py
> 
> nuitka --standalone --show-memory --show-progress --nofollow-imports --output-dir=out main.py
> nuitka --standalone --show-memory --show-progress --output-dir=out main.py
> 
> //2021-02-21
> python -m nuitka main.py
> python -m nuitka --standalone --show-memory --show-progress --follow-imports --output-dir=out main.py
> ```
>

## 安装

```
conda install nuitka
python -m nuitka --version


pip install nuitka
pip install -U "https://github.com/Nuitka/Nuitka/archive/develop.zip"
--mingw64  #默认为已经安装的vs2017去编译，否则就按指定的比如mingw
--standalone  独立文件，这是必须的
--windows-disable-console 没有CMD控制窗口
--recurse-all  所有的资源文件 这个也选上
-recurse-not-to=numpy,jinja2 不编译的模块，防止速度会更慢
--output-dir=out  生成exe到out文件夹下面去
--show-progress 显示编译的进度，很直观
--show-memory 显示内存的占用
--plugin-enable=pylint-warnings  报警信息
--plugin-enable=qt-plugins  需要加载的PyQT插件
```

## 1

```
如下是一条完整的命令 编译的py文件为index.py
nuitka --mingw64 --windows-disable-console --standalone --show-progress --show-memory --plugin-enable=qt-plugins --plugin-enable=pylint-warnings --recurse-all --recurse-not-to=numpy,jinja2 --output-dir=out index.py

--nofollow-imports   #所有的import全部不使用，交给python3x.dll执行
--follow-import-to=need  #need为你需要编译成C/C++的py文件夹



```

## 使用

# cx-freeze

> python中比较常用的python转exe方法有三种，分别是cx_freeze,py2exe，PyInstaller。py2exe恐怕是三者里面知名度最高的一个，但是同时相对来说它的打包质量恐怕也是最差的一个。pyinstaller打包很好，但是操作工序较为复杂，推荐cx_freeze，可以通过pip install cx-freeze 安装。
>
> pip install cx-freeze==5.1.1
>
> 
>
> cxfreeze main.py --target-dir dir1

