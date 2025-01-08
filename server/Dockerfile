FROM python:3.12.2-slim

COPY . /server/

WORKDIR /server/

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8080"]