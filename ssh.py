import paramiko
import os
privateketfile = os.path.expanduser('/home/ramu/.ssh/id_rsa')
mykey = paramiko.RSAKey.from_private_key_file(privateketfile)
hostnames = ["192.168.49.137", "192.168.49.136" ]
username = "ramu"

commands = [ "uptime" , "date", "uname -a"]

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    for i in hostnames:
      client.connect(hostname=i, username=username, pkey = mykey )
      for command in commands:
        print("="*50, command, "="*50)
        stdin, stdout, stderr = client.exec_command(command)
        print(stdout.read().decode())
        err = stderr.read().decode()
        if err:
          print(err)

except:
    print("[!] Cannot connect to the SSH Server")
    exit()


