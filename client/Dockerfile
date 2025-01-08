FROM python:3.12.2-slim

COPY . /client/

WORKDIR /client/

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["streamlit", "run", "ui.py", "--server.address", "0.0.0.0", "--server.port", "8000"]