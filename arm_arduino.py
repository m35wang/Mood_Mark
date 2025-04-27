import serial
import time
import os

#the structure of the data is: base, shoulder, elbow, wrist1, wrist2, gripper, speed 

class ArduinoCommunictaion():
    def __init__(self):
        self.speed=9600 #baud rate for Arduino com
        self.rest=3 #delay between movements
        self.port='COM4'

    #opens text file to read arm positions
    def process_file(self, filename):
        try:
            with open(filename, 'r') as file:
                lines = [line.strip() for line in file if line.strip()]
                
            with serial.Serial(self.port, self.speed, timeout=1) as ser:
                time.sleep(self.rest)  # Arduino reset delay
                print(f"\nSending {len(lines)} commands from {filename}:")
                
                for line in lines:
                    ser.write((line + '\n').encode('utf-8'))
                    print(f"Sent: {line}")
                    time.sleep(self.rest)  # 3-second delay between commands
                
        except FileNotFoundError:
            print(f"Error: File {filename} not found!")
            exit()
        except serial.SerialException as e:
            print(f"Error: {str(e)}")
            exit()

    def read_file_send_to_arduino(self, filelocation):
        filename = filelocation
        if not os.path.exists(filename):
            print(f"\nError: {filename} not found in script directory!")
            return
        
        self.process_file(filename=filename)
