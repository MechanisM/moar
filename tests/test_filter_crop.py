# -*- coding: utf-8 -*-
import moar

from .utils import *


def test_pil_crop():
    thumbnail = moar.Thumbnailer(engine=moar.engines.pil.Engine)
    source = get_source('a200x140.png')

    thumb = thumbnail(source, ('crop', 50, 90), format='PNG')
    name = thumb.key + '.png'
    assert_image(name, 'crop50x90.png')
    remove_thumb(name)


def test_pil_crop_xy_px():
    thumbnail = moar.Thumbnailer(engine=moar.engines.pil.Engine)
    source = get_source('a200x140.png')

    thumb = thumbnail(source, ('crop', 50, 50, 100, 20), format='PNG')
    name = thumb.key + '.png'
    assert_image(name, 'crop50x50-100|20.png')
    remove_thumb(name)


def test_pil_crop_xy_short():
    thumbnail = moar.Thumbnailer(engine=moar.engines.pil.Engine)
    source = get_source('a200x140.png')

    thumb = thumbnail(source, ('crop', 50, 50, 70), format='PNG')
    name = thumb.key + '.png'
    assert_image(name, 'crop50x50-70.png')
    remove_thumb(name)


def test_pil_crop_xy_pc():
    thumbnail = moar.Thumbnailer(engine=moar.engines.pil.Engine)
    source = get_source('a200x140.png')

    thumb = thumbnail(source, ('crop', 50, 50, '30%', '50%'), format='PNG')
    name = thumb.key + '.png'
    assert_image(name, 'crop50x50-30pc|50pc.png')
    remove_thumb(name)


def test_pil_crop_xy_center():
    thumbnail = moar.Thumbnailer(engine=moar.engines.pil.Engine)
    source = get_source('a200x140.png')

    thumb = thumbnail(source, ('crop', 50, 50, 'center'), format='PNG')
    name = thumb.key + '.png'
    assert_image(name, 'crop50x50-center.png')
    remove_thumb(name)


def test_pil_crop_xy_overflow_xy():
    thumbnail = moar.Thumbnailer(engine=moar.engines.pil.Engine)
    source = get_source('a200x140.png')

    thumb = thumbnail(source, ('crop', 50, 50, 190, 130), format='PNG')
    name = thumb.key + '.png'
    assert_size(name, 10, 10)
    remove_thumb(name)


def test_pil_crop_xy_overflow_wh():
    thumbnail = moar.Thumbnailer(engine=moar.engines.pil.Engine)
    source = get_source('a200x140.png')

    thumb = thumbnail(source, ('crop', 500, 500), format='PNG')
    name = thumb.key + '.png'
    assert_image(name, 'crop500x500.png')
    remove_thumb(name)

## ----------------------------------------------------------------------------

def test_wand_crop():
    thumbnail = moar.Thumbnailer(engine=moar.engines.wand.Engine)
    source = get_source('a200x140.png')

    thumb = thumbnail(source, ('crop', 50, 90), format='PNG')
    name = thumb.key + '.png'
    assert_image(name, 'crop50x90.png')
    remove_thumb(name)


def test_wand_crop_xy_px():
    thumbnail = moar.Thumbnailer(engine=moar.engines.wand.Engine)
    source = get_source('a200x140.png')

    thumb = thumbnail(source, ('crop', 50, 50, 100, 20), format='PNG')
    name = thumb.key + '.png'
    assert_image(name, 'crop50x50-100|20.png')
    remove_thumb(name)


def test_wand_crop_xy_short():
    thumbnail = moar.Thumbnailer(engine=moar.engines.wand.Engine)
    source = get_source('a200x140.png')

    thumb = thumbnail(source, ('crop', 50, 50, 70), format='PNG')
    name = thumb.key + '.png'
    assert_image(name, 'crop50x50-70.png')
    remove_thumb(name)


def test_wand_crop_xy_pc():
    thumbnail = moar.Thumbnailer(engine=moar.engines.wand.Engine)
    source = get_source('a200x140.png')

    thumb = thumbnail(source, ('crop', 50, 50, '30%', '50%'), format='PNG')
    name = thumb.key + '.png'
    assert_image(name, 'crop50x50-30pc|50pc.png')
    remove_thumb(name)


def test_wand_crop_xy_center():
    thumbnail = moar.Thumbnailer(engine=moar.engines.wand.Engine)
    source = get_source('a200x140.png')

    thumb = thumbnail(source, ('crop', 50, 50, 'center'), format='PNG')
    name = thumb.key + '.png'
    assert_image(name, 'crop50x50-center.png')
    remove_thumb(name)


def test_wand_crop_xy_overflow_xy():
    thumbnail = moar.Thumbnailer(engine=moar.engines.wand.Engine)
    source = get_source('a200x140.png')

    thumb = thumbnail(source, ('crop', 50, 50, 190, 130), format='PNG')
    name = thumb.key + '.png'
    assert_size(name, 10, 10)
    remove_thumb(name)


def test_wand_crop_xy_overflow_wh():
    thumbnail = moar.Thumbnailer(engine=moar.engines.wand.Engine)
    source = get_source('a200x140.png')

    thumb = thumbnail(source, ('crop', 500, 500), format='PNG')
    name = thumb.key + '.png'
    assert_image(name, 'crop500x500.png')
    remove_thumb(name)

