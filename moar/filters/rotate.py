# -*- coding: utf-8 -*-
"""
# moar.filters.rotate

Rotates the image counter-clockwise by a specified number of degrees.
If degrees is negative, the rotation it's clockwise instead.

Example:

```python
thumbnail(source, '200x100', ('rotate', 45) )
thumbnail(source, '200x100', ('rotate', -90) )
```
"""
try:
    from PIL import Image
except ImportError:
    pass
try:
    from wand.color import Color
except ImportError:
    pass


def pil(im, *args, **options):
    angle = args[0]
    im = im.convert('RGBA')
    im = im.rotate(angle, resample=Image.BICUBIC,
        expand=True)

    if options.get('format') != 'PNG':
        # a white image same size as rotated image
        fff = Image.new('RGB', im.size, (255,)*3)
        # create a composite image using the alpha
        # layer of im as a mask
        im = Image.composite(im, fff, im)
    
    return im


def wand(im, *args, **options):
    angle = - args[0]
    background = None
    with Color('#fff') as white:
        if options.get('format') != 'PNG':
            background = white
        im.rotate(angle, background=background, reset_coords=True)
    return im

