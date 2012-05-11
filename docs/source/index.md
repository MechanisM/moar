title: Moar thumbnails documentation
template: page.html
index: 1


# Moar thumbnails

**Welcome to Moar!**

Moar is an MIT Licensed library, written in Python, that allows you to make custom thumbnails wherever you need them.

```jinja
<img src="{{ thumbnail(source, '200x100', ['crop', 50, 50]) }}" />
```


## Features at a glance

* Pluggable engine support ([PIL][pil]{:target=_blank} and [GraphicsMagick][gmi]{:target=_blank} included).
* Automatic cache: a thumbnail is generated only once.
* Pluggable storage support (FileSystem included).
* Flexible, simple syntax, generates no HTML.
* Several filters available by default:
    * Cropping
    * Rotation
    * Blur
    * Grayscale/Sepia
* Easily extendable.


[pil]: http://www.pythonware.com/products/pil/
[gmi]: http://www.graphicsmagick.org/
