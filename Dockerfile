FROM python:3.8-slim-buster
WORKDIR /Yatusha
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "Server/Server.py"]
