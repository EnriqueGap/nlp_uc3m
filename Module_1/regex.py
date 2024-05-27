import zipfile
import re

logsHTTP="""199.72.81.55 - - [01/Jul/1995:00:00:01 -0400] "GET /history/apollo/ HTTP/1.0" 200 6245
unicomp6.unicomp.net - - [01/Jul/95:00:00:06 -0400] "GET /shuttle/countdown/ HTTP/1.0" 200 3985
199.120.110.21 - - [01/Jul/1995:00:00:09 -0400] "GET /shuttle/missions/sts-73/mission-sts-73.html HTTP/1.0" 200 4085
 burger.letters.com - - [01/Jul/1995-00:00:11 -0400] "GET /shuttle/countdown/liftoff.html HTTP/1.0" 304 0
199.120.110.21 - - [01/Jul/1995:00:00:11 -0400] "GET /shuttle/missions/sts-73/sts-73-patch-small.gif HTTP/1.0" 200 -
burger.letters.com - - [01/July/1995:00:00:12 -0400] "GET /images/NASA-logosmall.gif HTTP/1.0" 304 0
burger.letters.com - - [01/Jul/1995:00:00:12 -0400] "GET /shuttle/countdown/video/livevideo.gif HTTP/1.0" 200 -
205.212.115.106 - - [01/Jul/1995:00:00:12 -0400] "GET /shuttle/countdown/countdown.html HTTP/1.0" 200 3985
 - - [01/Jul/1995:00:00:13 -0400] "GET /shuttle/countdown/ HTTP/1.0" 200 3985
129.94.144.152 - - [01/Jul/1995:00:00:13 -0400] "GET / HTTP/1.0" 200 -
unicomp6.unicomp.net - - [01/Jul/1995:00:00:14] "GET /shuttle/countdown/count.gif HTTP/1.0" 200 40310
unicomp6.unicomp.net - - [01/Jul/1995:00:00:14 -0400] "GET /images/NASA-logosmall.gif HTTP/1.0" 200 786
pipe6.nyc.pipeline.com - - [01/Jul/1995:00:22:43 -0400] "GET /shuttle/missions/sts-71/movies/sts-71-mir-dock.mpg" 200 946425
columbia.acc.brad.ac.uk - - [01/Jul/1995:00:51:31 -0400] "GET /ksc.html" 200 7074"""

records = logsHTTP.split("\n")

expression = r"^([\S.-]+)"
list_host = [re.search(expression, reg).group(1) for reg in records if re.search(expression, reg)]
print("Hosts")
print(list_host)
print('*' * 20)

expression = r"(\d{2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2})\s\-\d{4}"
list_date = [re.search(expression, reg).group(1) for reg in records if re.search(expression, reg)]
print("Dates")
print(list_date)
print('*' * 20)

expression = r'GET\s+([^"]+)\s+HTTP'
list_request = [re.search(expression, reg).group(1) for reg in records if re.search(expression, reg)]
print("Request")
print(list_request)
print('*' * 20)

expression = r'"GET.*"\s+(\d{3})'
list_status = [re.search(expression, reg).group(1) for reg in records if re.search(expression, reg)]
print("Status")
print(list_status)
print('*' * 20)

expression = r"(-|\d+)$"
list_bytes = [re.search(expression, reg).group(1) for reg in records if re.search(expression, reg)]
print("Bytes")
print(list_bytes)
print('*' * 20)

with zipfile.ZipFile('../data/NASA_access_red.log.zip') as myzip:
    with myzip.open('NASA_access_red.log') as myfile:
       logsHTTP = myfile.read().decode('UTF-8')

final_records = logsHTTP.split("\n")

def parse_record(record : list) -> dict:
    regex = r'^(?P<IP>([\S.-]+)) - - \[(?P<Date>(\d{2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2}))\s[\-]\d{4}\] "GET\s+(?P<Request>([^"]+))" (?P<Status>(\d{3})) (?P<Bytes>(-|\d+))$'

    match = re.match(regex, record)

    if match:
        dict_record = match.groupdict()
        dict_record["Bytes"] = int(dict_record["Bytes"]) if dict_record["Bytes"] != '-' else 0
        return dict_record
    else:
        # Si no hay coincidencias, imprimir el registro para depuración
        print("Unmatched:", record)
        return None

print([parse_record(reg) for reg in records])
print("*" * 20)
print("*" * 20)
print("*" * 20)
data_parsed = [parse_record(reg) for reg in final_records]