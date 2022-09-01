import time

localTime = time.localtime()

if localTime.tm_hour >= 19:
    response = 'Es hora de ir a casa son las {} (horas) {} (minutos) y {} (segundos), terminas a las 19hrs, máquina'.format(localTime.tm_hour, localTime.tm_min, localTime.tm_sec)
    print(response)
else:
    response  = 'Quedan {} (horas) {} (minutos) y {} (segundos) para salir'.format(18-localTime.tm_hour, 59-localTime.tm_min, 59-localTime.tm_sec)
    print(response)
