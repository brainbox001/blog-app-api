FROM python:3.9-alpine3.13
LABEL maintainer="marcusdev"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./app /app
COPY ./scripts /scripts
COPY ./requirements.txt /tmp/requirements.txt
WORKDIR /app
EXPOSE 8000

RUN python -m venv /py && \
/py/bin/pip install --upgrade pip && \
apk  add --update --no-cache postgresql-client jpeg-dev && \
apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev zlib zlib-dev linux-headers && \
/py/bin/pip install -r /tmp/requirements.txt && \
rm -rf /tmp && \
apk del .tmp-build-deps


RUN mkdir -p /vol/web/static && \
mkdir -p /vol/web/media && \
chmod -R 777 /vol && \
chmod -R +x /scripts

ENV DJANGO_SETTINGS_MODULE=app.settings
ENV PATH="/scripts:/py/bin:$PATH"

CMD ["run.sh"]
