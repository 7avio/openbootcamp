def secondWrite():
    newWrite = open('ejercicio_8-1.txt', 'a')
    newWrite.write('This is my second text line written from python!')
    newWrite.close()

def readFile():
    newRead = open('ejercicio_8-1.txt', 'r')
    print(newRead.read())
    newRead.close()


def main():
    newFile = open('ejercicio_8-1.txt', 'a')
    newFile.write('This is my first text line written from python!\n')
    newFile.close()
    secondWrite()
    readFile()




if __name__ == '__main__':
    main()
