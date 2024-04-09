#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Please provide an Elastic IP as an argument."
    exit 1
fi

ELASTIC_IP=$1
echo "Received Elastic IP: $ELASTIC_IP"

cat > san.cnf <<EOF
[req]
default_bits = 2048
distinguished_name = req_distinguished_name
req_extensions = req_ext
x509_extensions = v3_req
prompt = no

[req_distinguished_name]
countryName = US
stateOrProvinceName = California
localityName = San Francisco
organizationName = My Company
commonName = My Company Common Name

[req_ext]
subjectAltName = @alt_names

[v3_req]
subjectAltName = @alt_names

[alt_names]
DNS.1 = example.com
IP.1 = $ELASTIC_IP
EOF

openssl req -new -x509 -days 365 -nodes -keyout server.key -out server.crt -config san.cnf

echo "Generated certificate (server.crt) and private key (server.key) for IP: $ELASTIC_IP"