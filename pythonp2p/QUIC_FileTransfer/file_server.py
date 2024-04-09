import asyncio
from aioquic.asyncio.protocol import QuicConnectionProtocol
from aioquic.asyncio.server import serve
from aioquic.quic.configuration import QuicConfiguration
from aioquic.quic.events import StreamDataReceived, HandshakeCompleted

class FileServerQuicProtocol(QuicConnectionProtocol):
    
    def quic_event_received(self, event):
        if isinstance(event, HandshakeCompleted):
            print("Handshake finished")
        elif isinstance(event, StreamDataReceived):
            print(f"Received data, buffering and write to file")
            with open('received_file.txt', 'wb') as file:
                file.write(event.data)
                if event.data.endswith(b'\r\n'):
                    print("File received successfully")
                    self.send_response()

    def send_response(self):
        response = b'File received successfully.\r\n'
        self._quic.send_stream_data(0, response, end_stream=True)
        self.transmit()
        print("Response sent to client.")

async def run_quic_server():
    configuration = QuicConfiguration(is_client=False)
    configuration.load_cert_chain('server.crt', 'server.key')

    await serve(
        '0.0.0.0', 4433, configuration=configuration, create_protocol=FileServerQuicProtocol
    )
    print('QUIC Server running on 0.0.0.0:4433')

    await asyncio.Event().wait()

if __name__ == '__main__':
    asyncio.run(run_quic_server())
