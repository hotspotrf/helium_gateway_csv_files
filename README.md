# Helium Gateway CSV Files

This repository provides daily Helium gateway CSV files along with python scripts used to insert these CSV files into a postgresql database used by [Helium Blockchain ETL](https://github.com/helium/blockchain-etl "Helium Blockchain ETL").

## Terms of Service

This repository is provided under HotspotRF's terms of service: [https://hotspotrf.com/hotspotrf-terms-of-use/](https://hotspotrf.com/hotspotrf-terms-of-use/)

## Dependencies

These python scripts rely on `psycopg2` that can be installed using `pip3 install psycopg2`.

## Useage

You'll want to insert gateways first `insert_gateway_inventory.py` and then update their status `insert_gateway_status.py`, as it will not allow an update of status unless the gateway exists in the inventory.

`insert_blocks.py` is not meant to be ran, it is meant to replenish missing blocks and/or if you know what you're doing - spin up a janky ETL without snapshots.

## CSV Files

You can download the CSV files here: [Helium CSV Files](https://storage.googleapis.com/hotspotrf_csv_files/2022-04-15-04-52-21_files.zip "Helium CSV Files")
