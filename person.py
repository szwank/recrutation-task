from Manager import Manager
from Options import Options
from database.Database import Database


def main():
    options = Options()
    args = options.get_arguments()

    database = Database()

    manager = Manager(args, database)
    manager.run()


if '__main__' == __name__:
    main()
