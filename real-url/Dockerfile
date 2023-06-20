# 创建一个容器用于运行main.py的网页服务器
FROM alpine:latest

# 安装python3
RUN apk add --no-cache python3 py3-pip \
    && pip3 install --upgrade pip

# 设置工作目录
WORKDIR /app

# 将当前目录下的文件复制到工作目录下
COPY . /app/

# 安装依赖
RUN pip3 --no-cache-dir install -r requirements.txt

# 对外暴露端口
EXPOSE 80

# 容器启动时执行的命令
CMD ["python3", "main.py"]
