## Security Log Analyzer ## 

Herramienta creada con Python para analizar las vulnerabilidades que se generan en las autenticaciones SSH a través fuerza bruta.#

Detecta las autenticaciones a través de ficheros.

Detecta Ips con varios logis repetidos.

Genera directamente un archivo CSV con los reportes.

HTR en Terminal asociado:

python analyzer.py

Analizador de Registros de Seguridad

Este Analizador de Registros de Seguridad es una herramienta de seguridad básica defensiva basada en Python que analiza los registros de autenticación para detectar posibles ataques de fuerza bruta.

Este proyecto está diseñado como un proyecto de auditoría de seguridad para empresas y particulares.

# Características #

Analiza los registros de autenticación SSH.
Detecta intentos de ataque a través defuerza bruta basándose en patrones de inicio de sesión fallidos
Admite múltiples indicadores de ataque: -Intentos fallidos de contraseña Usuarios no válidos Intentos de inicio de sesión root
Agrega eventos por dirección IP
Rastrea las marcas de tiempo de primera y última visualización
Genera informes CSV
Configurable mediante archivo JSON
Admite argumentos de la CLI
Estructura del proyecto

security-log-analyzer/
├── analyzer.py
├── config.json
├── sample_logs/
│ └── sample_auth.log 
├── output/ 
│ └── report.csv 
├── requirements.txt 
└── README.md

# Debug #

Ejecución báisca a través de la terminal:

python3 analyzer.py

python3 analyzer.py --config config.json --threshold 3

## Análisis de seguridad a través de logs con fuerza bruta JSGO 2026 
