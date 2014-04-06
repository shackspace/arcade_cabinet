# Wahcade 
Wahcade is a somewhat still supported mame arcade cabinet chooser.

# Installation

WARNING: you need at least 4 GB ram (or ram + swap = 4GB) in order to build a
complete list of your games for the game chooser! 

Wahcade is Frickelsoftware(tm).

## Arch Linux

    # you need an up-to-date system but we need a custom kernel
    pacman -Syu --ignore linux\*
    # wahcade pure is unmaintained since 2009
    yaourt -S wahcade-bzr


# Configuration
## Important stuff
### Refreshing games

	ssh -X shack@kabinett wahcade-setup
	'Mame Only' -> 'Setup Filters' -> 'Generate' -> 'wait forever'


## catver.ini
Contains a Category for all the mame roms

    cd ~/.mame
    wget http://www.progettoemma.net/public/ccount/click.php?id=6 -O cv.zip
    unzip cv.zip
    mv catveren/Catver.ini catver.ini

## media files

google "mame artwork" or grab a torrent, extract to ~/.mame

# Setup

start `wahcade-setup`

## Wah!Cade

- Layout: for us it was something_640x480

## Keys

- Tick "Joystick"
- Edit "LAUNCH_GAME", add one of the joystick buttons to it (IMPORTANT)
    without it you will not start anything

## Emulators

- Application: /usr/bin/sdlmame
- List Generation: Rom Dir: ~/.mame/roms
        Method: XML File
- Artwork:
    With the default layout only Artwork #1 is visible,
    choose the media folder with game screenshots or preview or something:
    Artwork #1: ~/.mame/artwork (or ~/.mame/title/)

## MAME Only

- XML: Default
- Category /Version File: ~/.mame/catver.ini

Press the "Reload Button (two arrows in a circle)". This may take some time
Now Press "Setup Filters", this will need forever and requires buttloads of
RAM, 4 GB at least in total (ram + swap). This was a mayor caveat for me, as
"Emulators -> List Generation -> Method: Rom Directory" did nothing for me.

It always resulted in:

    Traceback (most recent call last):
    File "/usr/share/wahcade/win_filter.py", line 245, in on_cboLists_changed
    self.load_filter()
    File "/usr/share/wahcade/win_filter.py", line 275, in load_filter
    if self.current_filter[fk[0]] == str(idx):
    KeyError: 'filter_type'

switching back to "Emulators -> List Generation -> Method: XML" resolved the
issue but requires >4gb ram.

### Add swap

    # a lot of people use dd to fill a file with zeros but these are noobs,
    # cool dudes use :
    truncate --size 8G /swapfile
    mkswap /swapfile
    swapon /swapon
    echo "/swapfile     none swap defaults 0 0" >> /etc/fstab

After finishing, close the setup.

# Playing:
now you can run `wahcade`
