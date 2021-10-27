#!/usr/bin/env python3

from os import popen
from argparse import ArgumentParser

### Program help and arguments definision. ###

parser = ArgumentParser()
s = "Script using Pacman's or Yay's output to search packages only by it's names. "
s += "Python is required for scritp to work. You can launch it with ‘python3’ prefix "
s += "or you can change script's permision by making it executable and launch directly. "
s += "You can launch script only with 'name' argument. It will use 'pacman -Ss' by default."
parser.description = s
parser.usage = '[python3] pbname.py [engine] [method] name'

s = "package name or it's part to be search"
parser.add_argument('name', help=s)

group1 = parser.add_argument_group()
group1.title ='engine'
mutualgroup1 = group1.add_mutually_exclusive_group()
s = 'search by Pacman'
mutualgroup1.add_argument('-p', '--pacman', dest='by', action='store_const', const='pacman ', default='pacman ', help=s)
s = 'search by Yay'
mutualgroup1.add_argument('-y', '--yay', dest='by', action='store_const', const='yay ', help=s)

group2 = parser.add_argument_group()
group2.title ='method'
mutualgroup2 = group2.add_mutually_exclusive_group()
s = 'search each package in the sync databases for names'
mutualgroup2.add_argument('-Ss', '--remote', dest='where', action='store_const', const='-Ss ', default='-Ss ', help=s)
s = 'search each locally-installed package for names'
mutualgroup2.add_argument('-Qs', '--local', dest='where', action='store_const', const='-Qs ', help=s)

args = parser.parse_args()

### Program main part. ###

a = len(popen('yay --version').read())
b = len(popen('pacman --version').read())

if b == 0:
    print('Pacman was not detected. Application could be only used in ArchLinux and other distributions based on it.')
    exit()

if (args.by == 'yay ') and (a == 0):
    print('Yay was not detected. Use Pacman instead.')
    exit()

cmd = args.by + args.where + args.name #creating search command from arguments
out = popen(cmd).readlines() #getting output lines

blue = '\033[94m'
green = '\033[32m'
reset = '\033[0m'
i = 0
while i < len(out):
    if ((out[i].startswith('local/') or out[i].startswith('aur/') or out[i].startswith('multilib/') 
    or out[i].startswith('community/') or out[i].startswith('extra/') or out[i].startswith('core/')) 
    and (out[i].split('/')[1].split(' ')[0].find(args.name) != -1)):
        print(blue + out[i].split('/')[0] + '/' + green + out[i].split('/')[1].replace('\n', '') + reset)
        print(out[i+1].replace('\n', ''))
    i += 1
