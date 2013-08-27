# Install Ubuntu
- add mame user
# install lightdm 
## configure autologin
# install blackbox
    
    echo "exec blackbox" > /home/<mameuser>/.xinitrc

# Install Mame Things

    # you want the newest mame version
    add-apt-repository ppa:c.falco/mame
    # install qmc2
    sudo add-apt-repository ppa:mmbossoni-gmail/emu
    sudo apt-get update
    sudo apt-get install mame qmc2-sdlmame qmc2-arcade qchdman

# create a filtered list for qmc2-arcade

    qmc2-sdlmame
    # Tools -> Front End -> Game list -> Untick Show Device Sets; Untick Show Rom Sets
    
    # Display -> QMC2 Arcade -> Game list filter -> Use filtered list
    ## -> click Export!

# grab the previews from http://qmc2.arcadehits.net/wordpress/download/

    for i in \[0-9\] a b c d e f g h i j k l m n o p q r s t u v w x y z; do wget http://qmc2.arcadehits.net/previews/${i}.zip ; done
    for i in `ls -1 *.zip`; do unzip $i; rm $i; done

