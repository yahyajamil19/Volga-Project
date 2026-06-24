FROM python:3.11

WORKDIR /app

COPY . .

RUN apt-get update

RUN apt-get install ffmpeg -y

RUN pip install -r requirements.txt

CMD ["uvicorn","app:app","--host","0.0.0.0","--port","8000"]
