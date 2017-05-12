from PIL import Image
import os, pathlib


sizes = [
    (48, 48),
    (72, 72),
    (96, 96),
    (144, 144),
    (192, 192),
    (512, 512)
]

filename = 'icon.png'
filename_base, filename_ext = os.path.splitext(filename)


def create_thumbnail(src, dst, wh):
    dst_path = f'{dst}/{filename_base}-{wh[0]}x{wh[1]}{filename_ext}'
    dst_path = str(pathlib.PurePath(dst_path))
    im = Image.open(src)
    im.thumbnail(wh)
    im.save(dst_path, "PNG")


path_full = os.path.realpath(__file__)
path_full_dir = os.path.dirname(path_full)

path_src_dir = path_full_dir + '/../static_src/images/manifest'
path_dst_dir = path_full_dir + '/../static/images/manifest'
path_src_dir = str(pathlib.PurePath(os.path.normpath(path_src_dir)))
path_dst_dir = str(pathlib.PurePath(os.path.normpath(path_dst_dir)))

path_file_src = str(pathlib.PurePath(f'{path_src_dir}/{filename}'))

sizes.reverse()

for size in sizes:
    create_thumbnail(path_file_src, str(path_dst_dir), size)
