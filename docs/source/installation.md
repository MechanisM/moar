title: Installation
template: page.html
description: Installation of Moar


# Installation

Just do

	pip install moar

## Requirements

You need to have an image library installed. Moar ships with support for the [Python Imaging Library][pil]{:target=_blank} and [ImageMagick][imagemagick]{:target=_blank} via [wand][wand]{:target=_blank}. 


### Python Imaging Library (PIL) installation

Prerequisites:

* libjpeg
* zlib

Ubuntu 10.04 package installation:

    sudo apt-get install libjpeg8 libjpeg62-dev libfreetype6 libfreetype6-dev

Then, install the [Python Imaging Library][pil]{:target=_blank} using pip:

    pip install pil

Watch the output for messages on what support got compiled in, you at least want to see the following:

    --- JPEG support available
    --- ZLIB (PNG/ZIP) support available


### Wand installation

Prerequisites:

* ImageMagick

#### Ubuntu 12.04
    
    sudo apt-get install libmagickwand-dev
    pip install Wand

#### OSX

    brew install imagemagick
    pip install Wand


[pil]: http://www.pythonware.com/products/pil/
[imagemagick]: http://www.imagemagick.org/script/index.php
[wand]: http://styleshare.github.com/wand/

