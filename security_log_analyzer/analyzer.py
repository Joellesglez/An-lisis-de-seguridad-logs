import re
import csv
import json
import os
from collections import defaultdict
from datetime import datetime
import argparse


# --------------------------------------------------
# Argument parser
# --------------------------------------------------

parser = argparse.ArgumentParser(
    description="Security Log Analyzer - Detect brute force attempts from logs"
)

parser.add_argument(
    "--config",
    default="config.json",
    help="Path to configuration file (default: config.json)"
)

parser.add_argument(
    "--threshold",
    type=int,
    help="Override failed attempts threshold"
)

args = parser.parse_args()


# --------------------------------------------------
# Load configuration
# --------------------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, args.config), "r") as config_file:
    config = json.load(config_file)


LOG_FILE = os.path.join(BASE_DIR, config["log_file"])
OUTPUT_CSV = os.path.join(BASE_DIR, config["output_file"])
FAILED_THRESHOLD = args.threshold if args.threshold else config["threshold"]


# Ensure output directory exists
os.makedirs(os.path.dirname(OUTPUT_CSV), exist_ok=True)

# --------------------------------------------------
# Data structures
# --------------------------------------------------

failed_attempts = defaultdict(int)
first_seen = {}
last_seen = {}

# --------------------------------------------------
# Log analysis
# --------------------------------------------------

with open(LOG_FILE, "r") as f:
    for line in f:
        if (
    "Failed password" in line
    or "invalid user" in line
    or "Failed password for root" in line
):
            ip_match = re.search(r'from (\d+\.\d+\.\d+\.\d+)', line)
            date_match = re.match(r'(\w+\s+\d+\s+\d+:\d+:\d+)', line)

            if ip_match and date_match:
                ip = ip_match.group(1)

                # Parse log timestamp (assume current year)
                log_time = datetime.strptime(
                    f"{datetime.now().year} {date_match.group(1)}",
                    "%Y %b %d %H:%M:%S"
                )

                failed_attempts[ip] += 1

                if ip not in first_seen:
                    first_seen[ip] = log_time

                last_seen[ip] = log_time

# --------------------------------------------------
# Alert generation
# --------------------------------------------------

alerts = []

for ip, count in failed_attempts.items():
    if count >= FAILED_THRESHOLD:
        alerts.append((ip, count))

# --------------------------------------------------
# Report generation
# --------------------------------------------------

analyzed_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open(OUTPUT_CSV, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([
        "IP",
        "Failed Attempts",
        "First Seen",
        "Last Seen",
        "Analyzed At"
    ])

    for ip, count in alerts:
        writer.writerow([
            ip,
            count,
            first_seen[ip].strftime("%Y-%m-%d %H:%M:%S"),
            last_seen[ip].strftime("%Y-%m-%d %H:%M:%S"),
            analyzed_at
        ])

# --------------------------------------------------
# Salida de Consola 
# --------------------------------------------------

print("Análisis completado Joëlle Samuel González Cbsgrd 2026.")
print(f"Alertas generadas: {len(alerts)}")
