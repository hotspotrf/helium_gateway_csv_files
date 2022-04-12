# Helium Gateway CSV Files

This repository provides daily Helium gateway CSV files along with python scripts used to insert these CSV files into a postgresql database used by [Helium Blockchain ETL](https://github.com/helium/blockchain-etl "Helium Blockchain ETL").

## Dependencies

These python scripts rely on `psycopg2` that can be installed using `pip3 install psycopg2`.

## Useage

You'll want to insert gateways first `insert_gateway_inventory.py` and then update their status `insert_gateway_status.py`, as it will not allow an update of status unless the gateway exists in the inventory.

## CSV Files

You can download the CSV files here: [Helium CSV Files]( "Helium CSV Files")
