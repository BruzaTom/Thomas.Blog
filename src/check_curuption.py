import hashlib

def check_curr(src, path):
    def calculate_checksum(file_path):
        hash_md5 = hashlib.md5()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()

    src_path = src
    dst_path = path

    src_checksum = calculate_checksum(src_path)
    dst_checksum = calculate_checksum(dst_path)

    if src_checksum == dst_checksum:
        print("File copied successfully")
    else:
        print("File corruption detected")
