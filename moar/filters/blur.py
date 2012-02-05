# -*- coding: utf-8 -*-
"""
# moar.filters.blur

Apply a gaussian blur (smoothing) to the image. The `radius` argument
determines the scale of fine detail that will be removed. Low values remove
only very fine detail while high values remove larger levels of detail.

Example:

```python
thumbnail(source, '200x100', ('blur', 4) )
```
"""
try:
    from PIL import ImageFilter

    class MyGaussianBlur(ImageFilter.Filter):

        name = "GaussianBlur"

        def __init__(self, radius=2):
            self.radius = radius
        
        def filter(self, image):
            return image.gaussian_blur(self.radius)
    
except ImportError:
    pass


class BlurFilter(object):
        
    def pil(self, im, *args, **options):
        radius = self.get_radius(args)
        im = im.filter(MyGaussianBlur(radius))
        return im
    
    def magick(self, im, *args, **options):
        radius = self.get_radius(args)
        im.blur(radius)
        return im
    
    def get_radius(self, args):
        return args[0]

