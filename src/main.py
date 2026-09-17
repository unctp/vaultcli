import argparse
import getpass

from authentication import authenticate
from database import get_connection
from manager import (
    add_password,
    delete_password,
    get_password,
    list_services,
    delete_database,
)

def create_parser():
    parser = argparse.ArgumentParser(
        description="vaultcli password manager"
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
    )

    add_parser = subparsers.add_parser(
        "add",
        help="add a password",
    )

    add_parser.add_argument(
        "service",
        help="service name, e.g. github",
    )

    add_parser.add_argument(
        "username",
        help="Username",
    )

    get_parser = subparsers.add_parser(
        "get",
        help="retrieve a password",
    )

    get_parser.add_argument("service")

    subparsers.add_parser(
        "list",
        help="list stored services",
    )

    delete_parser = subparsers.add_parser(
        "delete",
        help="delete a password",
    )

    clean_parser = subparsers.add_parser(
        "clean",
        help="deletes the full database permanently",
    )

    delete_parser.add_argument("service")

    return parser

def main():
    parser = create_parser()
    args = parser.parse_args()

    conn = get_connection()

    try:
        # nothing below this point happens until the user
        # successfully authenticates.
        key = authenticate(conn)

        if args.command == "add":
            password = getpass.getpass("Password: ")

            add_password(
                conn,
                key,
                args.service,
                args.username,
                password,
            )

        elif args.command == "get":
            get_password(
                conn,
                key,
                args.service,
            )

        elif args.command == "list":
            list_services(conn)

        elif args.command == "delete":
            delete_password(
                conn,
                args.service,
            )
        elif args.command == "clean":
            delete_database()

    finally:
        conn.close()


if __name__ == "__main__":
    main()
