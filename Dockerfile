FROM python:3.10.0

ENV WORKDIR="/opt/apps/interview_task"
WORKDIR /opt/apps/interview_task
ENV PYTHONPATH="${PYTHONPATH}:${WORKDIR}"
RUN env
RUN apt update \
    && apt -y install build-essential python3-dev swig wkhtmltopdf xvfb vim cron

RUN pip install --upgrade pip && pip install pipenv python-subunit junitxml

COPY ./Pipfile* ./

RUN pipenv install --system --deploy

# Custom cache invalidation
ARG CACHEBUST=1

COPY . ./

CMD scrapy crawl tiktok_shop_spider -L INFO
