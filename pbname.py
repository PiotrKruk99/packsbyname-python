#!/usr/bin/env python3

from os import popen
from argparse import ArgumentParser

pacmanPrefix = 'pacman '
yayPrefix = 'yay '
paruPrefix = 'paru '

### Program help and arguments definision. ###

parser = ArgumentParser()
s = "Script using Pacman's, Yay's or Paru's output to search packages only by it's names. "
s += "Python is required for script to work. You can launch it with ‘python3’ prefix "
s += "or you can change script's permision by making it executable and launch directly. "
s += "You can launch script only with 'name' argument, it will use 'pacman -Ss' by default. "
s += "For advanced search put ‘*’ character on pattern back [name*] to search only packages "
s += "which names start with pattern or on pattern front [*name] to search only that which "
s += "names end with pattern. You can use up to 5 words to be search. Package will be displayed "
s += "only when it's name contains all of these words. You can use '*' in any of these words."
parser.description = s
parser.usage = '[python3] pbname.py [engine] [method] name [name ...]'

s = "package name or it's part to be search [additional words to be search]"
parser.add_argument('name', nargs='+', help=s)

s = "no colored output"
parser.add_argument('--nocolors', action='store_true', help=s)

group1 = parser.add_argument_group()
group1.title = 'engine'
mutualgroup1 = group1.add_mutually_exclusive_group()
s = 'search by Pacman'
mutualgroup1.add_argument('-p', '--pacman', dest='by',
                          action='store_const', const=pacmanPrefix, default=pacmanPrefix, help=s)
s = 'search by Yay'
mutualgroup1.add_argument('-y', '--yay', dest='by',
                          action='store_const', const=yayPrefix, help=s)

s = 'search by Paru'
mutualgroup1.add_argument('-r', '--paru', dest='by',
                          action='store_const', const=paruPrefix, help=s)

group2 = parser.add_argument_group()
group2.title = 'method'
mutualgroup2 = group2.add_mutually_exclusive_group()
s = 'search each package in the sync databases for names'
mutualgroup2.add_argument('-Ss', '--remote', dest='where',
                          action='store_const', const='-Ss ', default='-Ss ', help=s)
s = 'search each locally-installed package for names'
mutualgroup2.add_argument('-Qs', '--local', dest='where',
                          action='store_const', const='-Qs ', help=s)

args = parser.parse_args()


### Program main part. ###


def checkNames():  # part of search algorithm
    for n in args.name:
        if out[i].split('/')[1].split(' ')[0].find(n.replace('*', '')) == -1:
            return False
        else:
            if n.startswith('*') and not out[i].split('/')[1].split(' ')[0].endswith(n.replace('*', '')):
                return False
            else:
                if n.endswith('*') and not out[i].split('/')[1].split(' ')[0].startswith(n.replace('*', '')):
                    return False
    return True

yayCheck = 0
if args.by == yayPrefix:
    yayCheck = len(popen('yay --version').read())

paruCheck = 0
if args.by == paruPrefix:
    paruCheck = len(popen('paru --version').read())

pacmanCheck = len(popen('pacman --version').read())

if pacmanCheck == 0:
    print('Pacman was not detected. Application could be only used in ArchLinux and other distributions based on it.')
    exit()

if (args.by == yayPrefix) and (yayCheck == 0):
    print('Yay was not detected. Use Pacman or Paru instead.')
    exit()

if (args.by == paruPrefix) and (paruCheck == 0):
    print('Paru was not detected. Use Pacman or Yay instead.')
    exit()

if len(args.name) > 5:
    print('Too many arguments to be search.')
    exit()

# creating search command from arguments
cmd = args.by + args.where + args.name[0].replace('*', '')
out = popen(cmd).readlines()  # getting output lines

if not args.nocolors:
    blue = '\033[94m'
    green = '\033[32m'
    reset = '\033[0m'
else:
    blue = ''
    green = ''
    reset = ''

i = 0
while i < len(out):
    if ((out[i].startswith('local/') or out[i].startswith('aur/') or out[i].startswith('multilib/')
         or out[i].startswith('community/') or out[i].startswith('extra/') or out[i].startswith('core/'))
            and checkNames()):
        print(blue + out[i].split('/')[0] + '/' + green +
              out[i].split('/')[1].replace('\n', '') + reset)
        print(out[i+1].replace('\n', ''))
    i += 1
