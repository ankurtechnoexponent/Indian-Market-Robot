import paramiko

username = "admin"
passwd = "Admin@123"
ip = "192.168.1.7"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip, username=username, password=passwd,port=22)
sftp_client = ssh_client.open_sftp()
print(dir(sftp_client))
