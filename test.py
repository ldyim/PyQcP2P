import hashlib


def hashFile(filepath):
        hasher = hashlib.md5()
        buf = filepath.encode()
        hasher.update(buf)
        return hasher.hexdigest()


print(hashFile("files/file1.txt"))
