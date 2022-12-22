import time

localTime = time.localtime()

if localTime.tm_hour >= 19:
    response = 'It\'s time to go home. It\'s {} hours {} minutes y {} seconds.'.format(localTime.tm_hour, localTime.tm_min, localTime.tm_sec)
    print(response)
else:
    response  = 'Keep focus. Remain {} hours {} minutes y {} seconds left to go home'.format(18-localTime.tm_hour, 59-localTime.tm_min, 59-localTime.tm_sec)
    print(response)
