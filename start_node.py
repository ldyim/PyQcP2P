
import requests
import time
import hashlib
import os

def get_public_ip(): 
    try: 
        response = requests.get('https://api.ipify.org') 
        if response.status_code == 200: 
            return response.text 
        else: 
            return "Error: Unable to retrieve public IP address" 
    except Exception as e: 
        return f"Error: {e}" 
public_ip = get_public_ip() 



def count_files(directory):
    # Check if the directory exists
    if not os.path.isdir(directory):
        print(f"The directory '{directory}' does not exist.")
        return
    
    # List all files in the directory
    files = os.listdir(directory)
    
    # Count the number of files
    num_files = len(files)
    
    # Print the result
    return num_files

# Replace 'transfer_directory' with the path to your directory
directory_path = 'transfer_directory'



from pythonp2p import Node
HOST = "0.0.0.0"
PORT = 9999
FILE_PORT = 65433
ip = ""
if __name__ == "__main__":
    print(f"Starting node on {public_ip}:{PORT}")
    node = Node(HOST, PORT, FILE_PORT, public_ip)  # start the node
    node.start()
    node.setfiledir("transfer_directory/")
    
    print("adding all files in file directory to node \n")
    for file in os.listdir("files"):
        node.addfile(f"files/{file}")
    
    
    
    time.sleep(3)
    node_num = input("Enter node #: ")
    while True:
        action = input("\n\n\nConnect to Node: Enter C \n Send Message: Enter M \n Add File: Enter A \n Get File list: Enter F \n Get File: Enter G \n Benchmark Download: Enter B \n")
        if action == "C":
            ip = input("Enter IP: ")
            node.connect_to(ip, 9999)
        elif action == "M":
            message = input("Enter Message: ")
            node.send_message(message)
        elif action == "A":
            file = input("Enter File Path: ")
            hash = node.addfile(file)
            node.send_message("addfile: " + file + " with hash: " + hash)
        elif action == "F":
            print(node.file_manager.files)
        elif action == "G":
            
            file = input("Enter File Hash: ")
            print(node.requestFile(file))
        elif action == "B":
            number_of_nodes = int(input("Enter number of nodes: "))
            start = time.time()
            for i in range(1, number_of_nodes + 1):
                if i == node_num:
                    continue
                for j in range(5):
                    file = f"files/file{i}_{j}.txt"
                    hash = hashlib.md5(file.encode()).hexdigest()
                    print(f"Requesting file {file} with hash {hash}")
                    print(node.requestFile(hash))
            
            # print(f"Time taken to download 5 files from each of {number_of_nodes} nodes: {end - start} seconds")
            while True:
                if count_files == 35:
                    end = time.time()
                    print(f"Time taken to download 5 files from each of {number_of_nodes} nodes: {end - start} seconds")
                    break
                  
            