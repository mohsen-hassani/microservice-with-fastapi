FROM python:3.11-slim-bookworm
WORKDIR /app
COPY ./feedback/requirements.txt /app/
RUN pip install -r /app/requirements.txt
COPY ./feedback/src/ /app/src/
WORKDIR /app/src

ENTRYPOINT ["python", "main.py"]