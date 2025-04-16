import random
import json
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

# Define log levels and components
log_levels = ['INFO', 'DEBUG', 'WARN', 'ERROR', 'CRITICAL']
components = ['AuthService', 'DBService', 'Network', 'Cache', 'APIGateway']
anomaly_phrases = [
    "Segmentation fault",
    "OutOfMemoryError",
    "Connection timed out",
    "Database locked",
    "Permission denied",
    "System overheating"
]

def generate_log_entry(timestamp, is_anomaly=False):
    level = random.choices(log_levels, weights=[50, 20, 15, 10, 5])[0] if not is_anomaly else random.choice(['ERROR', 'CRITICAL'])
    component = random.choice(components)
    
    if is_anomaly:
        message = random.choice(anomaly_phrases)
    else:
        message = fake.sentence(nb_words=6)

    log = {
        "timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S"),
        "level": level,
        "component": component,
        "message": message,
        "label": "anomaly" if is_anomaly else "normal"
    }
    return log

def generate_logs(num_logs=1000, anomaly_rate=0.05, output_file="data/logs.jsonl"):
    base_time = datetime.now()

    with open(output_file, "w") as f:
        for i in range(num_logs):
            timestamp = base_time + timedelta(seconds=i * random.randint(1, 5))
            is_anomaly = random.random() < anomaly_rate
            log_entry = generate_log_entry(timestamp, is_anomaly)
            f.write(json.dumps(log_entry) + "\n")

    print(f"✅ {num_logs} logs generated → {output_file}")

if __name__ == "__main__":
    generate_logs(num_logs=1000, anomaly_rate=0.08)
