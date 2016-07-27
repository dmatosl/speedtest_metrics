FROM python:2.7

ENV "INFLUXDB_HOST=influxdb"
ENV "INFLUXDB_PORT=8086"
ENV "INFLUXDB_USER=admin"
ENV "INFLUXDB_PASSWORD=admin"
ENV "INFLUXDB_DATABASE=speedtest_metrics"
ENV "SLEEP=10"

WORKDIR /app

ADD ./ /app
#COPY ./collect.py /app
#COPY ./import_datasource.py /app
#COPY ./requirements.txt /app
#COPY ./run.sh /app

RUN pip install -r requirements.txt

ENTRYPOINT ["/app/run.sh"]
CMD [""]
