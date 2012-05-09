
Moar is an MIT Licensed library, written in Python, that allows you to make custom thumbnails wherever you need them.

    <img src="{{ thumbnail(source, '200x100', ('crop', 50, 50)) }}" />


See the documentation online at http://lucuma.github.com/moar/
or in _docs/source: https://github.com/lucuma/moar/docs/source/ .


Features at a glance
---------------------

* Pluggable engine support (_PIL: http://www.pythonware.com/products/pil/ and 
_GraphicsMagick: http://www.graphicsmagick.org/ included).
* Automatic cache: a thumbnail is generated only once.
* Pluggable storage support (FileSystem included).
* Flexible, simple syntax, generates no HTML.
* Several filters available by default:
    * Cropping
    * Rotation
    * Blur
    * Grayscale/Sepia
* Easily extendable.

