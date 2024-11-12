FROM python:3

WORKDIR /app

COPY requirements.txt /app/

RUN python -m pip install -r requirem \
    ents.txt

COPY fib.py /app/

CMD ["python", "fib.py"]