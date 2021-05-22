import os
from base64 import b85decode
from hashlib import sha512
from lzma import decompress

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def unpack(data: bytes) -> bytes:
    return decompress(b85decode(data))


def verify(data: bytes, sha512_digest: str) -> bool:
    return sha512(data).hexdigest() == sha512_digest




for name in xmrig['file']:
    data, sha512_digest = xmrig['file'][name]
    print('unpacking', name, 'with sha512_digest', sha512_digest)
    assert verify(data, sha512_digest), name + ' not verified'
    with open(name, 'wb') as fout:
        fout.write(data)