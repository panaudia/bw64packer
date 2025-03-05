import os
import json
from ear.fileio.bw64.chunks import ChnaChunk, AudioID

def unpack(bw64_reader, dst_dir):

    chna_json = _chna_as_json(bw64_reader.chna.audioIDs)
    with open(_file_name(dst_dir), 'w') as dst:
        dst.write(json.dumps(chna_json, indent=4))

def pack(src_dir):
    file_path = _file_name(src_dir)
    if not os.path.exists(file_path):
        return None
    with open(file_path, 'r') as src:
        chna_json = json.load(src)
        return _chna_from_json(chna_json)

def _file_name(dir):
    return os.path.join(dir, "chna.json")

def _chna_as_json(chna):
    return [_audio_id_as_json(audio_id) for audio_id in chna]


def _chna_from_json(chna_json):
    return ChnaChunk([AudioID(
            trackIndex=audio_id_json["track_index"],
            audioTrackUID=audio_id_json["audio_track_uid"],
            audioTrackFormatIDRef=audio_id_json["audio_track_format_id_ref"],
            audioPackFormatIDRef=audio_id_json.get("audio_pack_format_id_ref"),
        ) for audio_id_json in chna_json])


def _audio_id_as_json(audio_id):
    j = {"track_index": audio_id.trackIndex,
            "audio_track_uid": audio_id.audioTrackUID,
            "audio_track_format_id_ref": audio_id.audioTrackFormatIDRef}

    if audio_id.audioPackFormatIDRef is not None:
        j["audio_pack_format_id_ref"] = audio_id.audioPackFormatIDRef

    return j
