title: Installation
template: page.html
description: Installation of Moar


# Installation

Just do

	pip install moar

## Requirements

You need to have an image library installed. Moar ships with support for the [Python Imaging Library][pil]{:target=_blank} and [GraphicsMagick][gmi]{:target=_blank} via [Wand][wand]{:target=_blank}. 


### Python Imaging Library installation

Prerequisites:

* libjpeg
* zlib

Ubuntu 10.04 package installation:

    sudo apt-get install libjpeg8 libjpeg62-dev libfreetype6 libfreetype6-dev

Then, install the [Python Imaging Library][pil]{:target=_blank} using pip:

    pip install pillow

Watch the output for messages on what support got compiled in, you at least want to see the following:

    --- JPEG support available
    --- ZLIB (PNG/ZIP) support available


### Wand installation

Prerequisites:

* GraphicsMagick

Ubuntu 10.04 prerequisites installation:
    
    sudo apt-get install graphicsmagick libgraphicsmagick++-dev

OSX installation of prerequisites with Homebrew:
    
    brew install graphicsmagick

Then, install Wand using pip:

    pip install wand


[pil]: http://www.pythonware.com/products/pil/
[gmi]: http://www.graphicsmagick.org/
[wand]: http://styleshare.github.com/wand/

