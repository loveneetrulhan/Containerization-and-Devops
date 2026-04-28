FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install flask --default-timeout=100

EXPOSE 80

CMD ["python", "app.py"]
