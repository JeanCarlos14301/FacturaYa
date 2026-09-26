# FacturaYa

A fictitious legacy billing application designed as a reference benchmark for **CodeArchaeologist AI**. Includes reproducible synthetic seed data, characterization test suites, and target contracts for legacy modernization. **This application is deliberately vulnerable and architecturally flawed for local evaluation with synthetic data.**

## Setup and Execution

Python 3.11+ is required. Check your version with `python --version` (or use the full path to your Python interpreter). In PowerShell, run from the repository root:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
.\.venv\Scripts\python.exe samples/facturaya-v1/seed.py samples/facturaya-v1/facturaya.sqlite3
$env:FACTURAYA_DB = (Resolve-Path samples/facturaya-v1/facturaya.sqlite3).Path
.\.venv\Scripts\python.exe -m flask --app samples/facturaya-v1/app.py run --host 127.0.0.1
```

The debugger is disabled by default. To re-seed into an existing database file, pass `--reset`; otherwise, the seed script rejects overwriting the file.

Synthetic demo credentials:
- `ana` / `DemoAna!2024`
- `bruno` / `DemoBruno!2024`
- `carla` / `DemoCarla!2024`

## HTTP Testing Examples

```powershell
curl.exe -c session.txt -d "username=ana&password=DemoAna!2024" http://127.0.0.1:5000/login
curl.exe -b session.txt http://127.0.0.1:5000/invoices/1
curl.exe -b session.txt "http://127.0.0.1:5000/invoices?q=FY-00001"
curl.exe -b session.txt http://127.0.0.1:5000/invoices/1/view
curl.exe -b session.txt "http://127.0.0.1:5000/reports/monthly?month=2024-01"
curl.exe -b session.txt -X POST http://127.0.0.1:5000/logout
```

The `/invoices/new` form allows creating invoices for owned customers with a date, status, and multiple line items. The `/customers` and `/invoices` pages require an authenticated session.

## Testing and Packaging

```powershell
.\.venv\Scripts\python.exe -m pytest -q
.\.venv\Scripts\python.exe scripts/verify_demo.py
.\.venv\Scripts\python.exe scripts/package_sample.py
```

The sample archive is generated at `dist/facturaya-v1.zip`. It contains only the code and resources required to initialize and run the benchmark sample. To run the packaged standalone app, extract the ZIP, install `requirements.txt`, run `seed.py`, and launch with `flask run` from within `facturaya-v1`.

> [!NOTE]
> Tests in `test_known_legacy_behavior.py` characterize known insecure legacy behaviors (such as SQL injection and broken object authorization); their success confirms legacy behavior reproducibility and does not imply security.
