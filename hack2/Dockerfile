FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential vim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN pip install PyMySQL
EXPOSE 8080
CMD ["python","app.py"]
