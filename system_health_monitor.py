import psutil
import logging
from datetime import datetime

# Setup logging
logging.basicConfig(filename='system_health.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Thresholds
CPU_THRESHOLD = 80  # in percentage
MEMORY_THRESHOLD = 80  # in percentage
DISK_THRESHOLD = 80  # in percentage

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f'High CPU usage detected: {cpu_usage}%')
    return cpu_usage

def check_memory_usage():
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent
    if memory_usage > MEMORY_THRESHOLD:
        logging.warning(f'High Memory usage detected: {memory_usage}%')
    return memory_usage

def check_disk_usage():
    disk_info = psutil.disk_usage('/')
    disk_usage = disk_info.percent
    if disk_usage > DISK_THRESHOLD:
        logging.warning(f'High Disk usage detected: {disk_usage}%')
    return disk_usage

def check_running_processes():
    process_count = len(psutil.pids())
    logging.info(f'Number of running processes: {process_count}')
    return process_count

def log_system_health():
    cpu_usage = check_cpu_usage()
    memory_usage = check_memory_usage()
    disk_usage = check_disk_usage()
    process_count = check_running_processes()

    logging.info(f'System Health - CPU: {cpu_usage}%, Memory: {memory_usage}%, Disk: {disk_usage}%, Processes: {process_count}')

if __name__ == '__main__':
    log_system_health()
