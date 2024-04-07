import os
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

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <size_in_mb> [filename]")
        sys.exit(1)
    
    size_in_mb = int(sys.argv[1])
    filename = 'large_text_file.txt'  # Default filename
    if len(sys.argv) > 2:
        filename = sys.argv[2]
    
    generate_large_text_file(filename, size_in_mb)