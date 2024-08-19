# 使用paramiko传递多个命令

from paramiko import SSHClient,AutoAddPolicy
import time


def ssh_client_multi_cmd(ip, username, passwrod, cmd_list, verbose=False):
    ssh = SSHClient()
    ssh.set_missing_host_key_policy(AutoAddPolicy())
    ssh.connect(hostname=ip, 
                username=username, password=passwrod,
                look_for_keys=False)
    ssh_shell = ssh.invoke_shell()      # 打开一个交互式会话
    time.sleep(1)
    result = ssh_shell.recv(4096).decode()
    for cmd in cmd_list:
        ssh_shell.send(cmd + '\n')
        time.sleep(1)
        result += ssh_shell.recv(4096).decode()
        if verbose:
            print(result)        # 返回回显
         
    ssh.close()


if __name__ == '__main__':
    cmd_list = ['terminal len 0', 'show inter brief', 
                'conf t ', 'inter l 10', 
                'ip add 10.10.10.10 255.255.255.255']
    no_inter_loop = ssh_client_multi_cmd('192.168.3.3',
                         'admin',
                         'cisco123',
                         cmd_list=cmd_list,
                         verbose=True)
    print(no_inter_loop)