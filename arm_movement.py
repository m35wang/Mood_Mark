from arm_arduino import ArduinoCommunictaion

class ArmAction():
    def __init__(self):
        self.arduino = ArduinoCommunictaion()

    def collect_dark_orange_stamp(self):
        file = 'arm_positions/dark_orange.txt'

        print("Moving arm to collect dark orange ink.")
        self.arduino.read_file_send_to_arduino(filelocation=file)
    
    def collect_light_orange_stamp(self):
        file = 'arm_positions/light_orange.txt'

        print("Moving arm to collect light orange ink.")
        self.arduino.read_file_send_to_arduino(filelocation=file)

    def collect_dark_blue_stamp(self):
        file = 'arm_positions/dark_blue.txt'

        print("Moving arm to collect dark blue ink.")
        self.arduino.read_file_send_to_arduino(filelocation=file)

    def collect_light_blue_stamp(self):
        file = 'arm_positions/light_blue.txt'

        print("Moving arm to collect light blue ink.")
        self.arduino.read_file_send_to_arduino(filelocation=file)
    
    def collect_dark_green_stamp(self):
        file = 'arm_positions/dark_green.txt'

        print("Moving arm to collect dark green ink.")
        self.arduino.read_file_send_to_arduino(filelocation=file)

    def collect_light_green_stamp(self):
        file = 'arm_positions/light_green.txt'

        print("Moving arm to collect light green ink.")
        self.arduino.read_file_send_to_arduino(filelocation=file)

    def draw_row_1(self):
        file = 'arm_positions/row_1.txt'

        print("Moving arm to draw 1rst stamp.")
        self.arduino.read_file_send_to_arduino(filelocation=file)

    def draw_row_2(self):
        file = 'arm_positions/row_2.txt'

        print("Moving arm to draw 2rnd stamp.")
        self.arduino.read_file_send_to_arduino(filelocation=file)
    
    def draw_row_3(self):
        file = 'arm_positions/row_3.txt'

        print("Moving arm to draw 3rd stamp.")
        self.arduino.read_file_send_to_arduino(filelocation=file)