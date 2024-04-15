import hashlib
def hashFileWhole(filepath):
        hasher = hashlib.md5()
        try:
            with open(filepath, "rb") as afile:
                buf = afile.read()
                while len(buf) > 0:
                    hasher.update(buf)
                    buf = afile.read()
            return hasher.hexdigest()
        except:
            print("Couldn't find/hash file " + filepath)
print(hashFileWhole("transfer_directory/file1-0.txt"))