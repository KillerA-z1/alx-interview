#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics"""
import sys
import re


def print_stats(size, stats):
    """
    Print accumulated statistics.

    Args:
        size (int): The total file size.
        stats (dict): A dictionary containing the statistics to be printed. 
                      Keys are the statistic names and values are their counts.

    Prints:
        The total file size and the statistics in a sorted order by key.
        Only prints statistics where the count is not zero.
    """
    print('File size: {:d}'.format(size))
    for key in sorted(stats.keys()):
        if stats[key] != 0:
            print('{}: {}'.format(key, stats[key]))


i = 0
sum_file_size = 0
status_code = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}

pattern = r'^[\d.]+\s+-\s+\[[^\]]+\]\s+"GET\s+/projects/260\s+HTTP/1\.1"\s+(\d+)\s+(\d+)$'

try:
    for line in sys.stdin:
        try:
            # Use regex to extract status code and file size
            match = re.match(pattern, line.strip())
            if match:
                status = match.group(1)
                file_size = match.group(2)
                
                # Update metrics if status code is valid
                if status in status_code:
                    status_code[status] += 1
                sum_file_size += int(file_size)
                
                i += 1
                if i == 10:
                    print_stats(sum_file_size, status_code)
                    i = 0
                    
        except (ValueError, IndexError):
            continue
            
except KeyboardInterrupt:
    pass
finally:
    print_stats(sum_file_size, status_code)
