from pyspark import SparkContext

from filters.host import (count_unique_hosts, error_for_day, error_for_host,
                          sum_total_bytes)
from helpers.helper import is_404_error

files = 'log/access_log*'


sc = SparkContext('local', 'nasa')
textFile = sc.textFile(files)
data_error = textFile.filter(lambda x: is_404_error(x[-5::][:3]))

list_error = [data for data in data_error.toLocalIterator()]

# Count Unique Hosts
print('Count Unique Hosts\n')
logs = textFile.flatMap(lambda x: x.split(" "))
num_hosts = count_unique_hosts(logs=logs)
print(f'Count unique hosts: {num_hosts}')

# Count 404 errors
print('Total 404 Erros:\n')
print(f'Total 404 error: {data_error.count()}')

# Top five errors host
print('Top five errors host\n')
top_five = error_for_host(lines=list_error, spark_context=sc)
print(f'Top five: {top_five}')

# Error for days
print('Error For Days\n')
erro_days = error_for_day(list_error)
print(f'Errors for days: {erro_days}')

# Total Bytes
print('Sum Total Bytes:')
result = sum_total_bytes(text_file=textFile)
print(f'Sum total bytes: {result}')
