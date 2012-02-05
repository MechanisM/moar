# -*- coding: utf-8 -*-
import io
import os

from PIL import Image


__all__ = [
    'get_cpath',
    'get_tpath',
    'get_source',
    'get_url',
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

TOLERANCE = 1


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

    test_data = list(Image.open(tp).getdata())
    control_data = list(Image.open(cp).getdata())

    equal = True
    for i in range(len(test_data)):
        if isinstance(test_data[i], int):
            if abs(test_data[i] - control_data[i]) > TOLERANCE:
                equal = False
                break
        else:
            rt, gt, bt, at = test_data[i]
            rc, gc, bc, ac = control_data[i]
            dr = abs(rt - rc) > TOLERANCE
            dg = abs(gt - gc) > TOLERANCE
            db = abs(bt - bc) > TOLERANCE
            da = abs(at - ac) > TOLERANCE
            if dr or dg or db or da:
                equal = False
                break
    
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

