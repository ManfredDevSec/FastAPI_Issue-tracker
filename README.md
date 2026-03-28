# FastAPI Issue Tracker

A lightweight REST API for tracking issues, built with **FastAPI** and backed by a local JSON file for persistence.

## Features

- Create, read, update, and delete (CRUD) issues
- Issue priority levels: `low`, `medium`, `high`
- Issue status workflow: `open` → `in_progress` → `closed`
- Request timing via `X-Process-Time` response header
- CORS support (all origins allowed by default)
- Auto-generated interactive API docs at `/docs`

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Framework | [FastAPI](https://fastapi.tiangolo.com/) |
| Data validation | [Pydantic v2](https://docs.pydantic.dev/) |
| Server | [Uvicorn](https://www.uvicorn.org/) |
| Persistence | JSON file (`data/issues.json`) |

## Project Structure

```
.
├── main.py               # Application entry point
├── requirements.txt      # Python dependencies
├── data/
│   └── issues.json       # Persistent data store
└── app/
    ├── schemas.py        # Pydantic models & enums
    ├── storage.py        # JSON read/write helpers
    ├── middleware/
    │   └── timer.py      # Request timing middleware
    └── routes/
        └── issues.py     # Issue CRUD endpoints
```

## Installation

### Prerequisites

- Python 3.10+

### Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/ManfredDevSec/FastAPI_Issue-tracker.git
   cd FastAPI_Issue-tracker
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux / macOS
   venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## Running the Server

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

| URL | Description |
|-----|-------------|
| `http://127.0.0.1:8000/docs` | Swagger UI (interactive docs) |
| `http://127.0.0.1:8000/redoc` | ReDoc documentation |

## API Endpoints

All endpoints are prefixed with `/api/v1/issues`.

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/api/v1/issues/` | List all issues |
| `POST` | `/api/v1/issues/` | Create a new issue |
| `GET` | `/api/v1/issues/{issue_id}` | Get a single issue by ID |
| `PUT` | `/api/v1/issues/{issue_id}` | Update an issue by ID |
| `DELETE` | `/api/v1/issues/{issue_id}` | Delete an issue by ID |

### Create an Issue — `POST /api/v1/issues/`

**Request body**

```json
{
  "title": "Button not responding",
  "description": "The submit button does nothing on the login page.",
  "priority": "high"
}
```

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| `title` | `string` | ✅ | 3–100 characters |
| `description` | `string` | ✅ | 5–1000 characters |
| `priority` | `string` | ❌ | `low` \| `medium` (default) \| `high` |

**Response `201 Created`**

```json
{
  "id": "2274ade3-553b-43d2-a9e2-d556d586e401",
  "title": "Button not responding",
  "description": "The submit button does nothing on the login page.",
  "priority": "high",
  "status": "open"
}
```

### Update an Issue — `PUT /api/v1/issues/{issue_id}`

**Request body** (all fields optional)

```json
{
  "title": "Login button not responding",
  "status": "in_progress"
}
```

| Field | Type | Constraints |
|-------|------|-------------|
| `title` | `string` | max 100 characters (no minimum) |
| `description` | `string` | max 1000 characters (no minimum) |
| `priority` | `string` | `low` \| `medium` \| `high` |
| `status` | `string` | `open` \| `in_progress` \| `closed` |

> **Note:** Unlike the create endpoint, the update endpoint does not enforce minimum length constraints on `title` or `description`.

## Data Models

### IssueStatus

| Value | Description |
|-------|-------------|
| `open` | Newly created issue (default) |
| `in_progress` | Issue is being worked on |
| `closed` | Issue has been resolved |

### IssuePriority

| Value | Description |
|-------|-------------|
| `low` | Low priority |
| `medium` | Medium priority (default) |
| `high` | High priority |

## License

This project is open source. Feel free to use and modify it.
