# -*- coding: utf-8 -*-
"""
# moar.filters.grayscale

Examples:

```python
thumbnail(source, '200x100', ('grayscale', ) )
```
"""
from . import sepia


def get_ramp(args):
    tone = (255, 255, 255)
    return sepia.make_linear_ramp(tone)


def pil(im, *args, **options):
    # Monkey patching!
    sepia.get_ramp = get_ramp
    return sepia.pil(im, *args, **options)


def wand(im, *args, **options):
    # Monkey patching!
    sepia.get_ramp = get_ramp
    return sepia.wand(im, *args, **options)

