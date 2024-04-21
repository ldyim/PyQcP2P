
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
            print(node.file_manager.files)
            file = input("Enter File Hash: ")
            print(node.requestFile(file))
        elif action == "B":
            number_of_nodes = int(input("Enter number of nodes: "))
            start = time.time()
            for i in range(1, number_of_nodes + 1):
                if i == int(node_num):
                    continue
                for j in range(5):
                    
                    #isComplete = None
                    if node.file_manager.downloader:
                        node.file_manager.downloader.finished = False
                    file = f"files/file{i}_{j}.txt"
                    hash = hashlib.md5(file.encode()).hexdigest()
                    print(f"Requesting file {file} with hash {hash}")
                    isComplete = (node.requestFile(hash))
                    # while not node.file_manager.downloader:
                    #     continue
                    # while isComplete == None or isComplete == False:
                    #     isComplete = node.file_manager.downloader.finished
                    #     continue
            end = time.time()
            print(f"Time taken to download 5 files from each of {number_of_nodes} nodes: {end - start} seconds")
                
        time.sleep(3)
