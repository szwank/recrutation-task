from Manager import Manager
from Options import Options


def main():
    options = Options()
    args = options.get_arguments()
    manager = Manager(args)
    manager.run()


if '__main__' == __name__:
    main()
