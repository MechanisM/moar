# -*- coding: utf-8 -*-
"""
# moar.filters.crop

Crop accepts a width, height and one or two optional values as the
coordinates of the new top-left corner (0,0 by default).
These last values can be integers (pixels), percentages or 'center'.

For example, some valid values are:

```python
thumbnail(source, '200x100', ('crop', 50, 50) )
thumbnail(source, '200x100', ('crop', 50, 50, '15%', '10%') )
thumbnail(source, '200x100', ('crop', 50, 50, 150, 50) )
thumbnail(source, '200x100', ('crop', 50, 50, 'center', 0) )
thumbnail(source, '200x100', ('crop', 50, 50, 'center', 'center') )
```
"""


def pil(im, *args, **options):
    imw, imh = im.size
    w, h, x, y = get_bounds(args, imw, imh)
    box = (x, y, x + w, y + h)
    return im.crop(box)


def wand(im, *args, **options):
    imw, imh = im.size
    w, h, x, y = get_bounds(args, imw, imh)
    im.crop(x, y, width=w, height=h)
    return im


def get_bounds(args, imw, imh):
    args = list(args)

    if (len(args) == 3):
        args.append(args[2])

    args.extend([0, 0])
    width = int(args[0])
    height = int(args[1])
    x = args[2]
    y = args[3]

    if not isinstance(x, basestring):
        x = int(x)
    elif x.endswith('%'):
        x = imw * int(x[:-1]) / 100
    elif x == 'center':
        x = (imw - width) / 2
    elif x.endswith('px'):
        x = int(x[:-2])
    else:
        x = int(x)

    if not isinstance(y, basestring):
        y = int(y)
    elif y.endswith('%'):
        y = imh * int(y[:-1]) / 100
    elif y == 'center':
        y = (imh - height) / 2
    elif y.endswith('px'):
        y = int(y[:-2])
    else:
        y = int(y)
    
    # Do not overflow
    if width + x > imw:
        width = imw - x
    if height + y > imh:
        height = imh - y
    
    return (width, height, x, y)

