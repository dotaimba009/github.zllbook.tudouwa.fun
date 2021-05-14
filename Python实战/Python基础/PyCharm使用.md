## PyCharm 的下载与安装

- 官网下载地址 : <https://www.jetbrains.com/pycharm/download/>，Pycharm 分为商业版（**Professional**）和社区版（**Community**），社区版是免费的。商业版提供更加高级的扩展功能，社区版已经可以胜任大部分的工作。
- PyCharm 是由 JetBrains 开发的一款 Python IDE。支持macOS、Windows、Linux系统。
- 安装过程中注意事项：
  - Update PATH variable(restart needed)
    - Add launchers dir to the PATH（将启动器目录添加到路径中）。
  - Create Associations
    - .py（创建关联，关联.py文件，双击都是以pycharm打开）。

## Python 集成开发环境IDE

> 常见操作都是用pip来进行包的下载、卸载、升级；但其实PyCharm已经把主流的包进行了集成，可在它上面直接操作！

- Pycharm还可以直接上传github，可以使用git，在Pycharm的初始界面，有三个选项：

  ```
  Create New Project
  Open
  Check out from Version Control
  	Git---可直接通过git下载、上传
  	Mercurial
  	Subversion
  ```

- 为避免不同版本python库的影响：

  1. PyCharm可以为每个工程单独建立环境变量，下载制定版本的开源库到单独的环境变量里，和系统环境变量分开。

  2. 可通过 File -- Setting -- Project name -- Project Interpreter 里面的 Project Interpreter 配置不同项目的Python解释器，可增加解释器和使用已存在的解释器，在 Project Interpreter 下面的包列表中，可点击右侧的 + 搜索下载不同的开源包，并自动加到当前工程的环境变量里。成功后，返回到Project左侧项目列表中，可以看到 External Libraries 列表中解释器及其下边的 site-packages中的包变化。

  3. 在配置 Run/Debug Configurations 时，需要 + 新的配置从Templates中，在其右侧列表中，Configuration下，选择 Script path 启动文件及 Python interperter 下选择解释器，并可选择性勾选。

     ```
     Add content roots to PYTHONPATH
     Add source roots to PYTHONPATH
     ```

## 整理 PyCharm 用法

```
Py---Pycharm查看函数定义
(1)ctrl+shift+i 查看函数定义
(2)按住ctrl键，将鼠标放到函数上，就会显示函数信息，点击进去可以查看函数源码。
(3)选中函数位置，按住ctrl＋左键就会跳转到函数的定义处

pycharm快捷键使用技巧
Ctrl+/ 注释选中的代码
Ctrl+鼠标左键 查看源代码
ctrl+alt+l 格式化代码，无需选中，全局格式化，这样也能使pycharm去掉部分在函数下显示的波浪线
Alt+enter 自动导入包


Ctrl+d 复制当前行、或者选择的块
Ctrl+n 跳转到类
Ctrl+shift+n 快速查找文件名
Ctrl+shift+f 全局查找，快速查找关键字的文件
Ctrl+shift+r 全局替换

Ctrl+alt+方向左右键 看源码的时候前进返回
Ctrl+a 全选


Tab 多行同时向后移动
shift+tab 与Tab相反
alt+选中像notepad++多行操作

如果pycharm中写了服务，比如web服务，已经开始运行了，那么在改完python代码后，保存后服务会自动重启，无需停掉服务后再启动。可能跟false启动了调试模式有关，未测试。
通过调用run()方法启动Flask应用程序。但是，当应用程序正在开发中时，应该为代码中的每个更改手动重新启动它。为避免这种不便，请启用调试支持。如果代码更改，服务器将自行重新加载。它还将提供一个有用的调试器来跟踪应用程序中的错误（如果有的话）。
```

