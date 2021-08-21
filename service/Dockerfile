FROM python:3.7-slim-buster

WORKDIR /app

# Copy files, install requirements
COPY requirements.txt .
COPY src ./

RUN pip install -r requirements.txt --no-cache-dir

EXPOSE 80

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=80"]
