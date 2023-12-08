#!/usr/bin/env python
import sys
import webbrowser
from colorama import Fore, Style

search = ''

if len(sys.argv) < 2:
    print(Fore.RED + "Too few arguments" + Style.RESET_ALL)
    sys.exit(1)

for item in sys.argv[1:]:
    search += f'{item} '

search.replace(" ", '%20')

webbrowser.open(f'https://google.com/search?q={search[:-1]}+site:reddit.com+OR+site:stackoverflow.com+OR+site:www.geeksforgeeks.org+OR+site:www.w3schools.com')