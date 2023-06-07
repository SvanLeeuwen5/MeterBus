from machine import UART
import time

class MbusCommunicator:
    def __init__(self, ):
        self.uart = UART(tx=17, rx=16, baudrate=9600, timeout=1)

    def send_short_frame(self, address):
        frame = bytearray([0x10, 0x5B, address, 0x00, 0x16]) # | Start | C-Field | Address | CheckSum | Stop |
        self.uart.write(frame)
        time.sleep(0.1)  # Wait for the response to arrive

    def read_response(self):
        response = self.uart.read(1792)  # Read 7 long frames (RSP_UD) of 256 bytes
        return response

    def close_connection(self):
        self.uart.deinit()