from telnetlib import Telnet
import time


def telnet_connect(ip,  username, password, cmd_list, enable=None, verbose=True):
    tn = Telnet(ip, 23)
    rackreplay = tn.expect([], timeout=1)[2].decode().strip()
    if verbose:
        print(rackreplay)
    tn.write(username.encode())
    tn.write(b'\n')
    time.sleep(1)
    rackreplay = tn.expect([], timeout=1)[2].decode().strip()
    if verbose:
        print(rackreplay)
    tn.write(password.encode())
    tn.write(b'\n')
    time.sleep(1)
    rackreplay = tn.expect([], timeout=1)[2].decode().strip()
    if verbose:
        print(rackreplay)
    if enable is not None:
        tn.write(b'enable\n')
        time.sleep(1)
        rackreplay = tn.expect([], timeout=1)[2].decode().strip()
        if verbose:
            print(rackreplay)
        tn.write(enable.encode())
        tn.write(b'\n')
        rackreplay = tn.expect([], timeout=1)[2].decode().strip()
        if verbose:
            print(rackreplay)
    time.sleep(1)
    for cmd in cmd_list:
        tn.write(cmd.encode() + b'\n')
        rackreplay = tn.expect([], timeout=1)[2].decode().strip()
        if verbose:
            print(rackreplay)
        time.sleep(1)
    tn.write(b'exit\n')
    rackreplay = tn.expect([], timeout=1)[2].decode().strip()
    if verbose:
        print(rackreplay)
    tn.close()


    if __name__ == '__main__':
        telnet_connect('192.168.3.3', 'admin', 'cisco123', ['show ip int brief', 'show ip route'])


