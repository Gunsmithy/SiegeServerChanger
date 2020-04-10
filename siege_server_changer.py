from pathlib import Path
from uuid import UUID
import configparser
import sys
import argparse

SECTION_NAME = 'ONLINE'
OPTION_NAME = 'DataCenterHint'
DATA_CENTRES = {
    'default': 'Default (Ping-based)',
    'eastus': 'US (East)',
    'centralus': 'US (Central)',
    'southcentralus': 'US (South Central)',
    'westus': 'US (West)',
    'brazilsouth': 'Brazil (South)',
    'northeurope': 'Europe (North)',
    'westeurope': 'Europe (West)',
    'southafricanorth': 'South Africa (North)',
    'eastasia': 'Asia (East)',
    'southeastasia': 'Asia (South East)',
    'australiaeast': 'Australia (East)',
    'australiasoutheast': 'Australia (South East)',
    'japanwest': 'Japan (West)',
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


def args_config():
    parser = argparse.ArgumentParser(description='Change R6:Siege servers/data-centre in your config file.')
    parser.add_argument('--account', dest='account', help='The account UUID for which you want to change servers. '
                                                          'Assumed to be all accounts found locally if not provided.')
    parser.add_argument('--server', dest='server', help='The server/data-centre you wish to use. Assumed to be '
                                                        'default/ping-based if not provided.')
    args = parser.parse_args()

    if args.account is not None:
        print('Using --account command-line argument...')
        account = args.account
    else:
        account = None

    if args.server is not None:
        print('Using --server command-line argument...')
        server = args.server
    else:
        server = None

    return account, server


def check_account(account_input):
    accounts = []
    if account_input and account_input != "":
        try:
            UUID(account_input)
        except ValueError:
            print("Invalid account ID provided. Please confirm your entry and try again.")
            sys.exit(2)

        read_config(account_input)
        accounts.append(account_input)
    else:
        print("No account provided. Assuming all accounts...")
        accounts = find_accounts()

    return accounts


def check_server(server_input):
    if server_input == "" or server_input is None:
        print("No server provided. Assuming default/ping-based...")
        server_output = "default"
    else:
        if not DATA_CENTRES.get(server_input):
            print("Invalid data centre provided. Please confirm your entry and try again.")
            sys.exit(2)
        else:
            server_output = server_input

    return server_output


def prompt():
    print("Input the account for which you would like to change the data centre.")
    print("Provide the account ID which can be found in the URL of its R6Tab profile.")
    print("Alternatively, input nothing to default to changing the server for all accounts found on this machine.")
    account_input = input("Account UUID: ").strip()

    print("\nInput the server/data centre you would like to use.")
    print("This can be one of the following:", ", ".join(DATA_CENTRES))
    print("Alternatively, input nothing to default to setting the server back to default (Ping-based).")
    server_input = input("Server: ").strip()

    return account_input, server_input


def main(accounts, server):
    for account in accounts:
        set_config(account, server)


if __name__ == "__main__":
    config_account, config_server = args_config()
    if config_account or config_server:
        input_accounts = check_account(config_account)
        input_server = check_server(config_server)
    else:
        prompted_account, prompted_server = prompt()
        input_accounts = check_account(prompted_account)
        input_server = check_server(prompted_server)

    main(input_accounts, input_server)
