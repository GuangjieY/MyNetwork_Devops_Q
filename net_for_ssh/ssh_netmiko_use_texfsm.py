# use_textfsm=True
# https://github.com/google/textfsm
# 查看支持厂商
# https://gethub.com/networktocode/ntc-templates/tree/master/ntc-templates

from netmiko import Netmiko

def netmiko_show_cred_use_textfsm(host, username,
                                  password,cmd,
                                  enable='Cisco'):
    device_info = {
        'device_type': 'cisco_ios',
        'host': host,
        'username': username,
        'password': password,
        'secret': enable
    }

    try:
        net_cnonect = Netmiko(**device_info)
        # 使用NETC-Template解析
        return net_cnonect.send_command(cmd, use_textfsm=True)
    except Exception as e:
        print(f' connection error ip :{host} error :{str(e)}')
        return
    

if __name__ == '__main__':
    from pprint import pprint
    parsed_result = netmiko_show_cred_use_textfsm(
        '192.168.3.3', 'admin', 'cisco123', 
        'show ip int brief')
    pprint(parsed_result)
