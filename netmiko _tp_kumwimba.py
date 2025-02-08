from netmiko import ConnectHandler

cisco1 = {
    "device_type": "cisco_nxos",
    "host": "sandbox-iosxr-1.cisco.com",
    "username": "admin",
    "password": "C1sco12345"
}

net_connect = ConnectHandler(**cisco1)
reponse = net_connect.send_command("show ip int brief")
print(reponse)
net_connect.disconnect()
