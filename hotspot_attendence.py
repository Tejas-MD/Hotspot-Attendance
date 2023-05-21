import time

from helper_functions import scan_wifi_networks, process_network_list, count_empty_benches, print_bench_matrix, get_present_students, get_absent_students
from helper_functions import total_columns, total_rows



while True:
    benches = {}
    network_list = scan_wifi_networks()

    if network_list is None:
        break

    benches, filtered_network_list = process_network_list(network_list)
    
    empty_benches = count_empty_benches(benches, total_rows, total_columns)
    
    print("Empty benches:", empty_benches)
    
    print_bench_matrix(benches)
    
    present_students = get_present_students(filtered_network_list)
    print("Students present: ")
    print(present_students)
    
    absent_students = get_absent_students(present_students)
    print("Absent students: ")
    print(absent_students)
    
    time.sleep(10)