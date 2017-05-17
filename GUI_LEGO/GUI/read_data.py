import serial
import time

# # Serial port parameters
serial_speed = 9600
serial_port = '/dev/tty.HC-06-DevB' # bluetooth shield hc-06



def print_data():
    print "conecting to serial port ..."
    ser = serial.Serial(serial_port, serial_speed, timeout=1)
 #   print "sending message to turn on PIN 13 ..."
#    ser.write('1')

#    while(True):
    print "recieving message from arduino ..."
    data = ser.readline()

    if (data != ""):
        print "arduino says: %s" % data
        #time.sleep(1)
    return(data)