import serial

port = serial.Serial("/dev/ttyACM0", baudrate=115200, timeout=3.0)


def push_position(data):
    if len(data) != 6:
        print('Format error')
        return

    frame = 22
    cs = 0
    command = [frame]
    for angle in data:
        HighBData = angle >> 8
        cs += HighBData
        command.append(HighBData)

        LowBData = angle & 0xFF
        cs += LowBData
        command.append(LowBData)

    cs &= 0xFF
    command.append(cs)
    command.append(frame)
    port.write(serial.to_bytes(command))


def deinit_serial():
    port.close()
