from gpiozero import DistanceSensor
from gpiozero import Servo, AngularServo
from time import sleep

# sensor = DistanceSensor(21,20)
# while True:
#     print(sensor.distance)

# servo = AngularServo(16, min_angle=0, max_angle=180, min_pulse_width=0.0006, max_pulse_width=0.0024)

# print(servo.angle)

# servo.angle = 0.0
# while True:
#     v = input("enter a number between 0 and 180 \n")
#     v = float(v)
#     print(type(v))
#     if v<=180 and v >= 0:
#         servo.angle = v
#         print(servo.angle)



# def move_detect():
#     while True:
#         while sensor.distance == 1.0:
#             for i in range (180):
#                 servo.angle = float(i)
#                 sleep(0.05)
#             for i in range (180, 0, -1):
#                 servo.angle = float(i)
#                 sleep(0.05)




        # if sensor.distance < 1.0:
        #     v = 70.0
        #     v = float(v)
        #     servo.angle = v
        # else:
        #     servo.angle = 0.0



# move_detect()

class Motion:
    def __init__(self):
        self.sensor = DistanceSensor(21,20)
        self.servo = AngularServo(16, min_angle=0, max_angle=180, min_pulse_width=0.0006, max_pulse_width=0.0024)

    def move_detect(self):
        # while True:
        while self.sensor.distance == 1.0:
            for i in range (180):
                self.servo.angle = float(i)
                sleep(0.05)
            for i in range (180, 0, -1):
                self.servo.angle = float(i)
                sleep(0.05)
