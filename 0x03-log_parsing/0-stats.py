#!/usr/bin/python3
"""Log parsing"""


import sys


def print_stats(stats, file_size):
    """Print the status"""
    print(f"File size: {file_size}")
    for code, count in sorted(stats.items()):
        if count:
            print(f"{code}: {count}")


if __name__ == '__main__':
    file_size, count = 0, 0
    stats = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}

    try:
        for line in sys.stdin:
            count += 1
            parts = line.split()

            try:
                status_code = parts[-2]
                if status_code in stats:
                    stats[status_code] += 1
            except IndexError:
                pass

            try:
                file_size += int(parts[-1])
            except (IndexError, ValueError):
                pass

            if count % 10 == 0:
                print_stats(stats, file_size)

        print_stats(stats, file_size)

    except KeyboardInterrupt:
        print_stats(stats, file_size)
        raise
