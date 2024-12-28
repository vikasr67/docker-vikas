FROM ubuntu

WORKDIR /vik

COPY game.py /vik

RUN apt update && apt install -y python3 python3-pip

CMD ["python3","game.py"]
