# timing_send

### 项目说明
    定时发送留言
    固定每天某个时间(比如凌晨1点)，根据advice接口请求数据然后定时发送指定数据到指定邮箱

### 项目需求
    定时发送留言:
    1、调用服务器接口获取数据
    2、根据配置文件中的配置发送数据到指定邮箱
    3、定时发送


### 项目配置
    自己在项目根目录下建一个private包，里面放settings.py和get.py
    settings.py: 写项目相关配置
    get.py: 写接口调用函数


### 运行项目
    安装schedule: pip3 install schedule
    运行项目根目录下的run.py