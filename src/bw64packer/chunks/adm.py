import os

def unpack(bw64_reader, dst_dir):
    with open(_file_name(dst_dir), 'wb') as dst:
        dst.write(bw64_reader.axml)

def pack(src_dir):
    file_path = _file_name(src_dir)
    if not os.path.exists(file_path):
        return None
    with open(file_path, 'rb') as src:
        return src.read()

def _file_name(dir):
    return os.path.join(dir, "adm.xml")