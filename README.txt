# VaultCLI
------------------------------------------------_
this is  a CLI password manager                 |
it uses AES-256                                 |
default location for DB ~/.vaultcli.db          |
                                                |
source code:                                    |
├── authentication.py - master password handling|
├── crypto.py - cryptography handling           |
├── database.py - sqlite handling               |
├── main.py - entry point for the program       |
└── manager.py - password manager logic         |
                                                |
arguments:                                      |
  clean - deletes the database                  |
  add <service> <username> - adds a password    |
  delete <service> - deletes a password         |
  get <service> - prints a password             |
  list - lists services                         |
                                                |
default encryption configuration:               |
PBKDF2: 600,000 iterations                      |
cipher: AES-GCM                                 |
                                                |
TODO:                                           |
it will copy and delete after two minutes       |
instead of printing it directly to the console  |
________________________________________________-
