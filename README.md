# Security Log Analyzer 🛡️

Herramienta en Python que analiza intentos de fuerza bruta en autenticaciones SSH y genera reportes CSV. Detecta IPs sospechosas, usuarios inválidos y eventos repetidos.

## Cómo usarlo

```bash
python3 analyzer.py

Características
Analiza los registros de autenticación SSH.

Detecta intentos de ataque por fuerza bruta basándose en patrones de inicio de sesión fallidos.

Admite múltiples indicadores de ataque:

Intentos fallidos de contraseña

Usuarios no válidos

Intentos de inicio de sesión root

Agrega eventos por dirección IP.

Rastrea las marcas de tiempo de primera y última visualización.

Genera informes CSV.

Configurable mediante archivo JSON.

Admite argumentos de la CLI.

Estructura del proyecto
security-log-analyzer/
├── analyzer.py
├── config.json
├── sample_logs/
│   └── sample_auth.log 
├── output/ 
│   └── report.csv 
├── requirements.txt 
└── README.md
Debug
Ejecución básica a través de la terminal:

python3 analyzer.py
python3 analyzer.py --config config.json --threshold 3


Licencia
MIT License – LICENSE

Este proyecto está diseñado como un proyecto de auditoría de seguridad para empresas y particulares.

          JSGO 2026



<p align="center">
  <a href="https://www.bestpractices.dev/projects/11885">
    <img src="https://bestpractices.dev/projects/11885/badge" alt="OpenSSF Best Practices">
  </a>
</p>



