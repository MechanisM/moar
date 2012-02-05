# -*- coding: utf-8 -*-
"""
# moar.engines.pgmagick

PgMagick (a wrapper for GraphicsMagick) engine.

"""
available = True
try:
    from pgmagick import Blob, Geometry, Image
    from pgmagick import InterlaceType, OrientationType
    from pgmagick._pgmagick import get_blob_data
except ImportError:
    available = False

from .base import BaseEngine


class Engine(BaseEngine):

    name = 'magick'

    def load_image(self, path):
        return Image.open(path)
    
    def get_data(self, im, options):
        format = options['format']
        im.magick(format.encode('utf8'))
        im.quality(options['quality'])
        if format == 'JPEG' and options['progressive']:
            im.interlaceType(InterlaceType.LineInterlace)
        blob = Blob()
        im.write(blob)
        return get_blob_data(blob)
    
    def _set_orientation(self, im):
        orientation = im.orientation()
        if orientation == OrientationType.TopRightOrientation:
            im.flop()
        elif orientation == OrientationType.BottomRightOrientation:
            im.rotate(180)
        elif orientation == OrientationType.BottomLeftOrientation:
            im.flip()
        elif orientation == OrientationType.LeftTopOrientation:
            im.rotate(90)
            im.flop()
        elif orientation == OrientationType.RightTopOrientation:
            im.rotate(90)
        elif orientation == OrientationType.RightBottomOrientation:
            im.rotate(-90)
            im.flop()
        elif orientation == OrientationType.LeftBottomOrientation:
            im.rotate(-90)
        im.orientation(OrientationType.TopLeftOrientation)
        return im

    def _get_image_size(self, im):
        geometry = im.size()
        return geometry.width(), geometry.height()
    
    def _scale(self, im, width, height):
        geometry = Geometry(width, height)
        im.scale(geometry)
        return im

