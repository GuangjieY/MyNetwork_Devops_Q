import asyncio
import os
import threading
import netmiko
from net_for_ssh import netmiko_show_cred
from datetime import datetime

# 创建一个事件循环
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

device = {
    'device_type': 'cisco_ios',
    'host': '192.168.3.3',
    'username': 'admin',
    'password': 'cisco123',
    'secret': 'Cisco123',
    'port': 22,
}

# 定义netmiko的携程函数
async def async_netmiko(task_id, ip, username, password, cmd):
    print(f'ID: {task_id} Started ')
    print(os.getpid(), threading.current_thread().ident)
    result = await loop.run_in_executor(None, 
                                        netmiko_show_cred, 
                                        ip, 
                                        username, 
                                        password, 
                                        cmd)
    print(f'ID: {task_id} Finished ')
    return ip, result    

if __name__ == '__main__':
    # 设备列表
    device_list = ['192.168.3.3', '192.168.3.4', '192.168.3.5']
    # 把ip，username，password，cmd放到一个列表，便于后续使用*device来传参数
    devices_cmd_list =[[d, 'admin', 'cisco123', 'show run'] for d in device_list]

    start_time = datetime.now()
    # ===========普通操作===============
    for d in devices_cmd_list:
        cmd_result = netmiko_show_cred(*d)
        print('=' * 20 + d[0] + '=' * 20)
        print(cmd_result)

    # ===========异步操作===============
    task_no = 1     # 循环任务计数号
    tasks = []     # 存放任务列表
    for d in devices_cmd_list:
        task = loop.create_task(async_netmiko(task_no, *d))
        tasks.append(task)
        task_no += 1
    loop.run_until_complete(asyncio.wait(tasks))
    # 提取并且打印结果，0号位为IP，1号位为结果
    for s in tasks:
        if s.result():
            print('=' * 20 + s.result()[0] + '=' * 20)
            print(s.result()[1])
            
    # ===========记录时间，打印耗时===============
    end_time = datetime.now()
    print(f'耗时: {(end_time - start_time).seconds}')