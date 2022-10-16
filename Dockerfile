FROM --platform=linux/amd64 python:3.10
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN set -ex \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY . /app
CMD ["python", "main.py"]