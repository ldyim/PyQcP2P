# import asyncio
# import sys

# from aioquic.asyncio.protocol import QuicConnectionProtocol
# from aioquic.asyncio.client import connect
# from aioquic.quic.configuration import QuicConfiguration
# from aioquic.quic.events import StreamDataReceived

# class FileClientQuicProtocol(QuicConnectionProtocol):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.ready_event = asyncio.Event()

#     def quic_event_received(self, event):
#         if isinstance(event, StreamDataReceived):
#             print(f"Get response from server: {event.data.decode()}")
#             if event.data.endswith(b'\r\n'):
#                 self.ready_event.set()

# async def run_quic_client(server_ip, file_path):
#     configuration = QuicConfiguration(is_client=True)
#     configuration.load_verify_locations('server.crt')

#     async with connect(
#         server_ip, 4433, configuration=configuration, create_protocol=FileClientQuicProtocol
#     ) as protocol:
#         print('Connect to QUIC Server')
#         # Read data from 
#         with open(file_path, 'rb') as file:
#             data = file.read()
#         protocol._quic.send_stream_data(0, data)
#         protocol._quic.send_stream_data(0, b'\r\n')
#         protocol.transmit()
#         # Wait for response from server
#         await protocol.ready_event.wait() 

# if __name__ == '__main__':
#     if len(sys.argv) != 3:
#         print("Command: python script.py <server_ip> <file_path>")
#         sys.exit(1)

#     server_ip = sys.argv[1]
#     file_path = sys.argv[2]
#     asyncio.run(run_quic_client(server_ip, file_path))

import asyncio
import sys

from aioquic.asyncio.protocol import QuicConnectionProtocol
from aioquic.asyncio.client import connect
from aioquic.quic.configuration import QuicConfiguration
from aioquic.quic.events import StreamDataReceived
import threading


class FileClientQuicProtocol(QuicConnectionProtocol):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ready_event = asyncio.Event()

    def quic_event_received(self, event):
        if isinstance(event, StreamDataReceived):
            print(f"Get response from server: {event.data.decode()}")
            if event.data.endswith(b'\r\n'):
                self.ready_event.set()

class QuicClient:
    def __init__(self, server_ip, file_path):
        self.server_ip = server_ip
        self.file_path = file_path
        self.configuration = QuicConfiguration(is_client=True)
        self.configuration.load_verify_locations('server.crt')

    async def run(self):
        async with connect(
            self.server_ip, 4433, configuration=self.configuration, create_protocol=FileClientQuicProtocol
        ) as protocol:
            print('Connect to QUIC Server')
            with open(self.file_path, 'rb') as file:
                data = file.read()
            protocol._quic.send_stream_data(0, data)
            protocol._quic.send_stream_data(0, b'\r\n')
            protocol.transmit()
            await protocol.ready_event.wait() 

    def start(self):
        asyncio.run(self.run())
