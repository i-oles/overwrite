import paramiko
import time

host = "192.168.0.42"
username = "pi"
password = "raspberry"

command = 'ls'

client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=username, password=password)

stdin, stdout, stderr = client.exec_command('ls -la')
time.sleep(5)

print(stdout.read().decode())



