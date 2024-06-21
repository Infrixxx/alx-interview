#!/usr/bin/python3
import sys
import re
from collections import defaultdict

def print_stats(total_size, status_codes):
    """Print the current statistics."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

total_size = 0
line_count = 0
status_codes = defaultdict(int)
log_pattern = re.compile(r'\S+ - \[\S+\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)')

try:
    for line in sys.stdin:
        match = log_pattern.match(line)
        if match:
            status_code = int(match.group(1))
            file_size = int(match.group(2))

            total_size += file_size
            status_codes[status_code] += 1

        line_count += 1

        if line_count % 10 == 0:
            print_stats(total_size, status_codes)

except KeyboardInterrupt:
    print_stats(total_size, status_codes)
    raise

print_stats(total_size, status_codes)
