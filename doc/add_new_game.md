# Adding a new game

## Fast track
    # google your game, find the short name:
    # e.g. Super Street Fighter II Turbo -> ssf2t
    ../bin/copy-rom  ssf2t

### copy-rom

Output:
    ./copy-rom mwalk
        Getting roms/mwalk.zip      :           [Success]
        Getting preview/mwalk.png   :           [Success]
        Getting artwork/mwalk.zip   : 
        #####################################################                     74.5%

## manual way

    # Download game, make sure that it is the current mame version :
    #    sdlmame -help |head -n 1
    mv ssf2t.zip ~/.mame/roms
    # grab artwork
    cp ssf2t.png ~/.mame/title 
    # etc etc
