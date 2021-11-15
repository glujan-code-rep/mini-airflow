import paramiko as pk

host = "localhost"
port = 22
username = ""
password = ""

command = "/usr/bin/python3 /home/guillorocker/Escritorio/dags/class_linked_list.py"

ssh = pk.SSHClient()
ssh.set_missing_host_key_policy(pk.AutoAddPolicy())
ssh.connect(host, port, username, password)

stdin, stdout, stderr = ssh.exec_command(command)
lines = stdout.readlines()
print(lines)
#print(stdin)
print(stderr)