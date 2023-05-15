FROM python:3.11.3-slim

RUN pip install --upgrade pip virtualenv

COPY . /app
WORKDIR /app

ENV VIRTUAL_ENV=/opt/venv
RUN virtualenv -p python3.11 $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install gunicorn -r requirements.txt

RUN ["chmod", "+x", "docker-entrypoint.sh"]
ENTRYPOINT ["./docker-entrypoint.sh"]