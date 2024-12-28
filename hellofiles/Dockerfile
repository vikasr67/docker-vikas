FROM ubuntu 

WORKDIR /app

COPY hello.py /app

RUN apt update && apt install -y python3 python3-pip

ENTRYPOINT ["python3"]

CMD ["hello.py"]
