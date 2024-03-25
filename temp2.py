from pythonp2p import Node
HOST = "0.0.0.0"
PORT = 9999
FILE_PORT = 81
ip = "18.224.20.85"
if __name__ == "__main__":
    print("starting main")
    node = Node(HOST, PORT, FILE_PORT)  # start the node
    node.start()
    
    #node.connect_to(ip, 65432)
    #node.send_message('{test}')   
