#!/bin/bash
# Author: dmatosl <https://github.com/dmatosl>

set -eo pipefail

if [[ "$GRAFANA_IMPORT_DATA" == "true" ]]; then
  # import data
  sleep 5 # mean time to spin up grafana and influxdb
  python import_grafana_data.py
fi

# Infinite loop for collecting metrics
while true ; do
    python collect.py
    sleep $SLEEP
done
