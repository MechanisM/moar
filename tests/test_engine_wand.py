# -*- coding: utf-8 -*-
import moar

from .utils import *


ENGINE = moar.engines.wand.Engine


def test_load_image():
    thumbnail = moar.Thumbnailer(engine=ENGINE)
    source = get_source('a200x140.png')
    
    thumb = thumbnail(source, format='PNG')
    name1 = thumb.key + '.png'
    assert_image(name1, 'default-wand.png')
    assert thumb.url == str(thumb)
    
    thumb2 = thumbnail(source, format='PNG')
    assert str(thumb) == str(thumb2)

    remove_thumb(name1)

    source = get_source('a200x140.jpeg')
    thumb = thumbnail(source)
    name2 = thumb.key + '.jpeg'
    assert_exists(name2)
    
    remove_thumb(name2)


def test_options():
    thumbnail = moar.Thumbnailer(engine=ENGINE)
    source = get_source('a200x140.png')

    thumb = thumbnail(source, format='JPEG', quality=20, progressive=True)
    name = thumb.key + '.jpeg'
    assert_exists(name)

    remove_thumb(name)


def test_orientation():
    ### Sadly, not implemented yet :( ###
    return
    thumbnail = moar.Thumbnailer(engine=ENGINE)
    test_images = [
        '1_topleft.jpeg',
        '2_topright.jpeg',
        '3_bottomright.jpeg',
        '4_bottomleft.jpeg',
        '5_lefttop.jpeg',
        '6_righttop.jpeg',
        '7_rightbottom.jpeg',
        '8_leftbottom.jpeg',
    ]

    for sname in test_images:
        source = get_source(sname)
        thumb = thumbnail(source, orientation=True)
        name = thumb.key + '.jpeg'
        assert_image(name, sname)

        remove_thumb(name)


def test_geometry_w():
    thumbnail = moar.Thumbnailer(engine=ENGINE)

    source = get_source('a200x140.jpeg')
    thumb = thumbnail(source, '100')
    name = thumb.key + '.jpeg'
    assert_size(name, width=100, height=70)

    remove_thumb(name)


def test_geometry_w_upscale():
    thumbnail = moar.Thumbnailer(engine=ENGINE)

    source = get_source('b94x200.png')
    thumb = thumbnail(source, '141', upscale=False)
    name = thumb.key + '.jpeg'
    assert_size(name, width=94, height=200)

    remove_thumb(name)

    thumb = thumbnail(source, '141', upscale=True)
    name = thumb.key + '.jpeg'
    assert_size(name, width=141, height=300)

    remove_thumb(name)


def test_geometry_h():
    thumbnail = moar.Thumbnailer(engine=ENGINE)

    source = get_source('b94x200.png')
    thumb = thumbnail(source, 'x100')
    name = thumb.key + '.jpeg'
    assert_size(name, width=47, height=100)

    remove_thumb(name)


def test_geometry_h_upscale():
    thumbnail = moar.Thumbnailer(engine=ENGINE)

    source = get_source('a200x140.jpeg')
    thumb = thumbnail(source, 'x280', upscale=False)
    name = thumb.key + '.jpeg'
    assert_size(name, width=200, height=140)

    remove_thumb(name)

    thumb = thumbnail(source, 'x280', upscale=True)
    name = thumb.key + '.jpeg'
    assert_size(name, width=400, height=280)

    remove_thumb(name)


def test_geometry_wh():
    thumbnail = moar.Thumbnailer(engine=ENGINE)

    source = get_source('a200x140.png')
    thumb = thumbnail(source, '50x50', format='PNG')
    name = thumb.key + '.png'
    assert_size(name, width=50, height=35)

    remove_thumb(name)

    source = get_source('b94x200.png')
    thumb = thumbnail(source, '50x50', format='PNG')
    name = thumb.key + '.png'
    assert_size(name, width=24, height=50)

    remove_thumb(name)


def test_geometry_wh_upscale():
    thumbnail = moar.Thumbnailer(engine=ENGINE)

    source = get_source('a200x140.jpeg')
    thumb = thumbnail(source, '400x400', upscale=True)
    name = thumb.key + '.jpeg'
    assert_size(name, width=400, height=280)

    remove_thumb(name)


def test_geometry_wh_resize():
    thumbnail = moar.Thumbnailer(engine=ENGINE)

    source = get_source('a200x140.jpeg')
    thumb = thumbnail(source, '50x50', resize=True)
    name = thumb.key + '.jpeg'
    assert_size(name, width=50, height=50)

    remove_thumb(name)


def test_geometry_callable():
    thumbnail = moar.Thumbnailer(engine=ENGINE)

    source = get_source('a200x140.jpeg')
    thumb = thumbnail(source, lambda: str(50 * 2))
    name = thumb.key + '.jpeg'
    assert_size(name, width=100, height=70)

    remove_thumb(name)

