# PyQcP2P
Make sure you install python3 and pip install pycryptodome before anything else
You might need to run the following commands

```shell
sudo apt upgrade && sudo apt update
sudo apt install python3
git clone https://github.com/ldyim/PyQcP2P.git
pip3 install pycryptodome
cd PyQcP2P
```
Add your port and IP address to the doc


How to test the existing file transfer function
```shell
python3 start_node.py # run this in two nodes
# choose the number and input the ip address you want to connect
# choose add files in node 1 and input the file path
# choose get files in node 2 and input the hash code.
```


# QUIC File transfer

```shell

# (Elastic IP preferred) Generate private key and certificate according to your EC2 IPv4 address. 
# Example ./generate_cert.sh 34.195.119.11
./generate_cert.sh <your ip address>

# Start the server
# The server will start running and listen on 0.0.0.0:4433.
python3 file_server.py

# Start the client and send file
python3 file_client.py <server_ip> <file_path_on_your_client>

# The server will receive the file and save it as received_file.txt. It will then send a response to the client indicating that the file was received successfully.

```

Tips:
1. To change the server's listening address or port, modify the run_quic_server function in file_server.py.
2. To customize the file handling logic on the server side, modify the quic_event_received method in the FileServerQuicProtocol class in file_server.py.
3. To modify the client's behavior or add additional functionality, update the run_quic_client function and the FileClientQuicProtocol class in file_client.py.

## EC2 Elastic IP configuration

Elastic IP binding to an EC2 instance provides a static, public IP address for stable external access and connectivity management.

Process:
EC2 console -> Network&Security -> Elastic IPs 
-> Allocate Elastic IP address -> Select region -> Associate with your EC2 instance.

## TLS Configuration Generator
The script (generate_cert.sh) uses an IP(Elastic IP preferred) provided as an argument and generates a self-signed SSL certificate with this IP included as a Subject Alternative Name (SAN), useful for securing connections.
 
It first validates the presence of an argument, then creates a configuration file (san.cnf) specifying certificate details and uses OpenSSL to generate the certificate and key based on this configuration.
