from pathlib import Path
from uuid import UUID
import configparser
import sys

SECTION_NAME = 'ONLINE'
OPTION_NAME = 'DataCenterHint'
DATA_CENTRES = {
    'default': 'ping based',
    'eus': 'us east',
    'cus': 'us central',
    'scus': 'us south central',
    'wus': 'us west',
    'sbr': 'brazil south',
    'neu': 'europe north',
    'weu': 'europe west',
    'eas': 'asia east',
    'seas': 'asia south east',
    'eau': 'australia east',
    'wja': 'japan west',
}


def find_accounts():
    accounts = []
    r6_path = Path(Path.home(), 'Documents', 'My Games', 'Rainbow Six - Siege')
    r6_dirs = [x for x in r6_path.iterdir() if x.is_dir()]

    for account_dir in r6_dirs:
        try:
            UUID(account_dir.parts[-1])
            accounts.append(account_dir.parts[-1])
        except ValueError:
            pass

    return accounts


def read_config(account_uuid):
    config_path = Path(Path.home(), 'Documents', 'My Games', 'Rainbow Six - Siege', account_uuid, 'GameSettings.ini')
    config = configparser.ConfigParser()
    config.read_file(open(config_path))

    print("Server for", account_uuid, "is currently set to", config.get(SECTION_NAME, OPTION_NAME))


def set_config(account_uuid, server):
    config_path = Path(Path.home(), 'Documents', 'My Games', 'Rainbow Six - Siege', account_uuid, 'GameSettings.ini')
    config = configparser.ConfigParser()
    config.read_file(open(config_path))
    config.set(SECTION_NAME, OPTION_NAME, server)

    with open(config_path, 'w') as configfile:
        config.write(configfile)

    print("Server for", account_uuid, "has been set to", server)


def main():
    print("Input the account for which you would like to change the data centre.")
    print("Provide the account ID which can be found in the URL of its R6Tab profile.")
    print("Alternatively, input nothing to default to changing the server for all accounts found on this machine.")
    account_input = input("Account UUID: ").strip()

    accounts = []
    if account_input != "":
        try:
            UUID(account_input)
        except ValueError:
            print("Invalid account ID provided. Please confirm your entry and try again.")
            sys.exit(2)

        read_config(account_input)
        accounts.append(account_input)
    else:
        accounts = find_accounts()

    print("\nInput the server/data centre you would like to use.")
    print("This can be one of the following:", ", ".join(DATA_CENTRES))
    print("Alternatively, input nothing to default to setting the server back to default (Ping-based).")
    server_input = input("Server: ").strip()

    if server_input == "":
        server_input = "default"
    else:
        if not DATA_CENTRES.get(server_input):
            print("Invalid data centre provided. Please confirm your entry and try again.")
            sys.exit(2)

    for account in accounts:
        set_config(account, server_input)


if __name__ == "__main__":
    main()
