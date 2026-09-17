# this file handles sqlite and nothing else
import os
import sqlite3

DB_FILE = os.path.expanduser("~/.vaultcli.db") # the file where the password database will be stored

def get_connection():
    con = sqlite3.connect(DB_FILE)
    con.execute("PRAGMA foreign_keys = ON")

    con.execute("""
        CREATE TABLE IF NOT EXISTS metadata (
            id INTEGER PRIMARY KEY CHECK (id = 1),
            salt BLOB NOT NULL,
            verifier BLOB NOT NULL
        )
    """)

    con.execute("""
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            service TEXT NOT NULL UNIQUE,
            username BLOB NOT NULL,
            password BLOB NOT NULL
        )
    """)

    # restrict perms on unix-like systems
    try:
        os.chmod(DB_FILE, 0o600)
    except OSError:
        pass

    return con

def get_metadata(con):
    return con.execute(
        "SELECT salt, verifier FROM metadata WHERE id = 1"
    ).fetchone()

def create_metadata(con, salt, verifier):
    con.execute(
        """
        INSERT INTO metadata (id, salt, verifier)
        VALUES (1, ?, ?)
        """,
        (salt, verifier),
    )
    con.commit()

