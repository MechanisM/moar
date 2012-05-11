title: Moar thumbnails documentation
template: page.html
index: 1


# Moar thumbnails

**Welcome to Moar!**

Moar is an MIT Licensed library, written in Python, that allows you to make custom thumbnails whenever you need them in your application.

```jinja
<img src="{{ thumbnail(source, '200x100', ['crop', 50, 50]) }}" />
```


## Features at a glance

* Pluggable engine support ([PIL][pil]{:target=_blank} and [GraphicsMagick][gmi]{:target=_blank} included<sup>*</sup>).
* Automatic cache: a thumbnail is generated only once.
* Pluggable storage support (FileSystem included).
* Flexible, simple syntax, generates no HTML.
* Auto-rotates the image according to its EXIF information. <sup>*</sup>
* Several filters available by default:
    * Cropping
    * Rotation <sup>*</sup>
    * Blur <sup>*</sup>
    * Grayscale/Sepia <sup>*</sup>
* Easily extendable.


[pil]: http://www.pythonware.com/products/pil/
[gmi]: http://www.graphicsmagick.org/

<div class="warning" markdown="1">
<sup>*</sup> Currently the support for GraphicsMagick is limited to resizing and/or cropping.
</div>