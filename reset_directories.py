import os
import random
import hashlib
import random
import string
import sys
def generate_random_word(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def generate_large_text_file(filename, size_in_mb):
    target_size = size_in_mb * 1024 * 1024  # Convert MB to bytes
    current_size = 0

    with open(filename, 'w') as file:
        while current_size < target_size:
            word = generate_random_word(random.randint(4, 10))  # Generate random words of length 4 to 10
            file.write(word + ' ')
            current_size += len(word) + 1  # Update current size including the space

    print(f'Generated file {filename} with size {os.path.getsize(filename)/1024/1024:.2f} MB')

try:
    os.mkdir("files")
except e:
    print(e)
    pass
    
try:
    os.mkdir("transfer_directory")
except:
    pass

files = [f for f in os.listdir("files")]
transfer_directory = [f for f in os.listdir("transfer_directory")]



for f in range(len(files)):
    os.remove(f"files/{files[f]}")
for t in range(len(transfer_directory)):
    os.remove(f"transfer_directory/{transfer_directory[t]}")

for i in range(5):
    num = random.randint(0, 100)
num = input("Enter the node number:")
for i in range(5):
    generate_large_text_file(f"files/file{num}_{i}.txt", 100)

