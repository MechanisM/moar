# -*- coding: utf-8 -*-
"""
moar.utils
"""


class StorageDict(dict):
    """A StorageDict object is like a dictionary except `obj.key` can be used
    in addition to `obj['key']`.
    
    Basic Usage:
    
        >>> o = StorageDict(a=1)
        >>> o.a
        1
        >>> o['a']
        1
        >>> o.a = 2
        >>> o['a']
        2
        >>> del o.a
        >>> print o.a
        None
    
    """
    def __init__(self, dd=None, _default_value=None, _case_insensitive=False,
            **kwargs):
        data = dd if dd else kwargs
        self.__dict__['_default_value'] = _default_value
        self.__dict__['_case_insensitive'] = _case_insensitive
        if _case_insensitive:
            dict.__init__(self, [(k.upper(), v) for k, v in data.items()])
        else:
            dict.__init__(self, **data)
    
    def __getattr__(self, key):
        if self._case_insensitive:
            key = key.upper()
        try:
            return self[key]
        except KeyError, error:
            if self._default_value is not None:
                return self._default_value
            else:
                raise AttributeError(error)
    
    def __setattr__(self, key, value):
        if self._case_insensitive:
            key = key.upper()
        self[key] = value
    
    def __delattr__(self, key):
        if self._case_insensitive:
            key = key.upper()
        try:
            del self[key]
        except KeyError, error:
            raise AttributeError(error)
    
    def __getstate__(self):
        return dict(self)
    
    def __setstate__(self, value):
        if self._case_insensitive:
            key = key.upper()
        for (key, value) in value.items():
            self[key] = value
        
    def __repr__(self):
        return '<StorageDict ' + dict.__repr__(self) + '>'

