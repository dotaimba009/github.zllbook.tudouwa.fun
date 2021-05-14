# 虚拟环境介绍

> Python 应用经常需要使用一些包第三方包或者模块，有时需要依赖特定的包或者库的版本，所以不能有一个能适应所有 Python 应用的软件环境，很多时候不同的 Python 应用所依赖的版本是冲突的，满足了其中一个，另一个则无法运行，解决这一问题的方法是虚拟环境。虚拟环境是一个包含了特定 Python 解析器以及一些软件包的自包含目录，不同的应用程序可以使用不同的虚拟环境，从而解决了依赖冲突问题，而且虚拟环境中只需要安装应用相关的包或者模块，可以给部署提供便利。
>
> 虚拟环境并不是什么新技术，主要是利用了操作系统中环境变量以及进程间环境隔离的特性。
>
> Python 处理虚拟环境的包有好几种，conda用的比较多。

# pip、Conda、virtualenv

> pip 是最常用的包管理工具，通过 `pip install <packagename>` 命令格式来安装软件包，使用的是 pypi 软件包源。安装python自带pip，或者通过 `yum install python-pip` 安装。
>
> conda 多用作科学计算领域的包管理工具，功能丰富且强大，使用的软件包源是 Anaconda repository 和 Anaconda Cloud，conda 不仅支持 Python 软件包，还可以安装 C、C++ 、R 以及其他语言的二定制软件包。除了软件包管理外，还能提供相互隔离的软件环境。安装 Anaconda 自带 conda。
>
> virtualenv 是一个虚拟环境管理器，作为非数据科学领域的开发者来说是很实用的。它可以让你每个项目甚至每个脚本配置一个自定义的Python解释器环境，这最大的好处是可以不污染开发环境。可以通过 `pip install virtualenv` 安装。
>
> 如果说venv是虚拟环境管理器，pip是包管理器，那么conda则是两者的结合。
>
> conda虚拟环境是独立于操作系统解释器环境的，即无论操作系统解释器什么版本（哪怕2.7），我也可以指定虚拟环境python版本为3.6（见文章开头所说原博客），而venv是依赖主环境的。

# pip

```
安装python
sudo apt-get install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.6

删除python
sudo apt-get remove --auto-remove python3.4

pip install xxx -i https://pypi.tuna.tsinghua.edu.cn/simple some-package

清空回收站命令：
sudo rm -rf ~/.local/share/Trash/*
```

# conda 的使用

## 验证及帮助

```
验证conda已被安装，打开“Anaconda Prompt”，conda --version
通过conda --help学习conda怎么使用
```

## 清理conda

```
清理 conda
conda clean -p      //删除从不使用的包
conda clean -t      //删除tar包
conda clean -a		 //删除索引缓存，锁定文件，未使用的缓存包和包
```

## conda的虚拟环境管理

```
1. 显示所有的虚拟环境：conda env list
	（注意目录：base 在基目录，其它后天的环境在 envs 内[C:\anaconda3\envs]）
2. 创建一个名为 zlltest 环境，指定Python版本是3.8或2.7
	conda create --name zlltest python=3.8
	#conda create --name zlltest python=2.7
	conda create --name zlltest python=3.7.1 --channel https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
	
3. 激活名为 zlltest 的环境
	conda activate zlltest  # windows
	source activate zlltest # linux/mac
4. 切换环境
	conda activate zlltest
5. 退出环境
	deactivate   #windows
	source deactivate #linux
6. 删除一个名为 zlltest 的环境
	conda remove --name zlltest --all
7. 克隆oldname环境为newname环境
	conda create --name newname --clone oldname
	
conda update -n base -c defaults conda
conda clean --packages && conda clean --all && conda update --al
```

## conda的包管理

```
conda 的包管理功能是对pip的一种补充，如果当前已经激活了某个Python环境，那么就可以在当前环境开始安装第三方包。

conda list  # 查看当前环境下已安装的package

conda search numpy # 查找名为 numpy 的信息 package 的信息

conda install numpy  # 安装名为 numpy 的包
（conda install numpy 会自动安装 mkl(intel 加速科学计算的包)，而pip install numpy 则不会）

conda update numpy   # 更新numpy 包
conda uninstall numpy   # 卸载numpy 包

# -n指定环境 --channel指定源地址
conda install -n zlltest numpy # 在名为 zlltest 环境下安装 numpy 包

# 使用地址 https://conda.anaconda.org/anaconda 来安装tensorflow
conda install --channel https://conda.anaconda.org/anaconda tensorflow=1.8.0

对于那些用 pip 无法安装成功的模块你都可以尝试用 conda 来安装，如果用 conda 找不到相应的包，当然你继续选择 pip 来安装包也是没问题的。

升级
conda update conda  # 更新 conda
conda update anaconda # 更新 anaconda
conda update anaconda-navigator    #update最新版本的anaconda-navigator  
conda update python # 更新 python
```

# virtualenv的使用

## 创建一个目录

```
mkdir myproject
cd myproject/
```

## 创建虚拟环境

```
创建一个独立的Python运行环境，命名为venv：
	virtualenv --no-site-packages venv
	如果报错：virtualenv: error: unrecognized arguments: --no-site-packages
	从版本20开始，默认就是’--no-site-packages‘了
	直接执行 virtualenv venv 就可以在myproject文件夹下生成 venv了，以后的环境均存在这里。
	
	--no-site-packages
    令隔离环境不能访问系统全局的site-packages目录
    --system-site-packages
    令隔离环境可以访问系统全局的site-packages目录

使用python可以查看python版本，使用 which python 可以查看当前python的路径
可以使用 python3，也可以使用 python3.6 只要安装了
nvidia@tegra-ubuntu:~/zll/zllpy3$ which python3
/usr/bin/python3
nvidia@tegra-ubuntu:~/zll/zllpy3$ 

在 /usr/bin/ 下可以看到：
python2.7
python2.7-config

python3
python3-config

python3.5
python3.5-config

python3.6

创建一个独立的 python3.6 虚拟环境:
	virtualenv -p /usr/bin/python3.6 venvp36
	
virtualenv --system-site-packages -p /usr/bin/python3.6 venv36 #依赖于主环境

查看python指向：
ls -l /usr/bin | grep python
rm /usr/bin/python

python3指向python3.6(定义一个软连接)
ln -s /usr/bin/python3.6 /usr/bin/python3
```

## 进入虚拟环境

```
新建的Python环境被放到当前目录下的venv目录。有了llenv这个Python环境，可以用source进入该环境：
source venv/bin/activate
source venvp36/bin/activate
```

## 退出、删除

```
在venv环境下，用pip安装的包都被安装到venv这个环境下，系统Python环境不受任何影响。也就是说，venv环境是专门针对myproject这个应用创建的。
退出当前的venv环境，使用命令：
deactivate 

如果需要删除我们创建的虚拟环境，只需要退出，并删除创建的文件夹即可：
$ deactivate
$ rm -r /path/to/ENV
```



# 原理(环境复制与包迁移)

## pip

> 第三方包的安装路径:  \Python37\Lib\site-packages
>
> **在没有网络的情况下非常适合从一个已经安装包的电脑上拷贝包到另一个没有安装包的电脑上。**
>
> 1. 进入第三方库安装的路径的文件夹。\site-packages。
> 2. 找到需要的包复制即可。注意一个库的包有两个文件，要同时复制。
> 3. 将包移动到另一台电脑上的\site-packages 粘贴即可使用（有很多第三方包是关联一些其它包的，都需要拷贝过去）。

## conda

### conda和pip安装库的区别

> 在Anaconda中，无论在哪个环境下，只要通过conda install xxx的方式安装的库都会放在Anaconda的pkgs目录下，如:E:\python\anaconda\pkgs\numpy-1.18.1-py36h48dd78f_1。这样的好处就是，当在某个环境下已经下载好了某个库，再在另一个环境中还需要这个库时，就可以直接从pkgs目录下将该库复制至新环境（将这个库的Lib\site-packages中的文件复制到当前新环境下Lib中的第三方库中，也即Lib\site-packages中，这个过程相当于通过pip install xxx进行了安装）而不用重复下载。

### conda和pip卸载库的区别

> pip是在特定的环境中进行库的安装，所以卸载库也是一样的道理，通过pip uninstall xxx就可以将该环境下Lib\site-packages中对应的库进行卸载了。
>
> 如果通过conda uninstall xxx删除当前环境下某个库时，删除的只是当前环境下site-packages目录中该库的内容，它的效果和通过pip uninstall xxx是一样的。如果再到另一个环境中通过conda install xxx下载这个库，则还是通过将pkgs目录下的库复制到当前环境。若要清空这个pkgs下的已下载库，可以通过命令conda clean -h进行实现。

# 替换成国内源

> 开源软件国内镜像源对比，参考：https://huaxiaostar.com/2020/07/open-source-china-mirror-list/#more

## pip

```
pypi 清华大学源：https://pypi.tuna.tsinghua.edu.cn/simple
pypi 豆瓣源 ：https://pypi.douban.com/simple/
pypi 腾讯源：https://mirrors.cloud.tencent.com/pypi/simple
pypi 阿里源：https://mirrors.aliyun.com/pypi/simple/

有些还安不上，可以增加：
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/

pip install markdown # 这样会从国外官网下载markdown模块并安装。
pip install markdown -i https://pypi.tuna.tsinghua.edu.cn/simple #替换成清华大学源。
pip install pyinstaller -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## conda

```
Conda 添加源有2种常用方式。以下以清华源为例做说明:
方式一
添加源的方式是执行以下命令：
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
conda config --set show_channel_urls yes

conda info 查看配置详情

conda install --channel https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/ torchvision=0.8.1
conda install --channel https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/ torch


方式二
修改用户目录下的 .condarc 文件如下：

channels:
  - defaults
show_channel_urls: true
channel_alias: https://mirrors.tuna.tsinghua.edu.cn/anaconda
default_channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free

注，Windows 在资源管理器里无法直接创建名为 .condarc 文件，有几种解决方案：
 - PowerShell 里执行 New-Item .condarc 命令来创建
 - 在 VS Code 里新建 .condarc 文件
 - 执行命令 conda config --set show_channel_urls yes 生成

注，上述两种方式里，都只列了比较核心的 main 和 free packages，但一般够用了。如果想添加更多 packages，可以参考清华源-Anaconda帮助页面：https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/
```

