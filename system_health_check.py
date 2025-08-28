import psutil
import platform
import socket
import time
from datetime import datetime
import smtplib
from email.message import EmailMessage

# ----- CONFIGURATION -----
LOG_FILE = "system_health_log.txt"
CHECK_INTERVAL = 300  # 5 minutes
CPU_THRESHOLD = 80    # percent
MEMORY_THRESHOLD = 80 # percent
DISK_THRESHOLD = 90   # percent

EMAIL_ALERTS = True
EMAIL_SENDER = "your_email@example.com"
EMAIL_PASSWORD = "your_email_password"
EMAIL_RECEIVER = "admin@example.com"
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587

# ----- ALERT FUNCTIONS -----
def send_email_alert(subject, body):
    if not EMAIL_ALERTS:
        return
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_SENDER
    msg['To'] = EMAIL_RECEIVER

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.send_message(msg)
        print("📧 Email alert sent!")
    except Exception as e:
        print(f"⚠️ Failed to send email: {e}")

# ----- SYSTEM CHECKS -----
def check_cpu():
    usage = psutil.cpu_percent(interval=1)
    alert = ""
    if usage > CPU_THRESHOLD:
        alert = "⚠️ HIGH CPU USAGE!"
        send_email_alert("CPU Alert", f"CPU usage is {usage}%")
    return f"CPU Usage: {usage}% {alert}"

def check_memory():
    memory = psutil.virtual_memory()
    alert = ""
    if memory.percent > MEMORY_THRESHOLD:
        alert = "⚠️ HIGH MEMORY USAGE!"
        send_email_alert("Memory Alert", f"Memory usage is {memory.percent}%")
    return f"Memory Usage: {memory.percent}% (Available: {round(memory.available/1024**3,2)} GB) {alert}"

def check_disk():
    disk = psutil.disk_usage('/')
    alert = ""
    if disk.percent > DISK_THRESHOLD:
        alert = "⚠️ HIGH DISK USAGE!"
        send_email_alert("Disk Alert", f"Disk usage is {disk.percent}%")
    return f"Disk Usage: {disk.percent}% (Free: {round(disk.free/1024**3,2)} GB) {alert}"

def check_network(host="8.8.8.8", port=53, timeout=3):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return "Network: Connected"
    except socket.error:
        alert = "⚠️ NETWORK DISCONNECTED!"
        send_email_alert("Network Alert", "Unable to reach the network!")
        return alert

def check_uptime():
    boot_time = psutil.boot_time()
    uptime_seconds = time.time() - boot_time
    uptime_hours = round(uptime_seconds / 3600, 2)
    return f"System Uptime: {uptime_hours} hours"

# ----- HEALTH REPORT -----
def system_health_report():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report = [
        "="*50,
        f"TIMESTAMP: {timestamp}",
        "SYSTEM HEALTH CHECK REPORT",
        "="*50,
        f"System: {platform.system()} {platform.release()}",
        f"Processor: {platform.processor()}",
        check_cpu(),
        check_memory(),
        check_disk(),
        check_network(),
        check_uptime(),
        "="*50,
        "\n"
    ]
    return "\n".join(report)

# ----- MAIN LOOP -----
def log_health_report():
    while True:
        report = system_health_report()
        print(report)
        with open(LOG_FILE, "a") as file:
            file.write(report)
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    log_health_report()
