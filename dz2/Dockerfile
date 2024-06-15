FROM python:3.10

RUN apt-get update
RUN apt-get install --yes iputils-ping

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY main.py .

ENTRYPOINT ["python", "main.py"]
