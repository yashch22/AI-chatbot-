FROM python:3.8.4

RUN mkdir -p /opt/chatbot
WORKDIR /opt/chatbot
COPY . /opt/chatbot/


RUN pip install -r requirements.txt


CMD ["python3", "app.py"]
