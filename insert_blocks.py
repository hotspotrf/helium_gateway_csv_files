import psycopg2, json
from io import StringIO
from csv import reader
from csv import DictReader

def csv_export(froto = None):
    nones = lambda n: [None for _ in range(n)]

    with open('blocks.csv', 'r') as read_obj:
        for i, v in enumerate(list(DictReader(read_obj))):
            if(froto and i >= int(froto)):
                break

            db_conn = psycopg2.connect(host="localhost", port="5432", dbname="database_name", user="database_user", password="database_password")
            db_cursor = db_conn.cursor()

            try:
                line = next(iter(v.values()))

                height, time, timestamp, prevhash, blockhash, transactioncount, hbbftround, electionepoch, epochstart, rescuesignature, snapshothash, createdat = line.split('|')

                height=int(height)
                time=int(time)
                transactioncount=int(transactioncount)
                hbbftround=int(hbbftround)
                electionepoch=int(electionepoch)
                epochstart=int(epochstart)

                addWits = str(f"INSERT INTO blocks (height, time, timestamp, prev_hash, block_hash, transaction_count, hbbft_round, election_epoch, epoch_start, rescue_signature, snapshot_hash, created_at) VALUES({height}, {time}, '{timestamp}', '{prevhash}', '{blockhash}', {transactioncount}, {hbbftround}, {electionepoch}, {epochstart}, '{rescuesignature}', '{snapshothash}', '{createdat}') ON CONFLICT (height) DO NOTHING")

                db_cursor.execute(addWits)
                db_conn.commit()

                # print(f'[{i}]', height, time, timestamp, prevhash, blockhash, transactioncount, hbbftround, electionepoch, epochstart, rescuesignature, snapshothash, createdat)
            except Exception as e:
                print(e)
                pass

            db_cursor.close()
            db_conn.close()

############ WARNING/ ############
###
### Be sure you change the 130 to what your (follower/etl/ledger)'s height is at or 5 blocks more
### If you fail to do this, you will get a 'no match of right hand value' error and completely ruin your ETL
### Perhaps you do ruin your ETL, just empty the database - TRUNCATE TABLE blocks; - and re-run this script to the (follower/etl/ledger)'s height
###
############ /WARNING ############

csv_export(130) # change this
