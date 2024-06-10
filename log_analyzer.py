import re
from collections import defaultdict, Counter

# Define the log file path (update this to the actual path of your log file)
LOG_FILE_PATH = '/var/log/nginx/access.log'

# Regular expression pattern for common log format
LOG_PATTERN = re.compile(
    r'(?P<ip>\S+) - - \[(?P<date>.*?)\] "(?P<request>.*?)" (?P<status>\d{3}) (?P<size>\S+) "(?P<referrer>.*?)" "(?P<user_agent>.*?)"'
)

def parse_log_line(line):
    match = LOG_PATTERN.match(line)
    if match:
        return match.groupdict()
    return None

def analyze_logs(log_file_path):
    total_requests = 0
    request_counts = defaultdict(int)
    status_counts = defaultdict(int)
    ip_counts = defaultdict(int)
    not_found_errors = 0

    with open(log_file_path, 'r') as file:
        for line in file:
            log_entry = parse_log_line(line)
            if log_entry:
                total_requests += 1
                request_counts[log_entry['request']] += 1
                status_counts[log_entry['status']] += 1
                ip_counts[log_entry['ip']] += 1
                if log_entry['status'] == '404':
                    not_found_errors += 1

    return total_requests, request_counts, status_counts, ip_counts, not_found_errors

def print_report(total_requests, request_counts, status_counts, ip_counts, not_found_errors):
    print(f"Total Requests: {total_requests}")
    print(f"Number of 404 Errors: {not_found_errors}")

    print("\nTop 10 Most Requested Pages:")
    for request, count in Counter(request_counts).most_common(10):
        print(f"{request}: {count}")

    print("\nTop 10 IP Addresses with Most Requests:")
    for ip, count in Counter(ip_counts).most_common(10):
        print(f"{ip}: {count}")

    print("\nHTTP Status Codes:")
    for status, count in status_counts.items():
        print(f"{status}: {count}")

if __name__ == '__main__':
    total_requests, request_counts, status_counts, ip_counts, not_found_errors = analyze_logs(LOG_FILE_PATH)
    print_report(total_requests, request_counts, status_counts, ip_counts, not_found_errors)
