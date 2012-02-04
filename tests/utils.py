# -*- coding: utf-8 -*-
import io
import os

from PIL import Image


__all__ = [
    'get_cpath',
    'get_tpath',
    'get_source',
    'get_url',
    'assert_image',
    'assert_size',
    'remove_thumb',
]


BASE_PATH = os.path.dirname(__file__)
BASE_URL = '/media'
PATH = 'res'

THUMBSDIR = 't'
CONTROLDIR = 'c'


def get_cpath(name):
    return os.path.join(BASE_PATH, PATH, CONTROLDIR, name)


def get_tpath(name):
    return os.path.join(BASE_PATH, PATH, THUMBSDIR, name)


def get_source(name):
    return {
        'base_path': BASE_PATH,
        'base_url': BASE_URL,
        'path': PATH,
        'name': name,
    }


def get_url(name):
    return '/'.join([BASE_URL, PATH, THUMBSDIR, name])


def assert_image(test, control, assert_equal=True):
    tp = get_tpath(test)
    cp = get_cpath(control)

    with io.open(tp, 'rb') as f:
        test_data = f.read()
    with io.open(cp, 'rb') as f:
        control_data = f.read()
    
    if assert_equal:
        assert test_data == control_data
    else:
        assert test_data != control_data


def assert_size(name, width=None, height=None):
    tpath = get_tpath(name)
    im = Image.open(tpath)
    w, h = im.size
    if width:
        assert w == width
    if height:
        assert h == height


def remove_thumb(name):
    path = get_tpath(name)
    os.remove(path)

