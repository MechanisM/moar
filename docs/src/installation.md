title: Installation
base: page.html
description: Requirements for MoarThumbnails

# Installation

Just do

	pip install moar

## Requirements

You need to have an image library installed. MoarThumbnails ships with support for the [Python Imaging Library][pil] and [GraphicsMagick][gmi] via [pgmagick][pgmagick]. 

The GraphicsMagick based engine `moar.engines.imagemagick.Engine` by default calls `convert` and `identify` shell commands. You can change the
paths to these tools by passing the optional parameters `convert` and `identify` respectively, to the constructor. See [Thumbnailer options](thumbnailer.html) for more details.

### Python Imaging Library installation

Prerequisites:

* libjpeg
* zlib

Ubuntu 10.04 package installation:

    sudo apt-get install libjpeg62 libjpeg62-dev zlib1g-dev

Installing the [Python Imaging Library][pil] using pip:

    pip install PIL

Watch the output for messages on what support got compiled in, you at least want to see the following:

    --- JPEG support available
    --- ZLIB (PNG/ZIP) support available

### GraphicsMagick installation

Ubuntu 10.04 package installation:

    sudo apt-get install graphicsmagick

OSX installation with Homebrew:

    brew install --use-clang --HEAD graphicsmagick

### pgmagick installation

Prerequisites:

* GraphicsMagick
* Boost.Python

Ubuntu 10.04 prerequisites installation:

    sudo apt-get install libgraphicsmagick++-dev
    sudo apt-get install libboost-python1.40-dev

OSX installation of prerequisites with Homebrew:
    
    brew install boost

Installing pgmagick using pip:

    pip install pgmagick


[pil]: http://www.pythonware.com/products/pil/
[gmi]: http://imagemagick.com/
[pgmagick]: http://bitbucket.org/hhatto/pgmagick/src

