FROM python:3.8

WORKDIR /usr/src/app

COPY files/requirements.txt ./
COPY files/cheapest_path.py ./

RUN pip install --no-cache-dir -r requirements.txt
