# Five-Minute Demonstration Runbook

1. **Minute 0–1:** Prepare the virtual environment and initialize the SQLite database using the commands in the README. Clarify that all seeded data is synthetic.
2. **Minute 1–2:** Launch the application with `flask run` on `127.0.0.1`; log in using synthetic credentials for user `ana`.
3. **Minute 2–3:** Navigate to `/customers`, `/invoices`, `/invoices/1/view`, and query `/invoices/1` using the session cookie. Point out values `100.07` (subtotal), `7.51` (discount), and `92.56` (total).
4. **Minute 3–4:** Execute `pytest -q` and `python scripts/verify_demo.py`. Explain that characterization tests anchor intentional legacy behaviors so automated auditors can detect them.
5. **Minute 4–5:** Run `python scripts/package_sample.py`, inspect the generated archive in `dist/`, and submit it as input to CodeArchaeologist. The ZIP archive contains clean sample source code without evaluation manifests.
