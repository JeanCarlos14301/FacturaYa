# Demostración de cinco minutos

1. **Minuto 0–1:** preparar entorno y generar SQLite con los comandos del README. Indicar que todos los datos son ficticios.
2. **Minuto 1–2:** ejecutar `flask run` en `127.0.0.1`; iniciar sesión como `ana`.
3. **Minuto 2–3:** abrir `/customers`, `/invoices`, `/invoices/1/view` y consultar `/invoices/1` con la cookie de sesión. Mostrar `100.07`, `7.51` y `92.56`.
4. **Minuto 3–4:** ejecutar `pytest -q` y `scripts/verify_demo.py`. Explicar que algunas pruebas fijan comportamiento heredado para que la evaluación pueda detectarlo.
5. **Minuto 4–5:** ejecutar `scripts/package_sample.py`, listar el ZIP y entregarlo como entrada a LegacyLens. El ZIP no contiene respuestas de evaluación ni la variante reservada.
