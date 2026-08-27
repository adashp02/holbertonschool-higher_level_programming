import hashlib
from typing import List, Set, Tuple

CHUNK_SIZE = 1024 * 1024  # 1 MiB

# Each entry contains: chunk index, chunk size and SHA-256 hash.
ChunkRecord = Tuple[int, int, str]


def compute_chunk_manifest(
    file_path: str,
) -> Tuple[List[ChunkRecord], str]:
    """
    Divides a file into fixed-size chunks and calculates:

    1. A SHA-256 hash for each chunk.
    2. A SHA-256 hash for the complete file.

    The chunk hashes allow the server to request only missing
    chunks. The complete-file hash is used for final verification.
    """
    manifest: List[ChunkRecord] = []
    whole_file_hash = hashlib.sha256()

    with open(file_path, "rb") as file:
        chunk_index = 0

        while True:
            chunk = file.read(CHUNK_SIZE)

            if not chunk:
                break

            whole_file_hash.update(chunk)
            chunk_hash = hashlib.sha256(chunk).hexdigest()

            manifest.append(
                (chunk_index, len(chunk), chunk_hash)
            )
            chunk_index += 1

    return manifest, whole_file_hash.hexdigest()


def get_missing_chunks(
    client_manifest: List[ChunkRecord],
    server_chunk_hashes: Set[str],
) -> List[int]:
    """
    Returns the indices of chunks not already held by the server.

    The server must maintain a chunk store in which chunk data can
    be retrieved by its SHA-256 hash.
    """
    return [
        index
        for index, _size, chunk_hash in client_manifest
        if chunk_hash not in server_chunk_hashes
    ]
