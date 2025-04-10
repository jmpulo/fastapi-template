FROM bitnami/python:3.12.3

RUN pip3 install gunicorn uvloop

WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
COPY ./alembic.ini /code/alembic.ini
COPY ./alembic /code/alembic

RUN pip3 install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app

ENV DB_PATH=placeholder

CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","8000"]