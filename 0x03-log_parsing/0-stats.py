#!/usr/bin/env python3
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

    for line in sys.stdin:
        try:
            parts = line.split()
            ip_address = parts[0]
            status_code = int(parts[-2])
            file_size = int(parts[-1])

            if parts[5] == '"GET' and parts[6].startswith('/projects/260'):
                total_size += file_size
                status_counts[status_code] += 1
                line_count += 1

                if line_count % 10 == 0:
                    print_stats(total_size, status_counts)

        except (IndexError, ValueError):
            pass


if __name__ == "__main__":
    main()
