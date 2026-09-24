# Arquitectura observada

```mermaid
flowchart LR
  browser[Navegador / cliente HTTP] --> app[app.py: rutas y HTML/JSON]
  app --> auth[auth.py]
  app --> billing[billing.py]
  app --> customers[customers.py]
  app --> reports[reports.py]
  app --> db[db.py]
  billing --> customers
  customers --> billing
  billing --> db
  reports --> db
  db --> sqlite[(SQLite)]
```

```mermaid
erDiagram
  users ||--o{ customers : owns
  users ||--o{ invoices : owns
  customers ||--o{ invoices : billed
  invoices ||--|{ invoice_items : contains
```

Consulta JSON: `GET /invoices/{id}` → `auth.login_required` → `db.invoice_by_id` → `db.invoice_items` → conversión de importes con `utils.amount` → JSON. El mismo identificador sirve para la vista HTML con sufijo `/view`.

Los importes se almacenan como texto decimal y se convierten con `Decimal`. Cada precio unitario tiene dos decimales; la línea es `cantidad × precio`, redondeada a centavos con `ROUND_HALF_UP`. El subtotal suma líneas. Si alcanza 100.00, el descuento de facturación es `subtotal × 0.075`, redondeado una sola vez a centavos. El total es `subtotal − descuento`.
