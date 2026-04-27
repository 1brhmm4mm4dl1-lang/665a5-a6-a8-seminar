from pymongo import MongoClient

def get_db():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["admin"]
    return db["logs"]


def get_all_logs(collection):
    return list(collection.find())


def get_error_logs(collection):
    return list(collection.find({"status": {"$gte": 400}}))


def get_slow_requests(collection):
    return list(collection.find().sort("response_time", -1).limit(5))


def get_top_ips(collection):
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 5}
    ]
    return list(collection.aggregate(pipeline))


def get_top_endpoints(collection):
    pipeline = [
        {"$group": {"_id": "$endpoint", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}}
    ]
    return list(collection.aggregate(pipeline))


if __name__ == "__main__":
    col = get_db()

    print(get_all_logs(col))
    print(get_error_logs(col))
    print(get_slow_requests(col))
    print(get_top_ips(col))
    print(get_top_endpoints(col))