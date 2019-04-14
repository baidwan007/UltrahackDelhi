import sys
import socket_scheduler_EV
from importlib import reload

part1Cache = None
if __name__ == "__main__":
    while True:
        if not part1Cache:
            part1Cache = socket_scheduler_EV.part1()
        socket_scheduler_EV.part2(part1Cache)
        print ("yo")
        sys.stdin.readline()
        reload(socket_scheduler_EV)