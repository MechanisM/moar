# -*- coding: utf-8 -*-
"""
# moar.storages.base

Base storage

"""


class BaseStorage(object):
    
    def get(self, thumb):
        raise NotImplementedError
    
    def save(self, thumb, data):
        raise NotImplementedError

