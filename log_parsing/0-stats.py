#!/usr/bin/python3
"""Read log lines and print cumulative metrics."""

import sys


def print_stats(total_size, status_counts):
    """Print total size and status counts in ascending order."""
    print("File size: {}".format(total_size))
    for code in sorted(status_counts):
        if status_counts[code]:
            print("{}: {}".format(code, status_counts[code]))


def main():
    """Read stdin and report metrics every ten lines and on exit."""
    total_size = 0
    line_count = 0
    status_counts = {
        "200": 0, "301": 0, "400": 0, "401": 0,
        "403": 0, "404": 0, "405": 0, "500": 0
    }

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()

            if len(parts) >= 2:
                try:
                    size = int(parts[-1])
                except ValueError:
                    pass
                else:
                    if size >= 0:
                        total_size += size
                        code = parts[-2]
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
