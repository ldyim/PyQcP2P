# import asyncio
# from aioquic.asyncio.protocol import QuicConnectionProtocol
# from aioquic.asyncio.server import serve
# from aioquic.quic.configuration import QuicConfiguration
# from aioquic.quic.events import StreamDataReceived, HandshakeCompleted

# class FileServerQuicProtocol(QuicConnectionProtocol):
    
#     def quic_event_received(self, event):
#         if isinstance(event, HandshakeCompleted):
#             print("Handshake finished")
#         elif isinstance(event, StreamDataReceived):
#             print(f"Received data, buffering and write to file")
#             with open('received_file.txt', 'wb') as file:
#                 file.write(event.data)
#                 if event.data.endswith(b'\r\n'):
#                     print("File received successfully")
#                     self.send_response()

#     def send_response(self):
#         response = b'File received successfully.\r\n'
#         self._quic.send_stream_data(0, response, end_stream=True)
#         self.transmit()
#         print("Response sent to client.")

# async def run_quic_server():
#     configuration = QuicConfiguration(is_client=False)
#     configuration.load_cert_chain('server.crt', 'server.key')

#     await serve(
#         '0.0.0.0', 4433, configuration=configuration, create_protocol=FileServerQuicProtocol
#     )
#     print('QUIC Server running on 0.0.0.0:4433')

#     await asyncio.Event().wait()

# if __name__ == '__main__':
#     asyncio.run(run_quic_server())

import threading
import asyncio
from aioquic.asyncio.protocol import QuicConnectionProtocol
from aioquic.asyncio.server import serve
from aioquic.quic.configuration import QuicConfiguration
from aioquic.quic.events import StreamDataReceived, HandshakeCompleted
import time
import uuid
import os

class FileServerQuicProtocol(QuicConnectionProtocol):
    def quic_event_received(self, event):
        #print("receive event:" + str(event))
        #print("\n\n\n")
        try:
            
            if isinstance(event, HandshakeCompleted):
                print("Handshake finished")
            elif isinstance(event, StreamDataReceived):
                stream_id = event.stream_id
                #print(f"Received data, buffering and write to file")
                node_index = int(stream_id / 10)
                file_index = stream_id % 10
                filename = f"file{node_index}-{file_index}.txt"
                filepath = "transfer_directory/"
                if not os.path.exists(filepath):
                    os.makedirs(filepath)
                with open(filepath + filename, 'wb') as file:
                    file.write(event.data)
                    if event.data.endswith(b'\r\n'):
                        print("File received successfully")
                        self.send_response(stream_id)
        except Exception as e:
            print(
                "File transfer error (" + str(e) + ")"
            )

    def send_response(self, stream_id):
        response = b'File received successfully.\r\n'
        #self._quic.send_stream_data(stream_id, response, end_stream=True)
        #self.transmit()
        print("Response sent to client.")

class QuicServer(threading.Thread):
    def __init__(self, host='0.0.0.0', port=4433):
        super().__init__()
        self.host = host
        self.port = port
        self.configuration = QuicConfiguration(is_client=False)
        self.configuration.load_cert_chain('server.crt', 'server.key')
        self.time = 0
        
    def run(self):
        asyncio.run(self.start_async())

    async def start_async(self):
        await serve(
            self.host, self.port, configuration=self.configuration, create_protocol=FileServerQuicProtocol
        )
        print(f'QUIC Server running on {self.host}:{self.port}')
        await asyncio.Event().wait()     
    

    # async def run(self):
    #     await serve(
    #         self.host, self.port, configuration=self.configuration, create_protocol=FileServerQuicProtocol
    #     )
    #     print(f'QUIC Server running on {self.host}:{self.port}')
    #     await asyncio.Event().wait()

    # def start(self):
    #     asyncio.run(self.run())