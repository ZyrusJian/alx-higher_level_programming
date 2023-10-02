#!/usr/bin/python3
"""
This script reads stdin line by line and computes metrics.

Input format: (<IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size>)
Each 10 lines and after a keyboard interruption (CTRL + C),
prints those statistics since the beginning:
- Total file size: File size: <total size> where <total size> is
the sum of all previous file sizes.
- Number of lines by status code:
  - possible status code: 200, 301, 400, 401, 403, 404, 405, and 500
  - if a status code doesn’t appear, don’t print anything for this status code
  - format: <status code>: <number>
  - status codes should be printed in ascending order
  - consider this cases:
    - One line of log: then prints the statistics of one line
    - 10 lines of log : then prints those statistics since the beginning
    - 10 lines of log with only 200 as status code:
    then prints those statistics since the beginning
    - empty file: then print log not found
    - long log: then prints those statistics after multiples of 10 lines
    - wrong input format: then print log has invalid format
"""

import sys

status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
status_count = {code: 0 for code in status_codes}
total_size = 0
line_count = 0


def compute_metrics(line):
    """
    Computes metrics for a single line of log.

    Args:
        line (str): A single line of log.

    Returns:
        tuple: A tuple containing the total file size and
        the count of each status code.
    """
    global total_size, line_count, status_count
    try:
        ip, _, _, date, _, request, status, size = line.split()
        if request != 'GET /projects/260 HTTP/1.1':
            return None
        if status not in status_codes:
            return None
        status_count[status] += 1
        total_size += int(size)
        line_count += 1
        if line_count % 10 == 0:
            print(f"File size: {total_size}")
            for code in sorted(status_codes):
                if status_count[code] > 0:
                    print(f"{code}: {status_count[code]}")
    except ValueError:
        return None
    return total_size, status_count


try:
    for line in sys.stdin:
        metrics = compute_metrics(line)
        if metrics is None:
            print("log has invalid format")
        elif line_count == 1:
            print(f"File size: {total_size}")
            for code in sorted(status_codes):
                if status_count[code] > 0:
                    print(f"{code}: {status_count[code]}")
        elif line_count % 10 == 1:
            print(f"File size: {total_size}")
            for code in sorted(status_codes):
                if status_count[code] > 0:
                    print(f"{code}: {status_count[code]}")
        elif all(value == 0 for value in status_count.values()):
            print("log not found")
        elif all(value == 0 for key, value in status_count.items()
                 if key != '200'):
            print(f"File size: {total_size}")
            print(f"200: {status_count['200']}")
        elif line_count % 10 == 0:
            print(f"File size: {total_size}")
            for code in sorted(status_codes):
                if status_count[code] > 0:
                    print(f"{code}: {status_count[code]}")
except KeyboardInterrupt:
    pass

if line_count > 0:
    print(f"File size: {total_size}")
    for code in sorted(status_codes):
        if status_count[code] > 0:
            print(f"{code}: {status_count[code]}")
