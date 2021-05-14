# 安装 .whl .egg

> Python安装第三方库，如何安装 .whl 和 .egg 文件
>
> 在Python的第三方库中，除了源码和二进制exe之外，.whl文件和.egg文件也是两种常用的文件类型。

## .whl 文件

```
.whl文件：现在常见的一种二进制格式
首先需要安装wheel库: pip install wheel

然后下载所需的.whl文件,最后用pip命令在.whl文件所在的位置安装
pip install h:/path/xxx.whl

清华源：
	https://pypi.tuna.tsinghua.edu.cn/simple
pip install torch-1.2.0-cp36-cp36m-linux_aarch64.whl 
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple torch-1.2.0-cp36-cp36m-linux_aarch64.whl 
```

## .egg 文件

```
egg文件是一种打包，后缀名可以改成rar，直接解压缩，按照源码的形式安装
一种最简单的安装方法就是把egg文件和egg文件解压出来的文件夹直接复制到Python的第三方库文件夹..Lib\site-packages中
```

# import搜索路径

```

```

# TX2导入whl问题解决

## cv2、torch

```
(venv36) nvidia@tegra-ubuntu:~/zll/zlpy3$ python3
Python 3.6.13 (default, Feb 20 2021, 21:42:50) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import cv2
Illegal instruction (core dumped)

# https://blog.csdn.net/xiaosongshine/article/details/114168235

可以使用临时添加方法，在运行Python指令前运行：export OPENBLAS_CORETYPE=ARMV8
也可以采用增加系统变量方法，可以进行全局修改。
将“export OPENBLAS_CORETYPE=ARMV8”加入到“~/.bashrc”中

vim ~/.bashrc
source ~/.bashrc 
```

# Python 基于 pip 实现离线打包

## 虚拟环境复制迁移

```
-----依赖于主环境
直接压缩生成的venv文件夹：
tar -zcvf venv.tar.gz ./venv

然后拷贝迁移至其他服务器下进行解压：
tar -zxvf FileName.tar.gz # 解压
tar -C DesDirName -zxvf FileName.tar.gz # 解压到目标路径

进入./venv/bin/下修改activate文件中参数：

VIRTUAL_ENV="/home/venv"
export VIRTUAL_ENV

将上述VIRTUAL_ENV修改为当前venv文件夹正确的路径，然后执行:
source activate

然后执行:
which python
或者
which pip

查看是否是虚拟venv路径下的工具，如果是的话，则成功。
---------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------
pip freeze > requirements.txt
pip install -r requirements.txt
---------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------
python -m virtualenv venv_dummy
source venv_dummy/bin/activate
(venv_dummy): pip install virtualenv-clone
(venv_dummy): virtualenv-clone venv1/ venv2/
```

## pip3离线打包

```
1. 已装模块统计并保持到requirements.txt
pip3 freeze > /home/nvidia/zll/requirements.txt
2. 将统计的模块下载到本地文件夹
pip3 download -r /home/nvidia/zll/requirements.txt -d /home/nvidia/zll/requirement

3. 在新环境安装复制过来的模块文件夹
pip install -r requirements.txt --no-index --find-links=file://your_download_dir

pip3 wheel --wheel-dir=./requirement -r requirements.txt

pip install –download /tmp/packages -r requirements.txt
```