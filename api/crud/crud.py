import pymongo
from pymongo import MongoClient

def get_client():
    # Connect to MongoDB
    client = MongoClient('mongodb://mongodb:27017/')
    return client

def get_nfts(database: str, limit):
    # Connect
    client = get_client()

    # Link with the database
    database = client[database]

    # Link with the collection
    collection = database['nfts']

    # Get NFTs
    nfts = [ _ for _ in collection.find({}).sort("date", pymongo.DESCENDING).limit(limit)]

    return nfts

def get_nft(database: str, id: str):
    # Connect
    client = get_client()

    # Link with the database
    database = client[database]

    # Link with the collection
    collection = database['nfts']

    # Get NFTs
    nft = collection.find_one({'_id':id})

    return nft

def insert_nft(database: str, nft):
    # Connect
    client = get_client()

    # Link with the database
    database = client[database]

    # Link with the collection
    collection = database['nfts']
 
    # Add or update the NFT in database
    _filter = {"contract_address":nft["contract_address"], "token_id":nft["token_id"]}
    if collection.find_one(_filter) is not None:
        del nft["_id"]
    collection.update_one(_filter, {"$set":nft}, upsert=True)
    
    return True

def get_cryptos(database: str, limit):
    # Connect
    client = get_client()

    # Link with the database
    database = client[database]

    # Link with the collection
    collection = database['cryptos']

    # Get NFTs
    cryptos = [ _ for _ in collection.find({}).limit(limit)]

    return cryptos

def get_crypto(database: str, ticker: str):
    # Connect
    client = get_client()

    # Link with the database
    database = client[database]

    # Link with the collection
    collection = database['cryptos']

    # Get NFTs
    crypto = [_ for _  in collection.find({'acronym':ticker}).sort("date", -1).limit(1)]

    if len(crypto) > 0:
        return crypto[0]
    else:
        return {}

def insert_crypto(database: str, crypto):
    # Connect
    client = get_client()

    # Link with the database
    database = client[database]

    # Link with the collection
    collection = database['cryptos']
    
    # Add or update the crypto in database
    _filter = {"acronym":crypto["acronym"], "name":crypto["name"]}
    if collection.find_one(_filter) is not None:
        del crypto["_id"]
    collection.update_one(_filter, {"$set":crypto}, upsert=True)
    
    return True
