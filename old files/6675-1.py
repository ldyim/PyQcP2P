from pythonp2p import Node
HOST = "0.0.0.0"
PORT = 9998
FILE_PORT = 65433
ip = "18.188.86.138"
public_ip = "3.143.144.51"
if __name__ == "__main__":
    print("starting main")
    node = Node(HOST, PORT, FILE_PORT, public_ip)  # start the node
    node.start()
    node.connect_to(ip, 9999)
    node.send_message('{"test": "test message from node 3"}')
    print(node.addfile("test.txt"))
