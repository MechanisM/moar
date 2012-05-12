# -*- coding: utf-8 -*-
import moar

from .utils import *


WandEngine = moar.engines.wand.Engine

## ----------------------------------------------------------------------------

# def test_wand_sepia():
#     thumbnail = moar.Thumbnailer(engine=WandEngine)
#     source = get_source('a200x140.png')

#     thumb = thumbnail(source, ['sepia'], format='PNG')
#     name = thumb.key + '.png'
#     assert_image(name, 'sepia-wand.png')
#     remove_thumb(name)


# def test_wand_sepia_rgb():
#     thumbnail = moar.Thumbnailer(engine=WandEngine)
#     source = get_source('a200x140.png')

#     thumb = thumbnail(source, ('sepia', 240, 220, 190), format='PNG')
#     name = thumb.key + '.png'
#     assert_image(name, 'sepia240|220|190-wand.png')
#     remove_thumb(name)


# def test_wand_sepia_hex():
#     thumbnail = moar.Thumbnailer(engine=WandEngine)
#     source = get_source('a200x140.png')

#     thumb = thumbnail(source, ('sepia', '#ffaf2e'), format='PNG')
#     name = thumb.key + '.png'
#     assert_image(name, 'sepiaFFAF2E-wand.png')
#     remove_thumb(name)


# def test_wand_grayscale():
#     thumbnail = moar.Thumbnailer(engine=WandEngine)
#     source = get_source('a200x140.png')

#     thumb = thumbnail(source, ('grayscale', ), format='PNG')
#     name = thumb.key + '.png'
#     assert_image(name, 'grayscale-wand.png')
#     remove_thumb(name)

