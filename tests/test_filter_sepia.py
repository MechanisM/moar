# -*- coding: utf-8 -*-
import moar

from .utils import *


def test_pil_sepia():
    thumbnail = moar.Thumbnailer(engine=moar.engines.pil.Engine)
    source = get_source('a200x140.png')

    thumb = thumbnail(source, ('sepia', ), format='PNG')
    name = thumb.key + '.png'
    assert_image(name, 'sepia.png')
    remove_thumb(name)


def test_pil_sepia_rgb():
    thumbnail = moar.Thumbnailer(engine=moar.engines.pil.Engine)
    source = get_source('a200x140.png')

    thumb = thumbnail(source, ('sepia', 240, 220, 190), format='PNG')
    name = thumb.key + '.png'
    assert_image(name, 'sepia240|220|190.png')
    remove_thumb(name)


def test_pil_sepia_hex():
    thumbnail = moar.Thumbnailer(engine=moar.engines.pil.Engine)
    source = get_source('a200x140.png')

    thumb = thumbnail(source, ('sepia', '#ffaf2e'), format='PNG')
    name = thumb.key + '.png'
    assert_image(name, 'sepiaFFAF2E.png')
    remove_thumb(name)


def test_pil_grayscale():
    thumbnail = moar.Thumbnailer(engine=moar.engines.pil.Engine)
    source = get_source('a200x140.png')

    thumb = thumbnail(source, ('grayscale', ), format='PNG')
    name = thumb.key + '.png'
    assert_image(name, 'grayscale.png')
    remove_thumb(name)


def test_magick_sepia():
    thumbnail = moar.Thumbnailer(engine=moar.engines.magick.Engine)
    source = get_source('a200x140.png')

    thumb = thumbnail(source, ('sepia', ), format='PNG')
    name = thumb.key + '.png'
    assert_image(name, 'sepia.png')
    remove_thumb(name)


def test_magick_sepia_rgb():
    thumbnail = moar.Thumbnailer(engine=moar.engines.magick.Engine)
    source = get_source('a200x140.png')

    thumb = thumbnail(source, ('sepia', 240, 220, 190), format='PNG')
    name = thumb.key + '.png'
    assert_image(name, 'sepia240|220|190.png')
    remove_thumb(name)


def test_magick_sepia_hex():
    thumbnail = moar.Thumbnailer(engine=moar.engines.magick.Engine)
    source = get_source('a200x140.png')

    thumb = thumbnail(source, ('sepia', '#ffaf2e'), format='PNG')
    name = thumb.key + '.png'
    assert_image(name, 'sepiaFFAF2E.png')
    remove_thumb(name)


def test_magick_grayscale():
    thumbnail = moar.Thumbnailer(engine=moar.engines.magick.Engine)
    source = get_source('a200x140.png')

    thumb = thumbnail(source, ('grayscale', ), format='PNG')
    name = thumb.key + '.png'
    assert_image(name, 'grayscale.png')
    remove_thumb(name)

