import time

print(time.time_ns())
print(time.time())
print(time.ctime(time.time()))
timeSet = time.struct_time((2019, 2, 26, 7, 6, 55, 1, 57, 0))
hourD = timeSet.tm_hour
print(hourD)
# time = None
# deadline = None
#
# if time > deadline:
#     print('Es hora de ir a casa')