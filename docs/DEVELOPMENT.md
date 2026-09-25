# Development guide

## Local workflow

```bash
source venv/bin/activate
pip install -r requirements.txt
python -m compileall app
python -m pytest
uvicorn app.server:app --reload
```

## Adding documents

Place supported source documents under `data/`, then run the ingestion flow described in the root README. Do not commit private, proprietary, or generated documents.

## Before opening a pull request

- Run the test suite.
- Run `python -m compileall app`.
- Confirm no credentials or private documents are included.
- Update the README when an endpoint, model, data path, or dependency changes.
- Keep experimental code isolated from the production API path.

## Naming cleanup

Several existing filenames contain historical typos (`retreiver`, `retreive`, `embded`, and `rag_implmentation`). Rename them only in a dedicated change after updating every import and script reference.
