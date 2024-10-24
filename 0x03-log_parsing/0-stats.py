#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics"""
import sys

line_counter = 0
total_file_size = 0
status_codes_count = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}

try:
    for log_line in sys.stdin:
        line_parts = log_line.split(' ')
        if len(line_parts) > 2:
            http_status = line_parts[-2]
            file_size = line_parts[-1]
            if http_status in status_codes_count:
                status_codes_count[http_status] += 1
            total_file_size += int(file_size)
            line_counter += 1
            if line_counter == 10:
                print('File size: {:d}'.format(total_file_size))
                sorted_status_codes = sorted(status_codes_count.keys())
                for status_code in sorted_status_codes:
                    count = status_codes_count[status_code]
                    if count != 0:
                        print('{}: {}'.format(status_code, count))
                line_counter = 0
except Exception:
    pass
finally:
    print('File size: {:d}'.format(total_file_size))
    sorted_status_codes = sorted(status_codes_count.keys())
    for status_code in sorted_status_codes:
        count = status_codes_count[status_code]
        if count != 0:
            print('{}: {}'.format(status_code, count))
