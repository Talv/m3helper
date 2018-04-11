import re
import os
import shutil
from glob import glob as real_glob


def insensitive_glob(pattern):
    def either(c):
        return '[%s%s]'%(c.lower(),c.upper()) if c.isalpha() else c
    return real_glob(''.join(map(either,pattern)))

glob = real_glob if os.name == 'nt' else insensitive_glob


def find_archives(curr_dir):
    for x in glob(curr_dir + '/*'):
        if not os.path.isdir(x):
            continue
        if re.search(r'(sc2mod|sc2map|sc2campaign|stormmod)$', x, flags=re.IGNORECASE):
            yield x
            yield from glob(x + '/base.*')
        else:
            yield from list(find_archives(x))


def find_files_in_archive(filenames, src_dirs):
    fmap = dict()
    for curr_fname in filenames:
        fmap[curr_fname] = False
        for curr_src in src_dirs:
            abs_filename = glob(os.path.join(curr_src, curr_fname))
            if len(abs_filename):
                fmap[curr_fname] = abs_filename[0]
                break
    return fmap


def insert_texture_file(target_dir, filename, src_filename):
    target_absfilename = os.path.join(target_dir, filename)
    if len(glob(target_absfilename)):
        return False
    if not os.path.exists(os.path.dirname(target_absfilename)):
        os.makedirs(os.path.dirname(target_absfilename))
    shutil.copyfile(src_filename, target_absfilename)
    return True


def m3_textures_list(filename):
    with open(filename, 'rb') as f:
        out = set()
        results = re.findall(rb'([\w\/]+\.dds)\x00', f.read(), flags=(re.ASCII | re.IGNORECASE))
        for x in results:
            out.add(x.decode('ascii'))
        return list(out)

