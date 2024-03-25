import os
import random
import hashlib
files = [f for f in os.listdir("files")]
transfer_directory = [f for f in os.listdir("transfer_directory")]

for f in range(len(files)):
    os.remove(f"files/{files[f]}")
for t in range(len(transfer_directory)):
    os.remove(f"transfer_directory/{transfer_directory[t]}")

for i in range(5):
    num = random.randint(0, 20)
    with open(f"files/{num}.txt", "w") as f:
        f.write(hashlib.md5(str(num).encode()).hexdigest())

    
