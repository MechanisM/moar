# -*- coding: utf-8 -*-
"""
# moar.storages.filesystem

Local file system store.

"""
import errno
import io
import os
import urlparse


def make_dirs(path):
    try:
        os.makedirs(os.path.dirname(path))
    except (OSError), e:
        if e.errno != errno.EEXIST:
            raise
    return path


class Storage(object):

    def __init__(self, thumbsdir='t'):
        self.thumbsdir = thumbsdir
    
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
        make_dirs(dest)
        with io.open(dest, 'wb') as f:
            f.write(raw_data)
        return self.get_url(thumb.source, name)
    
    def get_name(self, key, options):
        return '%s.%s' % (key, options['format'].lower())
    
    def get_path(self, source, name):
        path = os.path.dirname(source.path)

        # Thumbsdir could be a callable
        # In that case, the path is built on the fly, based on the thumbs name
        thumbsdir = self.thumbsdir
        if callable(self.thumbsdir):
            thumbsdir = self.thumbsdir(name)

        return os.path.join(path, thumbsdir, name)
    
    def get_url(self, source, name):
        parsed = urlparse.urlsplit(source.url)
        path, _ = parsed.path.rsplit('/', 1)
        new_path = '/'.join([path, self.thumbsdir, name])
        new_parsed = (parsed.scheme, parsed.netloc, new_path, parsed.query,
            parsed.fragment)
        return urlparse.urlunsplit(new_parsed)

