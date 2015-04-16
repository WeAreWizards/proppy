# proppy
A proposal generator

TODO: lots of things

## Installing with pip
You will need to use a version of wkhtmltopdf containing the patched qt.  
For example the default in pacman won't include that but you can 
install it from AUR, package name is wkhtmltopdf-static.  

$ pip install -r requirements.txt

## Installing with nix
$ nix-env  -f build.nix -i python3.4-proppy-0.01
