#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics"""
import sys
import re
from collections import defaultdict


def print_stats(total_size, status_codes):
    """Print the statistics."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def main():
    """ The function handles invalid lines by skipping them and continues
    processing the next line."""
    # Initialize variables
    total_size = 0
    line_count = 0
    status_codes = defaultdict(int)
    valid_codes = {200, 301, 400, 401, 403, 404, 405, 500}

    # Regular expression pattern for the log format
    pattern = (
        r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} '
        r'\d{2}:\d{2}:\d{2}\.\d+\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)$'
    )

    try:
        for line in sys.stdin:
            try:
                # Remove trailing whitespace
                line = line.strip()

                # Match the line against the pattern
                match = re.match(pattern, line)
                if match:
                    # Extract status code and file size
                    status_code = int(match.group(1))
                    file_size = int(match.group(2))

                    # Update metrics
                    if status_code in valid_codes:
                        status_codes[status_code] += 1
                    total_size += file_size
                    line_count += 1

                    # Print stats every 10 lines
                    if line_count % 10 == 0:
                        print_stats(total_size, status_codes)

            except ValueError:
                # Skip lines that don't match the expected format
                continue

    except KeyboardInterrupt:
        # Handle CTRL+C
        print_stats(total_size, status_codes)
        raise


if __name__ == "__main__":
    main()
