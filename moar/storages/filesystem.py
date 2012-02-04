# -*- coding: utf-8 -*-
"""
# moar.storages.filesystem

Local file system store.

"""
import io
import errno
import os

from .base import BaseStorage


def make_dir(path):
    try:
        os.makedirs(os.path.dirname(path))
    except (OSError), e:
        if e.errno != errno.EEXIST:
            raise
    return path


class Storage(BaseStorage):

    thumbsdir = 't'
    
    def get(self, thumb):
        """"""
        name = self.get_name(thumb.key, thumb.options)
        path = self.get_path(thumb.source, name)
        if os.path.isfile(path):
            return self.get_url(thumb.source, name)
        return None
    
    def save(self, thumb, raw_data):
        name = self.get_name(thumb.key, thumb.options)
        dest = self.get_path(thumb.source, name)
        make_dir(dest)
        with io.open(dest, 'wb') as f:
            f.write(raw_data)
        return self.get_url(thumb.source, name)
    
    def get_name(self, key, options):
        return '%s.%s' % (key, options['format'].lower())
    
    def get_path(self, source, name):
        return os.path.join(source.base_path, source.path, self.thumbsdir, name)
    
    def get_url(self, source, name):
        return '/'.join([source.base_url, source.path, self.thumbsdir, name])

