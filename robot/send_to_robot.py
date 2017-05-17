import paramiko

ip_address = '192.168.0.1'
usrname = 'robot'
pwd = 'maker'
ssh = SSHClient() #open an ssh tunnel
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #to avoid missing_host_key error
ssh.connect(ip_address,username=usrname,password=pwd)#connect to IP address with username usrname and password pwd
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('/move.py') #command to execute
if(ssh_stderr != ""):
    print ssh_stderr
