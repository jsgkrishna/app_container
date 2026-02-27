# Content

This is a HTTP API built with Flask that fetches publicly available gists for a given GitHub user.

The API interacts with the GitHub REST API and returns structured JSON data.

## How it works ?

- Fetch public gists for any GitHub user
- Proper error handling (404, API failures)
- Automated unit tests using pytest
- Containerized using Docker
- Runs on port 8080

---

## Project Structure

.
├── app/
│   ├── __init__.py
│   └── gj.py
├── tests/
│   └── test_api.py
├── Dockerfile
├── requirements.txt
└── README.md

---

## Requirements

- Python 3.10+
- Docker (optional, recommended)

---

# Running Locally (Without Docker)

## 1. Create virtual environment

python -m venv venv
source venv/bin/activate -->  Linux
venv\Scripts\activate    -->  Windows

## 2. Install dependencies

pip install -r requirements.txt

## 3. Run the API

python app/gj.py

The API will start on:
http://localhost:8080

---

# Running with Docker

## Build Image

docker build -t flask-gists-api .

## Run Container

docker run -p 8080:8080 flask-gists-api

The API will be available at:
http://localhost:8080

---

# API Usage

## Endpoint

GET /<username>

## Example

curl http://localhost:8080/octocat

## Example Response


{
  "gists": [
        {
      "description": null,
      "id": "1162032",
      "url": "https://gist.github.com/octocat/1162032"
    }
  ],
  "user": "octocat"
}

---

# Running Tests

pytest -v

Tests mock the GitHub API to avoid external dependency during execution.
Note: Recommended to run with "-s" --> "pytest -s tests/test_api.py" to see full output.


---EOF---

