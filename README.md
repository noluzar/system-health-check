# system-health-check

**Overview**
This Python script monitors the health of a computer system by checking CPU usage, memory usage, disk usage, network connectivity, and system uptime. It logs reports over time and triggers alerts if any system resource exceeds predefined thresholds. This project simulates a SOC-style system monitoring tool, making it ideal for entry-level cybersecurity or IT portfolios.

**Features**
Monitors:
CPU Usage
Memory Usage
Disk Usage
Network Connectivity
System Uptime
Threshold alerts for CPU, memory, and disk usage.
Logs reports to a file (system_health_log.txt).
Optional email notifications for real-time alerts.
Can run continuously in the background for automated monitoring.

**Requirements**
Python 3.x
psutil
 library for system metrics
Optional: SMTP email account if email alerts are enabled
Install required packages:
pip install psutil

**Usage:**
Download the script and save it as system_health_check.py.
Configure optional settings in the script:
CHECK_INTERVAL – how often to check system health (seconds)
CPU_THRESHOLD, MEMORY_THRESHOLD, DISK_THRESHOLD – thresholds for alerts
Email settings (EMAIL_ALERTS, EMAIL_SENDER, EMAIL_RECEIVER, etc.)

**Run the script:**
python system_health_check.py
View the report in the terminal or in the log file system_health_log.txt.

**Example Output**
==================================================
TIMESTAMP: 2025-08-28 11:45:02
SYSTEM HEALTH CHECK REPORT
==================================================
System: Windows 10
Processor: Intel64 Family 6 Model 158
CPU Usage: 12%
Memory Usage: 45% (Available: 6.34 GB)
Disk Usage: 71% (Free: 85.21 GB)
Network: Connected
System Uptime: 3.45 hours
==================================================

**Example alert when thresholds are exceeded:**
CPU Usage: 85% HIGH CPU USAGE!

**Project Skills Demonstrated**
Python scripting and automation
System monitoring and health checks
Logging and reporting
Threshold-based alerts and email notifications
Basic cybersecurity operations simulation

**License**
This project is open-source and free to use for educational purposes.
