"""Binary telemetry frame packing/unpacking."""
import struct

HEADER_MAGIC = b'\xAE\x42'

def pack_frame(seq: int, timestamp_ms: int, payload: bytes) -> bytes:
    """
    Pack a telemetry frame.
    Format: 2B magic | 2B seq | 4B timestamp_ms | 2B payload_len | Nb payload
    """
    header = struct.pack('>HHIH', *struct.unpack('>HH', HEADER_MAGIC + b'\x00\x00')[:0],
                        seq, timestamp_ms, len(payload))
    # simpler manual pack
    return HEADER_MAGIC + struct.pack('>HIH', seq, timestamp_ms, len(payload)) + payload

def unpack_frame(data: bytes) -> dict:
    """Unpack a telemetry frame produced by pack_frame."""
    if data[:2] != HEADER_MAGIC:
        raise ValueError("Bad magic bytes")
    seq, timestamp_ms, plen = struct.unpack_from('>HIH', data, 2)
    payload = data[10:10 + plen]
    return {'seq': seq, 'timestamp_ms': timestamp_ms, 'payload': payload}
