# -*- coding: utf-8 -*-
import moar

from .utils import *


def test_pil_blur():
    thumbnail = moar.Thumbnailer(engine=moar.engines.pil.Engine)
    source = get_source('a200x140.jpeg')

    thumb = thumbnail(source, ('blur', 20))
    name = thumb.key + '.jpeg'
    assert_image(name, 'blur20pil.jpeg')
    remove_thumb(name)


def test_pil_rotate_ccw():
    thumbnail = moar.Thumbnailer(engine=moar.engines.pil.Engine)
    source = get_source('a200x140.jpeg')

    thumb = thumbnail(source, ('rotate', 60))
    name = thumb.key + '.jpeg'
    assert_image(name, 'rotate60ccw.jpeg')
    remove_thumb(name)


def test_pil_rotate_cw():
    thumbnail = moar.Thumbnailer(engine=moar.engines.pil.Engine)
    source = get_source('a200x140.jpeg')

    thumb = thumbnail(source, ('rotate', -60))
    name = thumb.key + '.jpeg'
    assert_image(name, 'rotate60cw.jpeg')
    remove_thumb(name)


def test_pil_rotate_alpha():
    thumbnail = moar.Thumbnailer(engine=moar.engines.pil.Engine)
    source = get_source('a200x140.jpeg')

    thumb = thumbnail(source, ('rotate', 60), format='PNG')
    name = thumb.key + '.png'
    assert_image(name, 'rotate60alpha.png')
    remove_thumb(name)


def test_pil_filters_comp():
    thumbnail = moar.Thumbnailer(engine=moar.engines.pil.Engine)
    source = get_source('a200x140.jpeg')

    thumb = thumbnail(source, '150x150',
        ('rotate', 50),
        ('crop', 60, 70, 'center'),
    )
    name = thumb.key + '.jpeg'
    assert_image(name, 'multifilter-pil.jpeg')
    remove_thumb(name)

