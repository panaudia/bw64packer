import os
import json

from ear.fileio.bw64.chunks import FormatInfoChunk, ExtraData

def unpack(bw64Reader, dst_dir):
    format_info_file_path = _file_name(dst_dir)
    format_info = bw64Reader._formatInfo
    format_info_json = _format_info_as_json(format_info)
    with open(format_info_file_path, 'w') as dst:
        dst.write(json.dumps(format_info_json, indent=4))

def pack(src_dir):
    with open(_file_name(src_dir), 'r') as src:
        format_json = json.load(src)
        extra_json = format_json.get("extra_data")
        extra_data = ExtraData(
            validBitsPerSample=extra_json["valid_bits_per_sample"],
            dwChannelMask=extra_json["dw_channel_mask"],
            subFormat=extra_json["sub_format"],
            subFormatString=extra_json["sub_format_string"],
        ) if extra_json is not None else None

        return FormatInfoChunk(formatTag=format_json["format_tag"],
                               channelCount=format_json["channel_count"],
                               sampleRate=format_json["sample_rate"],
                               bitsPerSample=format_json["bits_per_sample"],
                                extraData=extra_data )

def _file_name(dir):
    return os.path.join(dir, "format.json")

def _extra_as_json(extra_data):
    return {"valid_bits_per_sample": extra_data.validBitsPerSample,
            "dw_channel_mask": extra_data.dwChannelMask,
            "sub_format": extra_data.subFormat,
            "sub_format_string": extra_data.subFormatString}

def _format_info_as_json(format_info):

    info = {"format_tag": format_info.formatTag,
            "channel_count": format_info.channelCount,
            "sample_rate": format_info.sampleRate,
            "bits_per_sample": format_info.bitsPerSample}

    if format_info.extraData is not None:
        info["extra_data"] = _extra_as_json(format_info.extraData)

    return info