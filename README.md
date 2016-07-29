# speedtest_metrics

This project uses speedtest metrics (by Ookla - http://www.speedtest.net ) to store data in InfluxDB and plot into Grafana Dashboard to allow any user to monitor their ISP broadband connection link.

## Build

Using docker-compose

    $ docker-compose build 

## Run

    $ docker-compose up

Under the hood it will spin up influxdb, grafana official containers and speedtest-metrics app container, import influxdb datasource and the dashboard to grafana and start collecting metrics and record into InfluxDB. It will collect metrics respecting $SLEEP (environment variable).



## Contribute
    Fork, Edit, Test, submit you MR
