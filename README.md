# M3 – PyTorch Image Classification API

A REST API for classifying images into 10 categories using a CNN model
trained on CIFAR-10, served via FastAPI inside a Docker container.

## Team
- Salah Ud Din
- Tarik Mulisic

## Tech Stack
- Python 3.11
- PyTorch / ONNX Runtime
- FastAPI & Uvicorn
- Docker & uv

## How to run

**Build and start the container:**
```bash
docker build -t m3-pytorch-api .
docker run -p 8000:8000 m3-pytorch-api
```

## API Endpoints
- `GET /` - Welcome message
- `POST /predict` - Returns predicted class label

## Pull Requests
- [PR #1 - Add README](https://github.com/Salah-Ud-Din01/M3-pytorch-api/pull/1)
- [PR #2 - Update main.py](https://github.com/Salah-Ud-Din01/M3-pytorch-api/pull/2)

## Made By
SlaahudDin & Tarik Mulisic