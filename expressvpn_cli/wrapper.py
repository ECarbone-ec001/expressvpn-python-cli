import random
import subprocess

from expressvpn_cli.commands import *


class ConnectException(Exception):
    pass


def run_command(command):
    p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    return list([str(v).replace('\\t', ' ').replace('\\n', ' ').replace('b\'', '').replace('\'', '')
                .replace('b"', '')
                 for v in iter(p.stdout.readline, b'')])

def background_enabled():
    return run_command(VPN_BACKGROUND_ENABLED)

def activation_check():
    print('Checking if the client is activated... (Please wait)')
    out = check_status()
    if not is_activated(out):
        print('Please follow instructions to activate using your activation key. Program will exit.')
        exit(1)
    print('Client is successfully logged in.')
    disconnect()

def check_status():
    print('Checking client status... (Please wait)')
    return run_command(VPN_STATUS)

def connect():
    return run_command(VPN_CONNECT)


def disconnect():
    return run_command(VPN_DISCONNECT)


def is_activated(connect_output):
    return not check_if_string_is_in_output(connect_output, 'Not logged in.')


def check_if_string_is_in_output(out, string):
    for item in out:
        if string in item:
            return True
    return False


def print_output(out):
    for o in out:
        print('{}'.format(o))


def connect_alias(alias):
    command = VPN_CONNECT + ' "' + str(alias)+'"'
    run_command(command)
    out = check_status()
    if not check_if_string_is_in_output(out, 'Connected to '+alias):
        raise ConnectException()
    if check_if_string_is_in_output(out, 'not region match found'):
        raise ConnectException()
    print('Successfully connected to {}'.format(alias))

def random_connect(useAllLocations = False):
    # activation_check()
    disconnect()
    vpn_list =run_command(VPN_REGIONS) if useAllLocations else run_command(VPN_CURRENT)
    print_output(vpn_list)
    aliases = vpn_list
    random.shuffle(aliases)
    selected_alias = aliases[0]
    print('Selected alias : {}'.format(selected_alias))
    connect_alias(selected_alias)  # might raise a ConnectException.
