#!/usr/bin/python3
"""Read HTTP logs from standard input and print cumulative metrics."""

import re
import sys


def print_stats(total_size, status_counts):
    """Print total file size and status counts in ascending order."""
    print("File size: {}".format(total_size))
    for code in sorted(status_counts):
        if status_counts[code]:
            print("{}: {}".format(code, status_counts[code]))


def main():
    """Process input and report metrics every ten lines and on exit."""
    total_size = 0
    line_count = 0
    status_counts = {
        "200": 0, "301": 0, "400": 0, "401": 0,
        "403": 0, "404": 0, "405": 0, "500": 0
    }
    pattern = re.compile(
        r'^\d{1,3}(?:\.\d{1,3}){3} - \[[^\]]+\] '
        r'"GET /projects/260 HTTP/1\.1" (\S+) (\d+)$'
    )

    try:
        for line in sys.stdin:
            line_count += 1
            match = pattern.match(line.rstrip("\n"))
            if match:
                code, size = match.groups()
                total_size += int(size)
                if code in status_counts:
                    status_counts[code] += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_counts)
    except KeyboardInterrupt:
        pass
    finally:
        print_stats(total_size, status_counts)


if __name__ == "__main__":
    main()
