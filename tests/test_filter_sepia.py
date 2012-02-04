# -*- coding: utf-8 -*-
import moar

from .utils import *


def test_pil_sepia():
    thumbnail = moar.Thumbnailer(engine=moar.engines.pil.Engine)
    source = get_source('a200x140.jpeg')

    thumb = thumbnail(source, ('sepia', ))
    name = thumb.key + '.jpeg'
    assert_image(name, 'sepia.jpeg')
    remove_thumb(name)


def test_pil_sepia_rgb():
    thumbnail = moar.Thumbnailer(engine=moar.engines.pil.Engine)
    source = get_source('a200x140.jpeg')

    thumb = thumbnail(source, ('sepia', 240, 220, 190))
    name = thumb.key + '.jpeg'
    assert_image(name, 'sepia240|220|190.jpeg')
    remove_thumb(name)


def test_pil_sepia_hex():
    thumbnail = moar.Thumbnailer(engine=moar.engines.pil.Engine)
    source = get_source('a200x140.jpeg')

    thumb = thumbnail(source, ('sepia', '#ffaf2e'))
    name = thumb.key + '.jpeg'
    assert_image(name, 'sepiaFFAF2E.jpeg')
    remove_thumb(name)


def test_pil_grayscale():
    thumbnail = moar.Thumbnailer(engine=moar.engines.pil.Engine)
    source = get_source('a200x140.jpeg')

    thumb = thumbnail(source, ('grayscale', ))
    name = thumb.key + '.jpeg'
    assert_image(name, 'grayscale.jpeg')
    remove_thumb(name)

