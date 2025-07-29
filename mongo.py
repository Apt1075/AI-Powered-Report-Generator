from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["ai-power-shipment-report"]
collection = db["shipment-details"]

def get_report(query: dict):
    return list(collection.find(query, {"_id": 0}))  # exclude _id
