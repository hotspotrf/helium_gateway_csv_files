import psycopg2, json
from io import StringIO
from csv import reader

def csv_export():
    nones = lambda n: [None for _ in range(n)]
    
    with open('status.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        header = next(csv_reader)
        if header != None:
            for row in csv_reader:
                db_conn = psycopg2.connect(host="localhost", port="5432", dbname="database_name", user="database_username", password="database_password")
                db_cursor = db_conn.cursor()

                try:
                    addy, online, block, updated, poc, last, peer = row[0].split('|')[:-1]

                    listen = str(row).split('|')[-1].replace('"','').replace(']','').replace('[','').replace('\'','')
                    listen = ''.join(listen.split())
                    
                    try:
                        listen = listen.split(',')
                    except:
                        pass

                    listen = str(listen).replace("'", '"')

                    print(addy, online, block, updated, poc, last, peer)

                    block = int(block)
                    last=int(last)
                    poc=int(poc)

                    addWits = str(f"INSERT INTO gateway_status (address, online, block, updated_at, poc_interval, last_challenge, peer_timestamp, listen_addrs) VALUES('{addy}', '{online}', {block}, '{updated}', {poc}, {last}, '{peer}', '{listen}') ON CONFLICT (address) DO NOTHING")

                    db_cursor.execute(addWits)
                    db_conn.commit()
                except Exception as e:
                    print(e)
                    pass
                
                db_cursor.close()
                db_conn.close()
                
csv_export()
