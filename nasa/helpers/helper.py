import re


def filter_host(data):
    regex_host = '^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$'  # noqa
    return re.match(regex_host, data, flags=0)


def is_number(value):
    return re.match(pattern='[\d]', string=value)


def is_404_error(data):
    return str(data) == '404'


def sum_error_data(error_list):
    data = dict()
    for error in error_list:
        if len(error) < 2:
            continue
        try:
            data[error[1]] += 1
        except Exception:
            print(f'Key: {error[0]} not found.')
            data.update({error[1]: 1})

    return data


def sum_error_host(error_list):
    data = dict()
    for error in error_list:
        try:
            try:
                data[error[0]] += 1
            except Exception:
                print(f'Key: {error[0]} not found.')
                data.update({error[0]: 1})
        except Exception as e:
            print(f'{error} - Exception: {e}')
    return data


def get_host_date(lines):
    list_host_date = []
    for line in lines:
        list_host_date += [[
            text.replace('[', '')
            for text in line.split(':')[0].split() if text != '-'
        ]]
    return list_host_date
