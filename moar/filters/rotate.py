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


class RotateFilter(object):

    def pil(self, im, *args, **options):
        angle = self.get_angle(args)
        im = im.convert('RGBA')
        im = im.rotate(angle, resample=Image.BICUBIC, expand=True)

        if options.get('format') != 'PNG':
            # a white image same size as rotated image
            fff = Image.new('RGB', im.size, (255,)*3)
            # create a composite image using the alpha layer of im as a mask
            im = Image.composite(im, fff, im)
        
        return im
    
    def magick(self, im, *args, **options):
        angle = self.get_angle(args)
        # background = None
        # if options.get('format') != 'PNG':
        #     background = Color('#fff')
        im.rotate(angle)
        return im
    
    def get_angle(self, args):
        return args[0]

