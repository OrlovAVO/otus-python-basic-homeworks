# Команда для запуска контейнера docker run -p 8000:8000 -it app

FROM python:3.10-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install --upgrade poetry=="1.7.1"
RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./

RUN poetry lock --no-update

RUN poetry install --no-root

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]



