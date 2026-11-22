# GreenfieldBotDemo

Prototipo de Migración Greenfield · AI-Q Consultores.

Mini demo estática (una sola página) que explica la arquitectura de un analizador de objetos Z para migraciones greenfield a S/4HANA: recorrido guiado de 8 etapas, arquitectura, cuadrantes y criticidad, explorador de objetos y límites del prototipo.

Todos los datos son ficticios (18 objetos de un ECC 6.0 simulado).

- `index.html`: la demo (se publica con GitHub Pages desde la raíz de `main`).
- `template.html` + `data.json` + `build.py`: fuente; `python3 build.py` regenera `index.html`.
