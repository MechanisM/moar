# -*- coding: utf-8 -*-
"""

"""
from hashlib import md5

from . import utils
from .engines import pil
from .storages import filesystem


class EngineNotAvailable(Exception):
    pass


INSTALL_PIL_MSG = '''Moar uses by default the Python Image Library (PIL) but
we couldn't found it installed.
Please see the documentation of Moar to find how to install it or how to choose
a different engine.'''


class Thumb(object):

    def __init__(self, source, geometry, filters, options):
        self.source = source
        self.geometry = geometry
        self.filters = filters
        self.options = options

        self.url = None
        self.key = self.get_key()
    
    def get_key(self):
        l = [str(self.source), str(self.geometry), str(self.filters),
            str(self.options)]
        seed = ' '.join(l)
        return md5(seed).hexdigest()
    
    def __repr__(self):
        return self.url


class Thumbnailer(object):
    """
    engine:
        An `Engine` class. By default `moar.engines.pil.Engine`.
    
    storage:
        An `Storage` class. By default `moar.storages.filesystem.Storage`.
    
    filters:
        Dictionary of extra filters than are added to those available
        by default.
    
    upscale:
        A boolean that controls if the image can be upscaled or not.
        For example if your source is `100x100` and you request a thumbnail of
        size `200x200` and upscale is `False` this will return a thumbnail of
        size 100x100. If upscale were `True` this would result in a thumbnail
        size `200x200` (upscaled).
        The default value is `True`.

    quality:
        When the output format is jpeg, quality is a value between 0-100 that
        controls the thumbnail write quality.
        Default value is `90`.

    progressive:
        This controls whether to save jpeg thumbnails as progressive jpegs.
        Default value is `True`.

    orientation:
        This controls whether to orientate the resulting thumbnail with
        respect to the source EXIF tags for orientation.
        Default value is `True`.

    format:
        This controls the write format and thumbnail extension. Formats 
        supported by the shipped engines are `'JPEG'` and `'PNG'`. 
        Default value is `'JPEG'`.
    
    resize:
        When setting the new geometry, this controls if the image is deformed
        to match exactly the given dimensions, regardless of the aspect ratio
        of the original image. If `resize` is `True`, the `upscale` option
        is ignored.
        Default value is `False`.
    """

    def __init__(self, engine=None, storage=None, filters=None, **default_options):
        if engine is None:
            if not pil.available:
                raise EngineNotAvailable(INSTALL_PIL_MSG)
            engine = pil.Engine
        if type(engine) == type:
            engine = engine()
        self.engine = engine

        if storage is None:
            storage = filesystem.Storage
        if type(storage) == type:
            storage = storage()
        self.storage = storage;
        
        self.custom_filters = filters or {}

        self.upscale = bool(default_options.get('upscale', True))
        self.quality = int(default_options.get('quality', 90))
        self.progressive = bool(default_options.get('progressive', True))
        self.orientation = bool(default_options.get('orientation', True))
        self.format = default_options.get('format', 'JPEG').upper()
        self.resize = bool(default_options.get('resize', False))
    
    def parse_geometry(self, geometry):
        if not geometry:
            return
        
        if callable(geometry):
            geometry = geometry()
        
        geometry = geometry.split('x')

        if len(geometry) == 1:
            width = int(geometry[0])
            height = None
        else:
            w = geometry[0]
            width = int(w) if w else None
            height = int(geometry[1])
        
        return (width, height)
    
    def __call__(self, source, geometry=None, *filters, **options):
        filters = list(filters)
        
        if isinstance(source, dict):
            source = utils.StorageDict(source)
        
        # No geometry provided
        if isinstance(geometry, (tuple, list)):
            filters.insert(0, geometry)
            geometry = None
        
        geometry = self.parse_geometry(geometry)
        
        _options = {
            'upscale': bool(options.get('upscale', self.upscale)),
            'quality': int(options.get('quality', self.quality)),
            'progressive': bool(options.get('progressive', self.progressive)),
            'orientation': bool(options.get('orientation', self.orientation)),
            'format': options.get('format', self.format).upper(),
            'resize': bool(options.get('resize', self.resize)),
        }

        thumb = Thumb(source, geometry, filters, _options)
        url = self.storage.get(thumb)
        if url:
            thumb.url = url
            return thumb
        raw_data = self.engine.process(thumb, self.custom_filters)
        thumb.url = self.storage.save(thumb, raw_data)
        return thumb

