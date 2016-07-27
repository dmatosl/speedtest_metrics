#!/bin/bash
# Author: dmatosl <https://github.com/dmatosl>

set -euf -o pipefail

# import datasource
sleep 5 # time to spin up grafana and influxdb
python import_grafana_data.py

while true ; do

    python collect.py
    sleep $SLEEP

done

