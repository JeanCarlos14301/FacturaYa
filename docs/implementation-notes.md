# Notas de implementación

La versión base conserva los seis objetivos de evaluación positivos. Las pruebas heredadas describen el comportamiento observado y no constituyen una garantía de seguridad. `evaluation/expected-findings.json` contiene la evidencia exacta, fuera del ZIP.

La función de creación de facturas combina validación, cálculo y HTML. La búsqueda usa una consulta concatenada; el acceso JSON no limita el propietario. Los demás accesos y la consulta de correo en `db.py` usan parámetros. La dependencia entre `billing.py` y `customers.py` se resuelve con un import diferido.

El reporte calcula el descuento redondeando cada línea antes de sumar; facturación redondea una vez el descuento del subtotal. Para la factura `FY-00001`, 50.03 + 50.04 = 100.07: facturación muestra 7.51 y el reporte 7.50.

El hash del snapshot se calcula sobre todos los archivos del repositorio, ordenados por ruta relativa POSIX, salvo `.git`, `.venv`, cachés, `evaluation`, `dist`, bases SQLite, ZIP y temporales. Por cada archivo se agrega al SHA-256 global `ruta UTF-8`, byte NUL, hash SHA-256 hexadecimal ASCII del contenido y salto de línea. La variante reservada se guarda fuera del repositorio.
