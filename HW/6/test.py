import datetime


date_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
message = f'[{date_now}]'+ 'nickname' +input('')
print(message)