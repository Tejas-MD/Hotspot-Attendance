import subprocess
import time

# Create a dictionary to keep track of the number of times each bench has been occupied
benches = {}
total_rows = 4
total_columns = 6

def scan_wifi_networks():
    devices = subprocess.check_output(['netsh', 'wlan', 'show', 'network'])
    devices = devices.decode('ascii')
    devices = devices.replace("\r", "")
    return devices



def print_bench_matrix(benches):
    # Create a matrix with 4 rows and 6 columns
    matrix = []
    for i in range(total_rows):
        row = []
        for j in range(total_columns):
            bench = (i+1, j+1)
            if bench in benches:
                count = benches[bench]
                if count == 1:
                    row.append("?")
                elif count == 2:
                    row.append("✓")
                # elif count == 0:
                    # row.append("X")
            else:
                row.append("X")
                # empty_benches += 1

        matrix.append(row)

    # Print the matrix
    print("\n".join([" ".join(row) for row in matrix]))




while True:
    benches = {}
    network_list = scan_wifi_networks()

    # print(network_list)
    network_list = network_list.split("\n")

    filtered_network_list = []


    for network in network_list:
        if network.startswith("SSID"):
            ssid = network.split(":")[1].strip()
            if ssid.startswith("1BY"):
                filtered_network_list.append(ssid)

                bench_coordinate = int(ssid[-2:])
                x = bench_coordinate // 10
                y = bench_coordinate % 10
                bench = (x, y)
                # print("Bench Coordinate:", bench)

                if bench in benches:
                    benches[bench] += 1
                else:
                    benches[bench] = 1
                # print("Current bench occupancies:", benches)
    
    # Check for any benches that have been occupied more than twice
    for bench, count in benches.items():
        if count > 2:
         print("Possible attendance issue at bench", bench)
        # if count == 0:
            # empty_benches += 1
    empty_benches = 0

    for i in range(total_rows):
        for j in range(total_columns):
            bench = (i+1, j+1)
            if bench in benches:
                count = benches[bench]
            # print("j:", j)
                if count == 1 or count == 2:
                    continue
            else:
                empty_benches += 1
    
    print("Empty benches:", empty_benches)

    print_bench_matrix(benches)

    three_char_list = [network[3:6] for network in filtered_network_list]
    print("Students present: ")
    print(three_char_list)

    three_char_int_list = [int(network) for network in three_char_list]

    absent_numbers = []

    for i in range(133, 200):
        if i not in three_char_int_list:
            absent_numbers.append(i)
    print("Absent students: ")
    print(absent_numbers)

    time.sleep(5) # waits for 5 seconds before running the loop again
