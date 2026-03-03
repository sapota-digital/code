# code

A Python/FastAPI project.

## Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
uvicorn main:app --reload
```

## API

- `GET /` — Hello world
- `GET /health` — Health check
