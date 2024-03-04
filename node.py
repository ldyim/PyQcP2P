from pythonp2p import Node
HOST = ""
PORT = 65436
FILE_PORT = 65437
ip = "127.0.0.1"
if __name__ == "__main__":
    print("starting node")
    node = Node(HOST, PORT, FILE_PORT)  # start the node
    node.start()
    node.connect_to("127.0.0.1", 65432)
    node.send_message('{"test": "test message from node 2"}')
