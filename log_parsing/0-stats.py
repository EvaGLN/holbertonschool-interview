#!/usr/bin/python3
"""Log Parsing"""
import sys


def print_stats(total_size, status_codes):
    """print cumulated stats"""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))


if __name__ == "__main__":
    valid_status_codes = {200, 301, 400, 401, 403, 404, 405, 500}

    total_size = 0
    status_codes = {}
    line_count = 0

    try:
        for line in sys.stdin:
            stripped = line.strip()
            parts = stripped.split()

            if len(parts) < 2:
                continue
            if '"GET /projects/260 HTTP/1.1"' not in stripped:
                continue

            try:
                file_size = int(parts[-1])
            except ValueError:
                continue

            total_size += file_size

            try:
                status_code = int(parts[-2])
            except ValueError:
                status_code = None

            if status_code in valid_status_codes:
                status_codes[status_code] = status_codes.get(
                    status_code, 0) + 1

            line_count += 1
            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

        print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise
