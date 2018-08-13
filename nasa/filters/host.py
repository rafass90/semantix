from helpers.helper import (filter_host, get_host_date, is_number,
                            sum_error_data, sum_error_host)


def count_unique_hosts(logs):
    hosts = logs.filter(lambda x: x if filter_host(x) else None)
    unique_hosts = hosts.distinct()

    return unique_hosts.count()


def error_for_host(lines, spark_context):
    list_host_date = get_host_date(lines)
    data = sum_error_host(list_host_date)
    result = spark_context.parallelize(data.items()).top(5, key=lambda x: x[1])
    return result


def error_for_day(lines):
    list_host_date = get_host_date(lines)
    return sum_error_data(list_host_date)


def sum_total_bytes(text_file):
    total_bytes = 0
    for data in text_file.toLocalIterator():
        value = data.split(' ')[-1::][0]
        if is_number(value):
            total_bytes += int(value)
    return total_bytes
