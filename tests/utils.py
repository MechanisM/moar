# -*- coding: utf-8 -*-
import io
import os

from PIL import Image, ImageChops


__all__ = [
    'get_cpath',
    'get_tpath',
    'get_source',''
    'assert_exists',
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
        'path': os.path.join(BASE_PATH, PATH, name),
        'url': '/'.join([BASE_URL, PATH, name]),
    }


def assert_image(test, control, assert_equal=True):
    tp = get_tpath(test)
    cp = get_cpath(control)

    test_image = Image.open(tp).convert('RGB')
    control_image = Image.open(cp).convert('RGB')
    try:
        diff = ImageChops.difference(test_image, control_image).getbbox()
        print diff
        equal = (diff is None)
    except ValueError, e:
        print e
        equal = False
    
    if assert_equal:
        assert equal
    else:
        assert not equal


def assert_size(name, width=None, height=None):
    tpath = get_tpath(name)
    im = Image.open(tpath)
    w, h = im.size
    if width:
        assert w == width
    if height:
        assert h == height


def assert_exists(name):
    tpath = get_tpath(name)
    assert os.path.exists(tpath)


def remove_thumb(name):
    path = get_tpath(name)
    os.remove(path)

