from paramiko import SSHClient, AutoAddPolicy
import re


def ssh_client_one_cmd(ip, username, password, cmd):
    try:
        client = SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(AutoAddPolicy())
        client.connect(ip,
                       port=22, 
                       username=username,
                        password=password,
                       timeout=5,
                       compress=True,
                       look_for_keys=False)     # 为True时，会寻找本地的ssh-key
        stdin, stdout, stderr = client.exec_command(cmd)
        x = stdout.read().decode()      # 读取回显
        client.close()
        return x
    except Exception as e:
        print(f'{ip} 连接失败，错误信息：{e}')


if __name__ == '__main__':
    ssh_client = ssh_client_one_cmd('192.168.3.3', 
                                    'admin', 
                                    'cisco123', 
                                    'show run')
    # 去掉多余的！行
    cleaned_config = '\n'.join([line for line in ssh_client.splitlines() if 
                                not line.strip().startswith('!')])
    print(cleaned_config)