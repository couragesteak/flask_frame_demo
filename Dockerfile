#FROM python:3.8-alpine
FROM vitcloud/centos7-python38:2.0

ADD . /usr/local/web
WORKDIR /usr/local/web

# 更新python pip和setuptools
RUN python -m pip install --upgrade pip -i https://pypi.douban.com/simple
RUN pip install --upgrade setuptools -i https://pypi.douban.com/simple

# 安装依赖包
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt -i https://pypi.douban.com/simple

# 腾讯cos
# RUN pip install -U cos-python-sdk-v5
# RUN pip install elasticsearch==7.17.0

CMD ["python", "main.py"]