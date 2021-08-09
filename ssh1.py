import paramiko
hostnames = ["192.168.49.137", "192.168.49.136" ]
username = "ramu"
password = "ramu"

commands = [ "uptime" , "date", "uname -a"]

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    for i in hostnames:
      client.connect(hostname=i, username=username, password=password )
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


