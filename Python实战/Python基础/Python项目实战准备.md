# 搭建Python高效开发环境Pycharm + Anaconda

**Pycharm**：目前一款主流的 Python 集成开发环境，它带有一整套帮助我们在Python开发时提高效率的工具，比如调试、语法高亮、Project管理、代码跳转、智能提示、自动完成、单元测试、版本控制。总的来说，

Pycharm 会极大地提高我们 Python 开发的效率和体验，用过都说好。

**Anaconda**：主要针对 Python 的数据科学整合包，包括有 Numpy，Pandas，Sklearn等。重要的是，自带管理软件 conda，它拥有安装，更新，删除，解决包依赖关系的包管理功能。同时，conda拥有环境管理功能，能创建独立运行环境， 使各项目间包环境和版本互不冲突和影响。另外，Conda 还可以管理包括 Bowtie2，FastQC 等软件环境，甚至 R 包环境。

总之，Anaconda 就是我们在编程时的管家，一切麻烦事扔给他，我们只要关注项目本身就行。

可以到其官网下载安装.

**有了 Anaconda 的支持，为什么还要 Conda 环境？**

Anaconda 环境包含各种数据分析，机器学习等包，可以直接拿来用，并不需要再安装一遍，方便实用。但是，有时候，我们并不需要这么多的包，而是需要特定版本的 Python 或者 Python 包，或是依赖冲突等问题，这就要求有一个独立运行的环境。而 Conda 建立的环境正好满足了这个需求。

# 安装CUDA和cuDNN

> 安装教程可参考：<https://zhuanlan.zhihu.com/p/94220564>
>
> YOLOv5可以在以下任何一个最新的验证过的环境中运行(所有依赖项包括CUDA/CUDNN, Python和PyTorch预安装)。我们知道做深度学习离不开GPU，不过一直以来对GPU和CPU的差别，CUDA以及cuDNN都不是很了解。介绍：<https://blog.csdn.net/u014380165/article/details/77340765>
>
> <https://blog.csdn.net/qq_34649170/article/details/90050132>
>
> 查看GPU是否支持 cudnn ：<https://developer.nvidia.com/zh-cn/cuda-gpus>

```
CUDA 安装验证
nvcc -V

为什么将数据转移至GPU的方法叫做.cuda而不是.gpu，就像将数据转移至CPU调用的方法是.cpu？这是因为GPU的编程接口采用CUDA，而目前并不是所有的GPU都支持CUDA，只有部分Nvidia的GPU才支持。PyTorch未来可能会支持AMD的GPU，而AMD GPU的编程接口采用OpenCL，因此PyTorch还预留着.cl方法，用于以后支持AMD等的GPU。
```

# Python项目管理流程

> setup.py 与 requirements.txt

## 开发完成后

> 开发完成后，打包依赖，生成 requirements.txt，有两种方式：

1. 使用 pip freeze > requirements.txt 命令将项目的库依赖导出，作为代码的一部分。

   ```
   使用 pip freeze > requirements.txt
   这种方式，会将环境中的依赖包全都加入，如果使用的全局环境，则下载的所有包都会在里面，不管是不是当前项目依赖的，适用于单虚拟环境。
   ```

2. 使用 pipreqs （https://github.com/bndr/pipreqs）（推荐）

   ```
   此类方法推荐使用，他只是总结程序中所用到的包，并不是电脑中安装的所有的包。
   # 安装
   pip install pipreqs
   # 在当前目录生成(cd 到项目目录)
   pipreqs . --encoding=utf8 --force
   
   注意 --encoding=utf8 为使用utf8编码，不然可能会报UnicodeDecodeError: 'gbk' codec can't decode byte 0xae in position 406: illegal multibyte sequence 的错误。
   --force 强制执行，当生成目录下的requirements.txt存在时覆盖。
   ```

## 代码上传服务器

```

```

## 在服务器上创建一个虚拟环境

```
conda create --name zlltest python=3.8
```

## 激活虚拟环境，安装项目依赖。

```
1. 激活虚拟环境
	conda activate zlltest
2. 安装项目依赖（在线安装）
	pip install -r requirements.txt
	
  	如果下载慢或下载不下来，可以使用国内源安装项目依赖：
  	（使用国内清华源，推荐使用清华源）
  	pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
  	
  	pip install -i http://pypi.douban.com/simple --trusted-host pypi.douban.com -r requirements.txt
  	

	如果涉及权限问题，可以如下：
	pip install --user -i http://pypi.douban.com/simple --trusted-host pypi.douban.com -r requirements.txt

  	查看是否成功：pip list显示安装的依赖
```

```
1. 离线安装
第一步：将requirements.txt中导入的包离线下载到packagesdir 文件夹:
pip download -d D:\360MoveData\Users\Administrator\Desktop\我\packagesdir  -r requirements.txt
第二步：安装离线的包:
pip install --no-index --find-links=DIR -r requirements.txt

解释：
DIR：离线包（temp）的路径（temp的路径，例如：D:\360MoveData\Users\Administrator\Desktop\我\packagesdir）
安装requirements.txt中的包，并且在D:\360MoveData\Users\Administrator\Desktop\我\packagesdir这个文件夹里取离线的包
```

