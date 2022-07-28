from functions import *
from constants import *
from add import *
from see import *
from example import *


def main():
    while True:
        name = produce_random_calling()
        waiting("--> What's your command, " + name + "? \
(To see commands, type info)", F0)
        # always smile.
        command = input(">").strip(ignore_these).lower()

        if command == "add":
            add()
        elif command == "see":
            see()
        elif command == "exadd":
            example_add()
        elif command == "info":
            os.system("info.txt")
        else:
            bye = produce_random_farewell()
            waiting("\n" + bye + "\n", F2)
            timer(0.5)
            break

if __name__ == "__main__":
    waiting("*" * 5 + "WELCOME**TO**INTERFACE**FOR**ENGLISH**STUDY" + "*" * 5,
            F0)
    main()
