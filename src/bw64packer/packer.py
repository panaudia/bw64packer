import os

from ear.fileio.bw64 import Bw64Reader, Bw64Writer
from bw64packer.chunks import adm, audio, bext, chna, format

def unpack(src_file, dst_dir):

    os.mkdir(dst_dir)

    with open(src_file, 'rb') as f:
        bw64_reader = Bw64Reader(f)
        for chunk in (adm, audio, bext, chna, format):
            chunk.unpack(bw64_reader, dst_dir)


def pack(src_dir, dst_file):

    with open(dst_file, "wb") as dst:
        writer = Bw64Writer(dst,
                            formatInfo=format.pack(src_dir),
                            chna=chna.pack(src_dir),
                            axml=adm.pack(src_dir),
                            bext=bext.pack(src_dir),
                            forceBw64=False)

        audio.pack(src_dir, writer)
        writer.close()
