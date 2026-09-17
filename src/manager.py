# password manager logic
from crypto import decrypt, encrypt


def add_password(con, key, service, username, password):
    encrypted_username = encrypt(key, username)
    encrypted_password = encrypt(key, password)

    try:
        con.execute(
            """
            INSERT INTO passwords
                (service, username, password)
            VALUES (?, ?, ?)
            """,
            (
                service,
                encrypted_username,
                encrypted_password,
            ),
        )

        con.commit()
        print(f"added '{service}'")

    except Exception as exc:
        con.rollback()

        if "UNIQUE constraint failed" in str(exc):
            print(f"an entry for '{service}' already exists")
        else:
            raise


def get_password(con, key, service):
    row = con.execute(
        """
        SELECT username, password
        FROM passwords
        WHERE service = ?
        """,
        (service,),
    ).fetchone()

    if row is None:
        print(f"no entry found for '{service}'")
        return

    username = decrypt(key, row[0])
    password = decrypt(key, row[1])

    print(f"service  : {service}")
    print(f"username : {username}")
    print(f"password : {password}")


def list_services(con):
    rows = con.execute(
        """
        SELECT service
        FROM passwords
        ORDER BY service
        """
    ).fetchall()

    if not rows:
        print("no passwords stored")
        return

    for (service,) in rows:
        print(service)


def delete_password(con, service):
    cursor = con.execute(
        "DELETE FROM passwords WHERE service = ?",
        (service,),
    )

    con.commit()

    if cursor.rowcount:
        print(f"deleted '{service}'")
    else:
        print(f"no entry found for '{service}'")

