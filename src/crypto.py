import secrets

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


SALT_SIZE = 16
KEY_SIZE = 32
NONCE_SIZE = 12
PBKDF2_ITERATIONS = 600_000


def generate_salt():
    return secrets.token_bytes(SALT_SIZE)


def derive_key(master_password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=KEY_SIZE,
        salt=salt,
        iterations=PBKDF2_ITERATIONS,
    )

    return kdf.derive(master_password.encode("utf-8"))


def create_verifier(key):
    """
    Creates a value that lets us verify the master password
    without storing the password itself.
    """
    nonce = secrets.token_bytes(NONCE_SIZE)

    ciphertext = AESGCM(key).encrypt(
        nonce,
        b"vaultcli-verifier",
        None,
    )

    # Store nonce + ciphertext
    return nonce + ciphertext


def verify_key(key, verifier):
    try:
        nonce = verifier[:NONCE_SIZE]
        ciphertext = verifier[NONCE_SIZE:]

        plaintext = AESGCM(key).decrypt(
            nonce,
            ciphertext,
            None,
        )

        return plaintext == b"vaultcli-verifier"

    except Exception:
        return False


def encrypt(key, plaintext):
    nonce = secrets.token_bytes(NONCE_SIZE)

    ciphertext = AESGCM(key).encrypt(
        nonce,
        plaintext.encode("utf-8"),
        None,
    )

    # Store nonce + ciphertext
    return nonce + ciphertext


def decrypt(key, encrypted):
    nonce = encrypted[:NONCE_SIZE]
    ciphertext = encrypted[NONCE_SIZE:]

    plaintext = AESGCM(key).decrypt(
        nonce,
        ciphertext,
        None,
    )

    return plaintext.decode("utf-8")
