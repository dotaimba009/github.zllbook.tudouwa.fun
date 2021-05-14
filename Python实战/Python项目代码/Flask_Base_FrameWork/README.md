项目源码地址：
https://gitee.com/ll.zhangll/zllbook.tudouwa.fun/tree/master/Python%E5%AE%9E%E6%88%98/Python%E9%A1%B9%E7%9B%AE%E4%BB%A3%E7%A0%81/Flask_Base_FrameWork

Flask_Base_FrameWork是一个基于flask的http后端应用，包含一些基本结构：
1. 统一蓝图使用
2. 请求中间件统一处理、错误处理
   统一结构回复
3. 日志记录
4. 统一配置模块
5. 单元测试
6. 统一邮件处理
7. 配合gunicorn部署的日志
8. 项目环境的管理

## 蓝图
1. Flask可以通过Blueprint来组织URL以及处理请求。
2. Flask使用Blueprint让应用实现模块化。


