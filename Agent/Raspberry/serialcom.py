import serial

port = serial.Serial("/dev/ttyUSB0", baudrate=115200, timeout=3.0)


def push_position(data1, data2, data3, data4, data5, data6):
    frame = 22
    cs = 0
    command = [frame]
    for data in [data1, data2, data3, data4, data5, data6]:
        HighBData = data >> 8
        cs += HighBData
        command.append(HighBData)

        LowBData = data & 0xFF
        cs += LowBData
        command.append(LowBData)

    cs &= 0xFF
    command.append(cs)
    command.append(frame)

    port.write(serial.to_bytes(command))
    port.close()

