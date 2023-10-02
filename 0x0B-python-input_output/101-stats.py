#!/usr/bin/python3
"""
This script reads stdin line by line and computes metrics.

Input format: (<IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size>)
Each 10 lines and after a keyboard interruption (CTRL + C),
prints those statistics since the beginning:
- Total file size: File size: <total size> where <total size> is the sum
of all previous file sizes.
- Number of lines by status code:
  - possible status code: 200, 301, 400, 401, 403, 404, 405, and 500
  - if a status code doesn’t appear, don’t print anything for this status code
  - format: <status code>: <number>
  - status codes should be printed in ascending order
  - consider this cases:
    - One line of log
    - 10 lines of log
    - 10 lines of log with only 200 as status code
    - empty file
    - long log
    - wrong input format
"""

import sys

status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
status_count = {code: 0 for code in status_codes}
total_size = 0
line_count = 0

try:
    for line in sys.stdin:
        try:
            ip, _, _, date, _, request, status, size = line.split()
            if request != 'GET /projects/260 HTTP/1.1':
                continue
            if status not in status_codes:
                continue
            status_count[status] += 1
            total_size += int(size)
            line_count += 1
            if line_count % 10 == 0:
                print(f"File size: {total_size}")
                for code in sorted(status_codes):
                    if status_count[code] > 0:
                        print(f"{code}: {status_count[code]}")
        except ValueError:
            pass
except KeyboardInterrupt:
    pass

print(f"File size: {total_size}")
for code in sorted(status_codes):
    if status_count[code] > 0:
        print(f"{code}: {status_count[code]}")
