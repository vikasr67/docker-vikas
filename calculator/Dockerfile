FROM ubuntu

WORKDIR /app

COPY calculator.py /app

RUN apt update && apt install python3 -y python3-pip

ENTRYPOINT ["python3"]

CMD ["calculator.py"]
