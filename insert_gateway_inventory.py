import psycopg2, json
from io import StringIO
from csv import reader

def csv_export():
    nones = lambda n: ['null' for _ in range(n)]
    address, owner, location, lastcallenge, lasthash, witnesses, firstblock, lastblock, nonce, name, firsttimestamp, reward, elevation, gain, locationhex, mode, payer = nones(17)
    
    with open('inventory.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        header = next(csv_reader)
        if header != None:
            for row in reader(read_obj):
                db_conn = psycopg2.connect(host="localhost", port="5432", dbname="database_name", user="database_user", password="database_password")
                db_cursor = db_conn.cursor()

                try:
                    address, owner, location, lastcallenge, lasthash, witnesses, firstblock, lastblock, nonce, name, firsttimestamp, reward, elevation, gain, locationhex, mode, payer = row[0].split("|")
                    
                    try:
                        lastcallenge=int(lastcallenge)
                    except:
                        lastcallenge = 'null'
                        pass

                    try:
                        firstblock=int(firstblock)
                    except:
                        firstblock = 'null'
                        pass

                    try:
                        lastblock=int(lastblock)
                    except:
                        lastblock = 'null'
                        pass

                    try:
                        nonce=int(nonce)
                    except:
                        nonce = 'null'
                        pass

                    try:
                        reward=float(reward)
                    except:
                        reward = 'null'
                        pass

                    try:
                        elevation=int(elevation)
                    except:
                        elevation = 'null'
                        pass

                    try:
                        gain=int(gain)
                    except:
                        gain = 'null'
                        pass

                    if not location:
                        location = None

                    addWits = str(f"INSERT INTO gateway_inventory (address, owner, location, last_poc_challenge, last_poc_onion_key_hash, witnesses, first_block, last_block, nonce, name, first_timestamp, reward_scale, elevation, gain, location_hex, mode, payer) VALUES('{address}', '{owner}', '{location}', {lastcallenge}, '{lasthash}', '{witnesses}', {firstblock}, {lastblock}, {nonce}, '{name}', '{firsttimestamp}', {reward}, {elevation}, {gain}, '{locationhex}', '{mode}', '{payer}') ON CONFLICT (address) DO NOTHING")
                    
                    print(addWits)

                    db_cursor.execute(addWits)
                    db_conn.commit()
                except Exception as e:
                    print(e)
                    pass

                db_cursor.close()
                db_conn.close()
csv_export()
