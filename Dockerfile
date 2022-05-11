FROM python:3.8

ENV PYTHONUNBUFFERED=1

RUN mkdir usr/src/task_3
WORKDIR usr/src/task_3

COPY requirements.txt .
RUN pip3 install --upgrade pip && pip3 install -r requirements.txt

COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

COPY . .
