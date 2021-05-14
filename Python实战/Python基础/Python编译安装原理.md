## Python的源码包和二进制包

> 源码包：源码包安装的过程，是先解压，再编译，最后才安装，所以它是跨平台的，由于每次安装都要进行编译，相对二进包安装方式来说安装速度较慢。源码包的本质是一个压缩包，其常见的格式有.zip，.tar，.gz，.bz2，.Z
>
> 二进制包：二进制包的安装过程省去了编译的过程，直接进行解压安装，所以安装速度较源码包来说更快。由于不同平台的编译出来的包无法通用，所以在发布时，需事先编译好多个平台的包。二进制包的常见格式有.egg，.whl

### egg 和 wheels 的区别

Egg 格式是由 setuptools 在 2004 年引入，而 Wheel 格式是由 PEP427 在 2012 年定义。Wheel 的出现是为了替代 Egg，Egg的本质是一个zip包，其现在被认为是 Python 的二进制包的标准格式。

- Wheel 有一个官方的 PEP427 来定义，而 Egg 没有 PEP 定义
- Wheel 是一种分发格式，即打包格式。而 Egg 既是一种分发格式，也是一种运行时安装的格式，并且是可以被直接 import
- Wheel 文件不会包含 .pyc 文件
- Wheel 使用和 PEP376 兼容的 .dist-info 目录，而 Egg 使用 .egg-info 目录
- Wheel 有着更丰富的命名规则。
- Wheel 是有版本的。每个 Wheel 文件都包含 wheel 规范的版本和打包的实现
- Wheel 在内部被 sysconfig path type 管理，因此转向其他格式也更容易

wheel可以通过pip安装，需要先安装wheel模块，再使用其他命令：

```
pip install wheel
pip wheel --wheel-dir=/local/wheels pkg
```

### distutils

> distutils是python的一个标准库（distribute utils分发工具），由python官方开发的打包工具，其精髓在于setup.py，它是模块分发与安装的指导文件。
>
> 我们经常使用python setup.py install来安装源码

```
Anaconda:
	conda install torchvision -c pytorch
pip:
	pip install torchvision
From source:
	python setup.py install
```

### setuptools

> setuptools是 Python Enterprise Application Kit（PEAK）的一个副项目，它是一组Python的 distutilsde工具的增强工具（适用于 Python 2.3.5 以上的版本，64 位平台则适用于 Python 2.4 以上的版本），可以让程序员更方便的创建和发布 Python 包，特别是那些对其它包具有依赖性的状况。

```
pip install setuptools
```

**功能亮点：**

- 利用EasyInstall自动查找、下载、安装、升级依赖包
- 创建Python Eggs
- 包含包目录内的数据文件
- 自动包含包目录内的所有的包，而不用在setup.py中列举
- 自动包含包内和发布有关的所有相关文件，而不用创建一个MANIFEST.in文件
- 自动生成经过包装的脚本或Windows执行文件
- 支持Pyrex，即在可以setup.py中列出.pyx文件，而最终用户无须安装Pyrex
- 支持上传到PyPI
- 可以部署开发模式，使项目在sys.path中
- 用新命令或setup()参数扩展distutils，为多个项目发布/重用扩展
- 在项目setup()中简单声明entry points，创建可以自动发现扩展的应用和框架

