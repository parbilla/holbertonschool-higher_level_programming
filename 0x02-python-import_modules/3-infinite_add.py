#!/usr/bin/python3
import sys
if __name__ == "__main__":
    suma = 0
    if len(sys.argv) == 1:
        print(suma)
    else:
        for i in range(1, len(sys.argv)):
            suma += int(sys.argv[i])
        print(suma)
