
from PIL import Image, ImageCms
im = Image.open('default.png')
im2 = im.convert('RGB')
sRGB = ImageCms.createProfile('sRGB')
im2 = ImageCms.profileToProfile(im, 'rgb.icc', 'rgb.icc', 1, 'RGB')
im2 = im2.resize((199, 139), resample=Image.ANTIALIAS)
im2 = ImageCms.profileToProfile(im2, 'rgb.icc', sRGB)
im2.save('test.jpg', format='JPEG', quality=90)