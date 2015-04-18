import pyb

class Cerbot():

    MOTOR_L_DIR = pyb.Pin('MOTOR_L_DIR', pyb.Pin.OUT_PP)
    MOTOR_L_PWM = pyb.Pin('MOTOR_L_PWM', pyb. Pin.OUT_PP)
    MOTOR_R_DIR = pyb.Pin('MOTOR_R_DIR', pyb.Pin.OUT_PP)
    MOTOR_R_PWM = pyb.Pin('MOTOR_R_PWM', pyb. Pin.OUT_PP) 

    def drive(self, direction: str, speed: int):

        #direction = 'FWD' | 'RWD'
        #speed = 0 .. 100

        if direction == 'FWD':
            self.MOTOR_L_DIR.low()
            self.MOTOR_R_DIR.high()
        elif direction == 'RWD':
            self.MOTOR_L_DIR.high()
            self.MOTOR_R_DIR.low()
        else:
            raise TypeError

        if type(speed) == int:
            if speed == 1:
                self.MOTOR_L_PWM.high()
                self.MOTOR_R_PWM.high()
            elif speed == 0:
                self.MOTOR_L_PWM.low()
                self.MOTOR_R_PWM.low()
            else:
                pass
        else:
            raise TypeError

    def rotate(self, direction: str, speed: int):

        #direction = 'LEFT' | 'RIGHT'
        #speed = 0 .. 100

        if direction == 'LEFT':
            self.MOTOR_L_DIR.high()
            self.MOTOR_R_DIR.high()
        elif direction == 'RIGHT':
            self.MOTOR_L_DIR.low()
            self.MOTOR_R_DIR.low()
        else:
            raise TypeError

        if type(speed) == int:
            if speed == 1:
                self.MOTOR_L_PWM.high()
                self.MOTOR_R_PWM.high()
            elif speed == 0:
                self.MOTOR_L_PWM.low()
                self.MOTOR_R_PWM.low()
            else:
                pass
        else:
            raise TypeError
