# Implementation Notes

The baseline repository preserves six positive evaluation targets and one negative control. Legacy characterization tests describe observed behavior and do not represent a security guarantee. `evaluation/expected-findings.json` specifies the exact ground-truth evidence and is kept outside the distributed input package.

The invoice creation route combines form validation, calculations, database transactions, and inline HTML rendering in a single function. Invoice search uses direct string concatenation into SQL queries; the invoice JSON endpoint does not verify resource ownership (BOLA). Other queries and the customer email lookup in `db.py` use parameterized statements. The cyclical dependency between `billing.py` and `customers.py` is resolved via a deferred inline import.

Reporting and billing compute discounts differently: reporting rounds each line item discount before summing, whereas billing rounds the discount once over the subtotal. For invoice `FY-00001` (50.03 + 50.04 = 100.07), billing displays a discount of 7.51 while reporting computes 7.50.

The repository snapshot hash is calculated over all source files sorted by POSIX relative path, excluding `.git`, `.venv`, caches, `evaluation`, `dist`, SQLite databases, ZIP archives, and temporary files. For each file, the global SHA-256 digest incorporates the UTF-8 relative path, a NUL byte, the ASCII hexadecimal SHA-256 hash of the file content, and a newline character.
