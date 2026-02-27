FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .

RUN useradd --create-home --shell /bin/bash  flaskuser

RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app
COPY tests ./tests

RUN chown -R flaskuser:flaskuser /app

USER flaskuser

EXPOSE 8080

CMD ["python", "app/gj.py"]
