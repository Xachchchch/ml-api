# ML API Project

This is a simple REST API for an image classification model using FastAPI. The project demonstrates **end-to-end ML deployment**, including Docker containerization and CI/CD with GitHub Actions.

## Features

- **Image Classification** using a pre-trained ResNet model.
- **REST API** built with FastAPI to serve predictions.
- **Dockerized** for easy deployment.
- **CI/CD** configured with GitHub Actions for automated testing and building.
- **Unit Tests** included and run in the CI workflow.

## Installation

### Clone the repository

```bash
git clone https://github.com/Xachchchch/ml-api.git
cd ml-api
```

## Create virtual environment (optional but recommended)

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Run locally

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## Run with Docker

```bash
docker build -t ml-api-docker .
docker run -p 8000:8000 ml-api-docker
```



