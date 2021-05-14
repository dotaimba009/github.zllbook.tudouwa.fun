## Python下载与安装

> ：一般都是直接安装Anaconda，不需要直接安装Python
>
> 不是安装越新的版本越好，需要考虑到一些其他的环境，比如，如果使用 python打包工具pyinstaller，而pyinstaller更新不如python版本快，pyinstaller还依赖python的版本等。

- 打开浏览器访问 <https://www.python.org/> 找到对应版本安装并下载，记得勾选加入环境变量，Add Python 3.8 to PATH
- ```
  executable installer 表示可执行版，需要安装后使用
  embeddable zip file 表示嵌入版，就是解压以后就可以使用的版本
  ```

- 安装好后，python提供了 IDLE 工具、Python Module Docs、Python Manuals 编辑器、模块doc以及开发手册。

## Anaconda 介绍

- https://www.anaconda.com/products/individual 下载与安装Anaconda

- Python 的强大之处在于它的应用领域范围广，涉及人工智能、科学计算、Web开发、系统运维、大数据、云计算、金融、游戏开发等。实现其强大功能的前提，是Python具有数量庞大且功能相对完善的标准库和第三方库。通过对库的引用，能够实现对不同领域业务的开发。然而，正是由于库的数量庞大，对于管理这些库以及，对这些库的及时维护成为既重要，但又很复杂度的事情。
- Anaconda 可以便捷获取包，且对包能够进行管理，对环境也可以统一管理。Anaconda包含了conda、Python 在内的超过180个科学包及其依赖项。
- Anaconda：开源、高性能使用Python和R语言、免费的社区支持；其特点的实现主要基于Anaconda拥有的：conda包、环境管理器、1000+开源库。
- **Anaconda、conda、pip：**
  - **Anaconda：** Anaconda是一个包含180+的科学库及其依赖项的发行版本。其包含的科学包包括：*conda，numpy，scipy、ipyhon notebook* 等。可以在Windwos、macOS、Linux。
  - **conda：** conda是包及其依赖项和环境的管理工具。
    - 适用语言：Python、R、Ruby、Lua、Scale、Jave、JaveScript、C/C++，FORTRAN。
    - 适用平台：Windows，macOS，Linux。
    - 用途：
      - 快速安装、运行和升级包及其依赖项。
      - 在计算机中便捷地创建、保存、加载和切换环境。（如果你需要的包要求不同版本的Python，你无需切换到不同环境，因为conda同样是一个环境管理器。仅需要几条命令，你可以创建一个完全独立的环境来运行不同的Python版本，同时继续在你常规的环境中使用你常用的Python版本。）
      - conda为Python项目而创造，但可适用于上述的多种语言。
      - conda包和环境管理器包含于Anaconda的所有版本当中。
  - **pip**：pip是用于安装和管理软件包的包管理器。
    - pip编写语言是Python，Python2.7.9及后续版本，默认安装命名为pip；Python3.4及后续版本，默认安装，命名为pip3。

## Anaconda 安装（Windows）

- 目标路径中**不能**含有**空格**，同时不能是**“unicode”**编码。
- 除非被要求以管理员权限安装，否则不要以管理员身份安装。
- 在“Advanced Installation Options”中**不要**勾选“Add Anaconda to my PATH environment variable.”（“添加Anaconda至我的环境变量。”）。因为如果勾选，则将会影响其他程序的使用。如果使用Anaconda，则通过打开Anaconda Navigator或者在开始菜单中的“Anaconda Prompt”（类似macOS中的“终端”）中进行使用。除非你打算使用多个版本的Anaconda或者多个版本的Python，否则便勾选“Register Anaconda as my default Python 3.x”。
- 如果你不想了解“Anaconda云”和“Anaconda支持”，则可以**不勾选**“Learn more about Anaconda Cloud”和“Learn more about Anaconda Support”。
- **验证安装结果：**
  - 开始 → Anaconda3（64-bit）→ Anaconda Navigator”，若可以成功启动Anaconda Navigator则说明安装成功。
  - “开始 → Anaconda3（64-bit）→ 右键点击Anaconda Prompt → 以管理员身份运行”，在Anaconda Prompt中输入 ***conda list\*** ，可以查看已经安装的包名和版本号。若结果可以正常显示，则说明安装成功。

## Anaconda navigator

Anaconda导航器是一个包含在Anaconda发行版中的桌面图形用户界面，允许您启动应用程序，轻松管理conda包、环境和通道，而无需使用命令行命令。导航器可以搜索Anaconda云或本地Anaconda存储库中的包。适用于Windows、macOS和Linux。

## Jupyter notebook

我们可以从Anaconda navigator的Home打开Jupyter notebook，Jupyter notebook其实是打开一个网页，但很像是文件管理器，你可以在这里创建自己的文件，并编写代码、调试和运行。

## 配合pythonIDE PyCharm使用

> 详见另一篇文章 <Python包和模块的管理>