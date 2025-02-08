import requests
import json


def login():
    payloadLogin = {"aaaUser":{"attributes":{"name":"admin","pwd":"!v3G@!4@Y"}}}
    url_login = "https://sandboxapicdc.cisco.com/api/aaaLogin.json"

    response = requests.post(url=url_login, json=payloadLogin, verify=False)

    if (response.status_code == 200):
        data = response.json()
        token = data["imdata"][0]["aaaLogin"]["attributes"]["token"]
        return token
    raise Exception("Error Auth")



# collecter l'inventaire du serveur ACI
    
def get_inventory(token):
    url = "https://sandboxapicdc.cisco.com/api/node/class/fabricNode.json"
    header = {
        "Cookie": "APIC-cookie=" + token
    }

    response = requests.get(url=url, headers=header, verify=False)

    if (response.status_code == 200):
        data = response.json()
        for device in data["imdata"]:
            name = device['fabricNode']['attributes']['name']
            role = device['fabricNode']['attributes']['role']
            ip = device['fabricNode']['attributes']['address']
            print(f"Name: {name}    Role: {role}    IP Add: {ip}")
        return ""
    raise Exception("Error Auth")    



token = login()
get_inventory(token)
