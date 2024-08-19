from netmiko import Netmiko
# 查看支持的device_type
# https://github.com/ktbyers/netmiko/blob/master/DEVICE_DATABASE

client = {
    'host': '192.168.3.3',
    'username': 'admin',
    'password': 'cisco123',
    #'device_type': 'cisco_ios_telnet',     # cisco telnet
    'device_type': 'cisco_ios',         # ssh
    'secret': 'Cisco123'
}

net_connect = Netmiko(**client)   # 使用字典映射方式传参数
# '>'用户模式
print(net_connect.send_command('show ip interface brief'))
# '#'特权模式
net_connect.enable()        # 如果需要，使用enable进入特权模式
print(net_connect.send_command('show run'))

# 进入全局配置模式下配置设备
config_commands = ['inter l 10',
                    'description python_config',
                    'ip add 10.10.10.10 255.255.255.255']
output = net_connect.send_config_set(config_commands)
print(output)

net_connect.disconnect()