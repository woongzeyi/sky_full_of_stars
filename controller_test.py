from machine import SPI

s = SPI(0)


while True: 
    s.write(bytearray(0x01))
    s.write(bytearray(0x42))
    print(s.read(7))