FROM python:3.12.2-alpine

# Install git
RUN apk update --no-cache \
    && apk upgrade --no-cache \
    && apk add git

WORKDIR /app

# Clone the repository with a cache-busting argument
ARG CACHEBUST
RUN git clone --branch main --single-branch --depth 1 https://github.com/greywidget/docker-log.git .

RUN ln -sf /dev/stdout /app/notify.log

CMD ["python", "play.py"]
