# Assessment-Problem2

## SYSTEM HEALTH MONITORING SCRIPT

## Overview
This script monitors the health of a Linux or Windows system by checking CPU usage, memory usage, disk space, and listing the top running processes. It alerts the user if any metrics exceed predefined thresholds.

## Features
- Monitors CPU usage and reports if it exceeds a specified threshold.
- Monitors memory usage and alerts when it exceeds a specified threshold (e.g., 80%).
- Checks disk usage and reports on its status.
- Lists the top 5 running processes along with their CPU usage.

## Requirements
- Python 3.x
- `psutil` library (install using `pip install psutil`)

## Output Example
Starting system health check...
CPU usage is normal: 6.4%
ALERT: High Memory usage detected: 82.7%
Disk usage is normal: 68.8%
Top 5 Running Processes:
{'pid': 0, 'cpu_percent': 0.0, 'name': 'System Idle Process'}
{'pid': 4, 'cpu_percent': 0.0, 'name': 'System'}
{'pid': 108, 'cpu_percent': 0.0, 'name': ''}
{'pid': 144, 'cpu_percent': 0.0, 'name': 'Registry'}
{'pid': 160, 'cpu_percent': 0.0, 'name': 'svchost.exe'}
System health check complete.


## APPLICATION HEALTH CHEAKER

## Overview
This script checks the uptime and status of a web application by sending HTTP requests and verifying the response status codes. It helps ensure that the application is functioning correctly.

## Features
- Sends HTTP GET requests to a specified web application URL.
- Reports whether the application is "UP" (HTTP status 200) or "DOWN" (any other status).
- Can be easily customized to check different application endpoints if needed.

## Requirements
- Python 3.x
- `requests` library (install using `pip install requests`)

## Example Output

Checking application health...
Application is UP
