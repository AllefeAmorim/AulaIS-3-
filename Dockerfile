FROM python:3.9-slim

WORKDIR /app

COPY . /app/

RUN pip install --upgrade pip \
    six==1.16.0 \
    is-wire==1.2.1 \
    protobuf==3.20.3

CMD ["python", "sub.py"]
