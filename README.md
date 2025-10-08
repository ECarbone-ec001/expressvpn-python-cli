## ExpressVPN - Python Wrapper (LINUX) CLI Version

**This fork supports cli version of Express VPN** 

This software is a modified version of the original developed by [Philip Remy](https://www.expressvpn.com/vpn-download/vpn-linux) .
It is adapted to works with current version of Express VPN for linux, in particular with CLI version.

Full bash documentation: [https://www.expressvpn.com/support/vpn-setup/app-for-linux-cli/](https://www.expressvpn.com/support/vpn-setup/app-for-linux-cli/)

This will not work on Windows!

## Installation with PyPI

If the command `expressvpn` is already installed on your Ubuntu then just run this:

```bash
pip install expressvpn-python-cli
```

## Download/Install the package on the official website

Refer to official site to download the official linux release:
[https://www.expressvpn.com/vpn-download/vpn-linux](https://www.expressvpn.com/vpn-download/vpn-linux)

## Change your public IP every x seconds

Check the script: [vpn.sh](vpn.sh).

## Set up expressvpn

You can find your activation key here: [https://www.expressvpn.com/setup](https://www.expressvpn.com/setup).

```bash
echo '[your activation code]' > activationCodeFile
expressvpnctl login activationCodeFile 
```

You can help improve ExpressVPN by sharing anonymized diagnostic reports. Enter Y to accept or n to decline.

After login and to logout, simply run:

```bash
expressvpnctl logout
```

NOTE that you will have to activate `expressvpn` again if you logout.
NOTE To use connection commands in the CLI, either the ExpressVPN GUI client must be running, or background mode must be enabled.

## Python bindings

### Set Background mode enabled

Bash

```bash
    expressvpnctl background enable
```

Python

```python
from expressvpn import enable_background
enable_background()
```

### Connect

Bash

```bash
expressvpnctl connect
```

Python

```python
from expressvpn import connect
connect()
```

### Connect with alias

Bash

```bash
expressvpnctl connect "[ALIAS]"
```

Python

```python
from expressvpn import connect_alias
connect_alias(alias: str)
```

### Random connect(From fastest servers)

Python

```python
from expressvpn.wrapper import random_connect
random_connect()
```

### Random connect(From all servers)

Python

```python
from expressvpn.wrapper import random_connect
random_connect(True)
```

### 

### Disconnect

Bash

```bash
expressvpnctl disconnect
```

Python

```python
from expressvpn import disconnect
disconnect()
```

## IP auto switching

Sometimes websites like Amazon or Google will ban you after too many requests. It's easy to detect because your script will fail for some obscure reason. Most of the time, if the HTML contains the word captcha or if the websites returns 403, it means that you probably got banned. But don't panic, you can use a VPN coupled with IP auto switching. Here's an example of a scraper doing IP auto switching:

```python
import logging

from expressvpn import wrapper


class BannedException(Exception):
    pass


def main():
    enable_background()
    while True:
        try:
            scrape()
        except BannedException as be:
            logging.info('BANNED EXCEPTION in __MAIN__')
            logging.info(be)
            logging.info('Lets change our PUBLIC IP GUYS!')
            change_ip()
        except Exception as e:
            logging.error('Exception raised.')
            logging.error(e)


def change_ip():
    max_attempts = 10
    attempts = 0
    while True:
        attempts += 1
        try:
            logging.info('GETTING NEW IP')
            wrapper.random_connect()
            logging.info('SUCCESS')
            return
        except Exception as e:
            if attempts > max_attempts:
                logging.error('Max attempts reached for VPN. Check its configuration.')
                logging.error('Browse https://github.com/philipperemy/expressvpn-python.')
                logging.error('Program will exit.')
                exit(1)
            logging.error(e)
            logging.error('Skipping exception.')
```
