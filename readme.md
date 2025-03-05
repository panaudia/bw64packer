# bw64packer

This is a slight utility that packs and unpacks BW64/ADM audio files.

The BW64/ADM file format is a packed binary format containing several distinct chunks of data.  
The raw audio, adm xml and the bext are just copied out as is into their own files. 
The format info and the chna data are converted to json.

It uses the file reader and writer from the EBU ADM Renderer to access the chunks  https://github.com/ebu/ebu_adm_renderer

## Usage

bw64packer has just two functions `unpack` and `pack`

```python
unpack(src_file, dst_dir)
```

This will read the file `src_file` and create the folder `dst_dir` containing the unpacked contents in separate files:

- `adm.xml`
- `format.json`
- `chna.json`
- `audio`
- `bext`

```python
pack(src_dir, dst_file)
```

This does the opposite, you give it the `src_dir` containing the chunks in separate files named as 
above and it will combine them into a single file `dst_file`
