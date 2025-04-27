#Braccio send and receive Arduino, by Fabio D'Agnano, including the Braccio Library  by Andrea Martino.
#This example is in the public domain.


import serial
import serial.tools.list_ports
import time
import os

#the structure of the data is: base, shoulder, elbow, wrist1, wrist2, gripper, speed 

#these are the libraries to import. Use pyp install pyserial

speed=9600 #baud rate for Arduino com
rest=3 #delay between movements
#this will list the available serial ports. When you run the program, use 1 to select the first port and so on.
def list_com_ports():
    ports = serial.tools.list_ports.comports()
    return [port.device for port in ports]

def select_com_port():
    com_ports = list_com_ports()
    if not com_ports:
        print("No COM ports found!")
        exit()
        
    print("\nAvailable COM ports:")
    for i, port in enumerate(com_ports, 1):
        print(f"{i}. {port}")
    
    while True:
        try:
            choice = int(input("\nSelect COM port (1-{}): ".format(len(com_ports))))
            if 1 <= choice <= len(com_ports):
                return com_ports[choice-1]
            print("Invalid selection. Try again.")
        except ValueError:
            print("Please enter a number.")

#this will send the values row by row. If you are not happy with the baud speed, change it accordingly.
def send_to_serial(port, data):
    try:
        with serial.Serial(port, speed, timeout=1) as ser:
            time.sleep(2)  # Arduino reset delay
            ser.write(data.encode('utf-8'))
            print(f"Sent: {data.strip()}")
    except serial.SerialException as e:
        print(f"Error: {str(e)}")
        exit()

#this opens the txt file that you can use with copy/past to work with Grasshopper
def process_file(port, filename):
    try:
        with open(filename, 'r') as file:
            lines = [line.strip() for line in file if line.strip()]
            
        with serial.Serial(port, speed, timeout=1) as ser:
            time.sleep(rest)  # Arduino reset delay
            print(f"\nSending {len(lines)} commands from {filename}:")
            
            for line in lines:
                ser.write((line + '\n').encode('utf-8'))
                print(f"Sent: {line}")
                time.sleep(rest)  # 3-second delay between commands
                
    except FileNotFoundError:
        print(f"Error: File {filename} not found!")
        exit()
    except serial.SerialException as e:
        print(f"Error: {str(e)}")
        exit()

def main():
    # COM port selection
    selected_port = select_com_port()
    print(f"\nSelected port: {selected_port}")
    
    # Mode selection
    while True:
        mode = input("\nChoose mode:\n1. Direct send\n2. List from file\n> ")
        if mode in ['1', '2']:
            break
        print("Invalid choice. Enter 1 or 2")
    
    # Handle modes
    if mode == '1':
        print("\nDirect mode - type commands (type 'exit' to quit)")
        while True:
            cmd = input("Enter command: ").strip()
            if cmd.lower() == 'exit':
                break
            if cmd:
                send_to_serial(selected_port, cmd + '\n')
    else:
        filename = 'arm_positions/row_3.txt'
        if not os.path.exists(filename):
            print(f"\nError: {filename} not found in script directory!")
            return
        process_file(selected_port, filename)

if __name__ == "__main__":
    main()