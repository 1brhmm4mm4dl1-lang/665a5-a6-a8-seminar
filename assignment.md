# MongoDB Log Analyzer CI/CD Pipeline

# Project Overview

This project is a Python-based MongoDB log analysis system that demonstrates CI/CD principles using GitHub Actions.

The system processes logs from MongoDB, analyzes them, and generates reports.


# CI (Continuous Integration)

Triggered on: `pull_request`

# Steps:
- Checkout repository
- Setup Python environment
- Install dependencies (pymongo, pytest)
- Start MongoDB service
- Insert test data
- Run unit tests
- Generate analysis report
- Upload artifact (report.txt)

# CD (Continuous Deployment)

Triggered on: `push to main branch`

# Steps:
- Checkout code
- Run analyzer script
- Create release folder
- Simulate deployment process
- Upload release artifact



# Testing

Pytest is used to validate:
- Log retrieval functions
- Error log filtering
- Slow request detection
- Top IP analysis
- Endpoint statistics



# Technologies Used

- Python
- MongoDB
- PyMongo
- PyTest
- GitHub Actions



# Goal

The goal of this project is to simulate a real-world CI/CD pipeline for a log analysis system.