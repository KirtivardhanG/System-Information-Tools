# System Information Tools
# Mini Project 1 Cloud Computing/ DevOps

import os
import platform
import socket
import psutil

hostname = socket.gethostname()
print(hostname)

operating_system = platform.system()
os_version = platform.version()

python_version = platform.python_version()
cpu_usage = psutil.cpu_percent(interval = 1)

memory_usage = psutil.virtual_memory().percent
disk_usage = psutil.disk_usage('/').percent

ip_address = socket.gethostbyname(hostname)

print("       System Information")
print("----------------------------")
print("Hostname:         {hostname}")
print("Operating System: {operating_system}")
print("Python Version:   {python_version}")
print("CPU Usage:        {cpu_usage}")
print("Memory Usage:     {memory_usage}%")
print("Disk Usgae:       {disk_usage}%")
print("IP Address:       {ip_address}")
