import serial
import sys

# The CH340 accepts a binary coded message to turn on/off or query the status
onMsg  = [ b'\xA0\x01\x01\xA2', b'\xA0\x02\x01\xA3', b'\xA0\x03\x01\xA4', b'\xA0\x04\x01\xA5' ]
offMsg = [ b'\xA0\x01\x00\xA1', b'\xA0\x02\x00\xA2', b'\xA0\x03\x00\xA3', b'\xA0\x04\x00\xA4' ]
statMsg = b'\xFF'
channel=0  # control channel 0 only
baudrate=9600

def getSerialPort(port):
    try:
       return serial.Serial(port, baudrate)
    except:
       return None

#
# argument: COM# [NC|NO]
#
argc=len(sys.argv)
if (argc>2):
    ComPort = sys.argv[1].upper()
    Control = sys.argv[2].upper()
else:
    print("Usage: UsbRelayCh340 COM# [NC|NO]")        
    sys.exit()

serialPort = getSerialPort(ComPort)

if (serialPort != None):
    if Control=='NO':
        serialPort.write(onMsg[channel])
    else:
        serialPort.write(offMsg[channel])
else:
    print("No serial port "+ComPort+" found.")        
