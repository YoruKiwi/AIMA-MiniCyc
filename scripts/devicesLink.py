import serial
import serial.tools.list_ports

# ser = serial.Serial(
#     port='COM1',
#     baudrate=9600,
#     parity=serial.PARITY_ODD,
#     stopbits=serial.STOPBITS_TWO,
#     bytesize=serial.SEVENBITS
# )

def send_data(data, ser):
    ser.write(data.encode())
    ser.close()

def read_data(ser):
    data = ser.readline().decode().strip()
    ser.close()

    return data

def list_available_ports():
    ports = serial.tools.list_ports.comports()
    available_ports = []

    for port in ports:
        available_ports.append(port.device)
        
    # Add PicoScope devices
    from pico_sdk import PicoDevice
    found = PicoDevice.enumerate()
    for device in found:
        available_ports.append("PicoScope " + device.variant + " with serial " + device.serial)


    return available_ports