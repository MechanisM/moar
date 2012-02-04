# -*- coding: utf-8 -*-
import moar

from .utils import *


def test_pil_crop():
    thumbnail = moar.Thumbnailer(engine=moar.engines.pil.Engine)
    source = get_source('a200x140.jpeg')

    thumb = thumbnail(source, ('crop', 50, 90))
    name = thumb.key + '.jpeg'
    assert_image(name, 'crop50x90.jpeg')
    remove_thumb(name)


def test_pil_crop_xy_px():
    thumbnail = moar.Thumbnailer(engine=moar.engines.pil.Engine)
    source = get_source('a200x140.jpeg')

    thumb = thumbnail(source, ('crop', 50, 50, 100, 20))
    name = thumb.key + '.jpeg'
    assert_image(name, 'crop50x50-100|20.jpeg')
    remove_thumb(name)


def test_pil_crop_xy_short():
    thumbnail = moar.Thumbnailer(engine=moar.engines.pil.Engine)
    source = get_source('a200x140.jpeg')

    thumb = thumbnail(source, ('crop', 50, 50, 70))
    name = thumb.key + '.jpeg'
    assert_image(name, 'crop50x50-70.jpeg')
    remove_thumb(name)


def test_pil_crop_xy_pc():
    thumbnail = moar.Thumbnailer(engine=moar.engines.pil.Engine)
    source = get_source('a200x140.jpeg')

    thumb = thumbnail(source, ('crop', 50, 50, '30%', '50%'))
    name = thumb.key + '.jpeg'
    assert_image(name, 'crop50x50-30c|50c.jpeg')
    remove_thumb(name)


def test_pil_crop_xy_center():
    thumbnail = moar.Thumbnailer(engine=moar.engines.pil.Engine)
    source = get_source('a200x140.jpeg')

    thumb = thumbnail(source, ('crop', 50, 50, 'center'))
    name = thumb.key + '.jpeg'
    assert_image(name, 'crop50x50-center.jpeg')
    remove_thumb(name)


def test_pil_crop_xy_overflow_xy():
    thumbnail = moar.Thumbnailer(engine=moar.engines.pil.Engine)
    source = get_source('a200x140.jpeg')

    thumb = thumbnail(source, ('crop', 50, 50, 190, 130))
    name = thumb.key + '.jpeg'
    assert_image(name, 'crop50x50-190|130.jpeg')
    remove_thumb(name)


def test_pil_crop_xy_overflow_wh():
    thumbnail = moar.Thumbnailer(engine=moar.engines.pil.Engine)
    source = get_source('a200x140.jpeg')

    thumb = thumbnail(source, ('crop', 500, 500))
    name = thumb.key + '.jpeg'
    assert_image(name, 'crop500x500.jpeg')
    remove_thumb(name)

