
     _______      ______
     \                 /   ___________            _______
      \               /    |          | |            |
       \             /     |            |            |
        \           /      |            |            |
         \         /       |            |            |
          \       /        |            |            |
           \     /         |            |            |
            \   /          |            |            |
             \ /           \_________   |_______  _______

    _-----------------------------------------------------_
    |               VaultCLI password manager             |
    |                                                     |
    |it uses AES-256                                      |
    |default location for DB ~/.vaultcli.db               |
    |                                                     |
    |source code:                                         |
    |├── authentication.py - master password handling     |
    |├── crypto.py - cryptography handling                |
    |├── database.py - sqlite handling                    |
    |├── main.py - entry point for the program            |
    |└── manager.py - password manager logic              |
    |                                                     |
    |arguments:                                           |
    |  clean - deletes the database                       |
    |  add <service> <username> - adds a password         |
    |  delete <service> - deletes a password              |
    |  get <service> - prints a password                  |
    |  list - lists services                              |
    |                                                     |
    |default encryption configuration:                    |
    |PBKDF2: 600,000 iterations                           |
    |cipher: AES-GCM                                      |
    |                                                     |
    |uses getpass to take password input                  |
    |                                                     | 
    |copies passwords instead of printing, uses pyperclip |
    |with threading as a timer to deletion time which is  |
    |30 seconds                                           |
    -_____________________________________________________-
    |                    TODO                             |
    |	features I will be adding in the future will go   |
    |here. they will be pending or complete. complete     |
    |will be kept for archival purposes.                  |
    |                                                     |
    | - add clipboard handling and auto-delete using      |      
    |   pyperclip and threading = COMPLETE Thursday Sept. |
    |   17, 2026                                          |
    | - merge functionality with my password generator    |
    |   project = PENDING                                 |
    -_____________________________________________________-
    |                    Installation                     |
    |                                                     |
    |	you must use python3.                             |
    | run pip install -r requirements.txt, and I recommend|
    |using pyinstaller to make it an executable with the  |
    |flag --onefile pointed towards the main.py file.     |
    |then rename and move the file in dist to a folder on |
    |your PATH.                                           |
    -_____________________________________________________-
    |                    Author/s                         |
    |                                                     |
    |	all ascii art and code is acredited to me, there  |
    |are no current contributors.                         |
    -_____________________________________________________-
