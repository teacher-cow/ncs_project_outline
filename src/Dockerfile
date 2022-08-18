# Python support can be specified down to the minor or micro version
# (e.g. 3.6 or 3.6.3).
# OS Support also exists for jessie & stretch (slim and full).
# See https://hub.docker.com/r/library/python/ for all supported Python
# tags from Docker Hub.
FROM python:3.7

# If you prefer miniconda:
#FROM continuumio/miniconda3

ENV PYTHONIOENCODING=utf-8

LABEL Name=Text_extract
LABEL author="Liuhong He"

# Build folder
COPY src/ /ailab/src
VOLUME /ailab
WORKDIR /ailab/src

#删除默认apt-get源 使用清华的源
RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak && \
    echo "deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster main contrib non-free" >/etc/apt/sources.list && \
    echo "deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster-updates main contrib non-free" >>/etc/apt/sources.list && \
    echo "deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster-backports main contrib non-free" >>/etc/apt/sources.list && \
    echo "deb https://mirrors.tuna.tsinghua.edu.cn/debian-security buster/updates main contrib non-free" >>/etc/apt/sources.list

RUN apt-get update
RUN apt-get install vim -y
RUN apt install -y supervisor

# Using pip:
COPY requirements.txt ./
RUN pip install --user --upgrade pip
RUN pip install -r requirements.txt

# Setup supervisord
RUN mkdir -p /var/log/supervisor
COPY /src/supervisord.conf /etc/supervisor/conf.d/supervisord.conf


# CMD ["/bin/bash", "start.sh"]
CMD ["/usr/bin/supervisord"]