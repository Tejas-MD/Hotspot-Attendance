import subprocess
import time

def scan_wifi_networks():
    devices = subprocess.check_output(['netsh', 'wlan', 'show', 'network'])
    devices = devices.decode('ascii')
    devices = devices.replace("\r", "")
    return devices

while True:
    network_list = scan_wifi_networks()

    print(network_list)
    network_list = network_list.split("\n")

    filtered_network_list = []

    for network in network_list:
        if network.startswith("SSID"):
            ssid = network.split(":")[1].strip()
            if ssid.startswith("1BY"):
                filtered_network_list.append(ssid)


    three_char_list = [network[3:6] for network in filtered_network_list]
    print("Students present: ")
    print(three_char_list)

    three_char_int_list = [int(network) for network in three_char_list]

    absent_numbers = []

    for i in range(133, 200):
        if i not in three_char_int_list:
            absent_numbers.append(i)
    
    time.sleep(5) # waits for 5 seconds before running the loop again
