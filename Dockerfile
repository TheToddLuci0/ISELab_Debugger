FROM python:3.7
ENV PYTHONBUFFERED=1

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        sqlite3 apt-get iputils-ping \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir /code
WORKDIR /code
COPY . /code
RUN pip install -r requirements.txt
RUN python manage.py migrate

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]