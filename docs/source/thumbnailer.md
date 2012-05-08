title: Thumbnailer class
template: post.html


# Thumbnailer class

Syntax:

```python
from moar import Thumbnailer

thumbnail = Thumbnailer([engine], [storage],
                [filters=extra_filters], [**default_options])
```

Moar come with support for pluggable engines and storages. By default it use `moar.engines.pil.Engine` and `moar.storages.filesystem.Storage`.

When you call the thumbnail instance, the current storage class will generates a key that represent a thumbnail made from that image with that specific filters and options. If a thumbnail with that key hasn't been generated before, it'll make a new one, store it using the key as an id, and returns it.

The default storage class (`moar.storages.filesystem.Storage`) store the generated thumbnails inside a `thumbs` folder in the same path as the source image. Other storages will operate different, for example, storing the key in a local database and uploading the thumbnail to a remote server.


## Filters

You can use the `filters` parameter to define a list of custom filters, adding them to those included by default. E.g.:

```python
from image_filters import watermak, enhace

thumbnail = Thumbnailer(filters=[watermak, enhace])
```

<div class=note markdown=1>
The filters has to have a method named after the current engine (eg: `wandº` or `pil`) or the'll be unusable. See the "[extending the library](extending.md#filters)" section for more details.
</div>

## Default Options

These options are the default for all thumbnails. However, they can be overwritten in individual `thumbnail` calls.

upscale
:   Upscale is a boolean that controls if the image can be upscaled or not. For example if your source is `100x100` and you request a thumbnail of size `200x200` and upscale is `False` this will return a thumbnail of size 100x100. If upscale were `True` this would result in a thumbnail size `200x200` (upscaled). The default value is `True`.

quality
:   When the output format is jpeg, quality is a value between 0-100 that controls the thumbnail write quality. Default value is `90`.

progressive
:   This controls whether to save jpeg thumbnails as progressive jpegs. Default value is `True`.

orientation
:   This controls whether to orientate the resulting thumbnail with respect to the source EXIF tags for orientation. Default value is `True`.

format
:   This controls the write format and thumbnail extension. Formats supported by the shipped engines are `'JPEG'` and `'PNG'`. Default value is `'JPEG'`.

resize
:   When setting the new geometry, this controls if the image is deformed to match exactly the given dimensions, regardless of the aspect ratio of the original image. If `resize` is `True`, the `upscale` option is ignored. Default value is `False`.

