
FROM python:3.9.13
WORKDIR /code

COPY ./requirements.txt .
RUN mkdir -p test_audio_files/temp
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y libsndfile1-dev

COPY ./app .
EXPOSE 8000

CMD ["fastapi", "run", "main.py", "--port", "8000"]

