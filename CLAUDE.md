# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Commands

```bash
uvicorn main:app --reload   # run dev server (hot reload on :8000)
pytest tests/ -v            # run all tests
pytest tests/test_users.py  # run a single test file
```

## Architecture

This is a minimal FastAPI application. All routes currently live in `main.py`. The `app` instance is the FastAPI application object — new routers should be created with `APIRouter` and included via `app.include_router()` as the project grows.
