import os

BLOCK_SIZE = 1024

def unpack(bw64_reader, dst_dir):
    with open(_file_name(dst_dir), 'wb') as dst:
        while bw64_reader.tell() != len(bw64_reader):
            dst.write(readRawAudioDataFromBW64(bw64_reader, BLOCK_SIZE))


def readRawAudioDataFromBW64(bw64_reader, block_size):
    ## checks for end of file
    if (bw64_reader.tell() + block_size > len(bw64_reader)):
        block_size = len(bw64_reader) - bw64_reader.tell()
    return bw64_reader._buffer.read(block_size * bw64_reader._formatInfo.blockAlignment)

def _file_name(dir):
    return os.path.join(dir, "audio")

def pack(src_dir, bw64_writer):
    file_path = _file_name(src_dir)
    if not os.path.exists(file_path):
        return None
    with open(file_path, 'rb') as src:
        for chunk in read_in_chunks(src):
            bw64_writer._buffer.write(chunk)
            bw64_writer._dataBytesWritten += len(chunk)


def read_in_chunks(file_object, chunk_size=1024):
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data