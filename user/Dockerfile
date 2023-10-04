FROM python:3.11-slim-bookworm
WORKDIR /app
COPY ./user/requirements.txt /app/
RUN pip install -r /app/requirements.txt
COPY ./user/src/ /app/

ENTRYPOINT ["python", "main.py"]