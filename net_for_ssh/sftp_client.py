# 使用paramiko实现sftp上传下载

from paramiko import SSHClient, AutoAddPolicy

def ssh_sftp_put(ip, username, password, local_file, remote_fiel, port=22):
    ssh = SSHClient()
    ssh.set_missing_host_key_policy(AutoAddPolicy())
    ssh.connect(ip, port, username, password)
    sftp = ssh.open_sftp()
    sftp.put(local_file, remote_fiel)       # 上传本地到远端
    ssh.close()

def ssh_sftp_get(ip, username, password, local_file, remote_fiel, port=22):
    ssh = SSHClient()
    ssh.set_missing_host_key_policy(AutoAddPolicy())
    ssh.connect(ip, port, username, password)
    sftp = ssh.open_sftp()
    sftp.get(remote_fiel, local_file)       # 下载远端到本地


if __name__ == '__main__':
    ssh_sftp_put('192.168.3.19', 'root', 
                 'eve', './sftp_python.txt', 
                 './python.txt')        #  上传文件到eve服务器
    ssh_sftp_get('192.168.3.19', 'root',
                 'eve', './remote_eve.txt',
                 '/root/eve.txt')    # get文件到本地