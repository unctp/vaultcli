# creates and checks the master password
import getpass
import secrets

from crypto import (
    create_verifier,
    derive_key,
    generate_salt,
    verify_key,
)
from database import create_metadata, get_metadata

def setup_master_password(con):
    print("no master password has been configured")
    print("create one now")

    while True:
        password = getpass.getpass("create master password: ")
        confirmation = getpass.getpass("confirm master password: ")

        if not password:
            print("master password cannot be empty")
            continue

        if not secrets.compare_digest(password, confirmation):
            print("passwords do not match")
            continue

        break

    salt = generate_salt()
    key = derive_key(password, salt)
    verifier = create_verifier(key)

    create_metadata(con, salt, verifier)

    print("master password created successfully")

    return key

def authenticate(con):
    metadata = get_metadata(con)

    if metadata is None:
        return setup_master_password(con)

    salt, verifier = metadata

    for _ in range(3):
        password = getpass.getpass("master password: ")

        key = derive_key(password, salt)

        if verify_key(key, verifier):
            return key

        print("incorrect master password")

    raise SystemExit("too many failed attempts, try harder")
