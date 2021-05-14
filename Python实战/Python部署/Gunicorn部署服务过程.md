
### 2. systemctl命令

```
syetemctl 就是service 和 chkconfig这两个命令的整合，在CentOS 7 和 Ubuntu16 就开始被使用
启动服务：systemctl start nginx.service
停止服务：systemctl stop nginx.service
重启服务：systemctl restart nginx.service
查看服务状态：systemctl status nginx.service
设置开机自启动：systemctl enable nginx.service
停止开机自启动：systemctl disable nginx.service
查看所有服务（包括启动失败的，已经启动的，退出运行的）：systemctl list-units --type=service
查看启动的服务：systemctl list-unit-files | grep enabled
查看依赖关系：systemctl list-dependencies nginx.service

更新.server 文件后，需要重置环境 sudo systemctl daemon-reload
```
### 3. 编写 xx.service

> 我们要为目标设置一个配置文件，linux作为一个复杂的系统，开机自启动涉及到的依赖、运行级别、运行环境等等问题肯定需要用户去指定，在启动的时候系统才知道怎么正确地去运行软件。这个配置文件固定以.service作为后缀，比如我们如果要运行/home/downey目录下的test.sh脚本，我们可以添加一个配置文件***test.service***:

将文件放在 `/usr/lib/systemd/system ` 或者 `/etc/systemd/system` 目录下，然后可以测试一下：

```
sudo systemctl start test.service
```

### 7. foodparser.service
```
[Unit]
Description=open gunicorn foodParser service
After=network.target sshd-keygen.service

[Service]
User=xzx
Group=xzx
WorkingDirectory=/home/xzx/Synjones_Robot_Server/Food_Parser/IvaFoodParserService
ExecStart=/home/xzx/miniconda3/bin/gunicorn -k gevent -b 0.0.0.0:5000 main:app

[Install]
WantedBy=graphical.target
```

使用 gevent 模式，需要安装 gevent

```
pip install gevent -i https://pypi.douban.com/simple/
```

# 3. gunicorn配置参数

## 参数详解

1. config `-c --config`  指定一个配置文件

   ```
   gunicorn -c gunicorn.conf manager:app
   ```

2. bind `-b --bind`  默认[‘127.0.0.1:8000’]

   ```
   gunicorn -b 127.0.0.1:8080
   ```

3. daemon 守护进程后台运行 `-D --daemon` 默认false

4. workers 进程数量 `-w --workers`  默认1

   ```
   worker推荐的数量为当前的CPU个数*2 + 1。
   ```

5. worker_class 工作进程类型 `-k  --worker-class`

   ```
   多个工作模式：
   同步Worker：sync 默认模式，也就是一次只处理一个请求
   异步Worker：通过Eventlet、Gevent实现的异步模式
   异步IO Worker：目前支持gthread和gaiohttp两种类型
   ```

   ```
    工作进程类型包括:
        sync(default)
        eventlet
        gevent
        tornado
        gthread
        gaiohttp
   ```

6. worker_connections `--worker-connections` 客户端最大同时连接数 默认 1000

   ```
   使用于gevent和eventlet工作模式
   ```

7. threads `--threads` 线程数 默认 1

   ```
   工作进程中线程的数，建议值2-4 x CPU核心数
   此配置只适用于gthread 进程工作方式， 因为gevent这种使用的是协程工作方式。
   ```

8. max_requests `--max-requests` 工作线程在重新启动之前将处理的最大请求数。 默认0

   ```
   重启之前，worker将处理的最大请求数
   0，默认值时，则禁止了worker的自动重启
   这个方法主要是防止内存泄露
   当超过max_requests时，就会重启worker
   ```

9. max_requests_jitter `--max-requests-jitter` max_requests的最大抖动值 默认 0

   ```
   抖动将导致每个工作的重启被随机化，
   这是为了避免所有工作被重启。randint(0,max-requests-jitter)
   ```

10. timeout `-t --timeout` worker超时时间，超时重启 默认30s

11. graceful_timeout `--graceful-timeout` 接收到restart信号后，worker可以在graceful_timeout时间内，继续处理完当前requests 默认30s

12. keepalive `--keep-alive` 连接上等待请求的秒数，默认情况下值为2。一般设定在1~5秒之间。默认2

13. limit_request_line ` --limit-request-line`   http request line最大字节数。值范围0-8190， 0表示无限制。  默认4094

14. limit_request_fields `--limit-request-fields`  http request中 header字段数的最大值，最大32768  默认100

15. limit_request_field_size `--limit-request-field_size`  http request header字段最大字节数，0时无限制。 默认8190

16. reload `--reload` 当代码有修改时，自动重启workers。适用于开发环境。 默认False

17. reload_extra_files `--reload-extra-file`  扩展reload配置，增加templates，configurations等文件修改监控。

18. backlog `--backlog`  最大挂起的连接数

19. chdir  `--chdir` 切换到指定的工作目录

20. loglevel  `--log-level` 输出error log的颗粒度

    ```
    有效颗粒度:
        debug
        info
        warning
        error
        critical
    ```

21. accesslog  `--access-logfile` 指定access日志文件

22. errorlog  `--error-logfile   --log-file` 指定error日志文件

# 4. 更换Synjones_Robot_Server目录注意事项

## 1. 替换模型

```
/home/xzx/Synjones_Robot_Server/Food_Parser/models 里边存的是 菜品识别算法模型，每个现场都不一样
例： fooddetector_bd_486_20210408.pth
文件后缀必须是 .pth的，	bd表示北大，	486表示训练时是486个类别
```

## 2. 菜品的特征

```
/home/xzx/Synjones_Robot_Server/Food_Parser/FoodFeature 这里边是菜品的特征，特征是根据模型不同，就不同。
```

## 3. 配置

```
/home/xzx/Synjones_Robot_Server/Food_Parser/config/config_detector.yaml
WEIGHT: "fooddetector_bd_486_20210408.pth" # replace model file && modify ROI_BOX_HEAD.NUM_CLASSES
NUM_CLASSES: 486 #545  # model classes
这个名称和类别需要和模型文件对应上
```



