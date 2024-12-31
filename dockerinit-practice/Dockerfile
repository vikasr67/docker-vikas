FROM python:3-slim

WORKDIR /apps

COPY . /apps

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python3", "app.py"]



