from pythonp2p import Node
HOST = ""
PORT = 65432
FILE_PORT = 65433
ip = "127.0.0.1"
if __name__ == "__main__":
    print("starting main")
    node = Node(HOST, PORT, FILE_PORT)  # start the node
    node.start()
    
    #node.connect_to(ip, )
   