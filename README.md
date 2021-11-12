# packsbyname-python
My try to resolve ArchLinux and other archbased distributions problem to easily search for packages only by it's name. Just get 'pbname.py' and check if you have Python installed. Then launch script with 'python3' prefix or change script to executable and launch it directly. Type 'pbname.py -h' for more info.

# how to search

You can use Pacman (-p argument) or Yay (-y argument) to search in AUR too. For installed packages search use -Qs argument or for search in online repositories use -Ss argument. If only words to search are specified it will be by Pacman and in online repositories.

You can search for up to 5 words same time. Package will be displayed as a result only if it name contains all of required words.

# examples of use

'pbname.py -Qs python* pip' - to search by Pacman on computer for each package that name starts with 'python' and contains 'pip'

'pbname.py -y adwaita* *theme gtk' - to search by Yay online for each package that name starts with 'adwaita', ends with 'theme' and contains 'gtk'

'pbname.py pacman' - to search by Pacman online for each package that name contains 'pacman'

'pbname.py -y -Qs pacman list' - to search by Yay on computer for each package thet name contains 'pacman' and 'list'

# tips

To use it more easy copy script to for example /usr/bin/ directory with sudo, make it executable and then you will can use it from any directory you want like other commands. You can change it's name to for example 'pbname' for better experience too. { sudo cp ./pbname.py /usr/bin/pbname && sudo chmod +x /usr/bin/pbname }

When AUR returns error 'Too many package results' try to change searched words order.
