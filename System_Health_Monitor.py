import psutil
import time

# Define thresholds
CPU_THRESHOLD = 80  # CPU usage in percentage
MEMORY_THRESHOLD = 80  # Memory usage in percentage
DISK_THRESHOLD = 90  # Disk usage in percentage

# Function to check CPU usage
def check_cpu():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        print(f"ALERT: High CPU usage detected: {cpu_usage}%")
    else:
        print(f"CPU usage is normal: {cpu_usage}%")

# Function to check memory usage
def check_memory():
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    if memory_usage > MEMORY_THRESHOLD:
        print(f"ALERT: High Memory usage detected: {memory_usage}%")
    else:
        print(f"Memory usage is normal: {memory_usage}%")

# Function to check disk space usage
def check_disk():
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    if disk_usage > DISK_THRESHOLD:
        print(f"ALERT: High Disk usage detected: {disk_usage}%")
    else:
        print(f"Disk usage is normal: {disk_usage}%")

# Function to list running processes
def check_processes():
    processes = [proc.info for proc in psutil.process_iter(['pid', 'name', 'cpu_percent'])]
    print("Top 5 Running Processes:")
    for proc in processes[:5]:
        print(proc)

# Main function to monitor the system health
def monitor_system():
    print("Starting system health check...")
    check_cpu()
    check_memory()
    check_disk()
    check_processes()
    print("System health check complete.\n")

# Run system check every minute
while True:
    monitor_system()
    time.sleep(60)  # Wait for 60 seconds before the next check