#!/usr/bin/python3
"""Log parsing"""


import sys
import signal
from collections import defaultdict

def print_stats(total_size, status_counts):
    print(f"File size: {total_size}")
    for status_code in sorted(status_counts):
        print(f"{status_code}: {status_counts[status_code]}")

def main():
    total_size = 0
    status_counts = defaultdict(int)
    line_count = 0

    def signal_handler(sig, frame):
        print_stats(total_size, status_counts)
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) == 10 and parts[5] == '"GET' and parts[6].startswith('/projects/260'):
                status_code = int(parts[-2])
                file_size = int(parts[-1])
                
                total_size += file_size
                status_counts[status_code] += 1
                line_count += 1

                if line_count % 10 == 0:
                    print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        signal_handler(signal.SIGINT, None)
