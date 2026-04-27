import pytest
from pymongo import MongoClient
from analyze import (
    get_all_logs,
    get_error_logs,
    get_slow_requests,
    get_top_ips,
    get_top_endpoints
)

@pytest.fixture
def collection():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["test_db"]
    col = db["logs"]

    col.delete_many({})

    col.insert_many([
        {"ip": "1.1.1.1", "status": 200, "response_time": 100, "endpoint": "/home"},
        {"ip": "2.2.2.2", "status": 500, "response_time": 900, "endpoint": "/login"},
        {"ip": "1.1.1.1", "status": 404, "response_time": 300, "endpoint": "/api"},
        {"ip": "3.3.3.3", "status": 200, "response_time": 50, "endpoint": "/home"},
    ])

    return col


def test_all_logs(collection):
    logs = get_all_logs(collection)
    assert len(logs) == 4


def test_error_logs(collection):
    errors = get_error_logs(collection)
    assert all(e["status"] >= 400 for e in errors)


def test_slow_requests(collection):
    slow = get_slow_requests(collection)
    assert slow[0]["response_time"] >= slow[-1]["response_time"]


def test_top_ips(collection):
    ips = get_top_ips(collection)
    assert ips[0]["_id"] == "1.1.1.1"


def test_top_endpoints(collection):
    endpoints = get_top_endpoints(collection)
    assert endpoints[0]["_id"] == "/home"