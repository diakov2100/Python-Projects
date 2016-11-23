import pymongo

client = pymongo.MongoClient("mongodb://max:123456@46.101.136.126/HackJunction_db")
db = client.HackJunction_db

def fillDB(fulldata):   
    collection= db["spotify_db"]
    for track in fulldata:
        collection.insert(track)
