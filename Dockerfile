FROM python:3.12.2-alpine

WORKDIR /app

COPY . .

RUN ln -sf /dev/stdout /app/notify.log

CMD ["./startup.sh"]
