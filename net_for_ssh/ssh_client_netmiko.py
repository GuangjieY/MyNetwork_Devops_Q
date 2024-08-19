
from netmiko import Netmiko

def netmiko_show_cred(host, username, password, cmd, enable='Cisco123'):
    device_info = {
        'host' : host,
        'username' : username,
        'password': password,
        'device_type': 'cisco_ios',
        'secret': enable
    }
    try:
        net_connect = Netmiko(**device_info)
        return net_connect.send_command(cmd)
    
    except Exception as e:
        print(f'connection error ip: {host} error: {str(e)}')
        return
    

def netmiko_config_cred(host, username, password, cmd_list, enable='Cisco123', verbose=False):
    device_info = {
        'host': host,
        'username': username,
        'password': password,
        'device_type': 'cisco_ios',
        'secret': enable
    }
    try:
        net_connect = Netmiko(**device_info)
        if verbose:     # 不产生回显，如需要回显，则verbose=True
            output = net_connect.send_config_set(cmd_list)
            return output
        else:
            net_connect.send_config_set(cmd_list)
    except Exception as e:
        print(f'connection error ip: {host} error: {str(e)}')
        return
    

if __name__ == '__main__':
    show_ip = netmiko_show_cred('192.168.3.3', 'admin', 'cisco123', 'show ip int brief')
    print(show_ip)
    # 配置设备loopback接口
    config_commands = ['int loopback 100', 
                       'ip address 1.1.1.1 255.255.255.255']
    netmiko_config_cred('192.168.3.3', 'admin', 'cisco123', config_commands, verbose=True)