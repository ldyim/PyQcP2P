from pythonp2p import Node
import time
HOST = "0.0.0.0"
PORT = 9999
FILE_PORT = 65432
ip = ""
public_ip = "3.143.144.51"
if __name__ == "__main__":
    print("starting main")
    node = Node(HOST, PORT, FILE_PORT, public_ip)  # start the node
    node.start()
    
    #node.connect_to(ip, 65432)
    #node.send_message('{test}')   
    time.sleep(10)
    print("requesting e8834645a7c08dd0a8c07203f7385c4f")
    node.requestFile("e8834645a7c08dd0a8c07203f7385c4f")
