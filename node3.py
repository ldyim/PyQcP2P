from pythonp2p import Node
HOST = "0.0.0.0"
PORT = 9998
FILE_PORT = 65433
ip = "54.205.231.78" # change to your own public ipv4 address
if __name__ == "__main__":
    print("starting main")
    node = Node(HOST, PORT, FILE_PORT)  # start the node
    node.start()
    node.connect_to(ip, 9999)
    node.send_message('{"test": "test message from node 3"}')
