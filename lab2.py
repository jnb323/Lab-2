import time

from Led import *
led=Led()

from Motor import *            
PWM=Motor()          

from Ultrasonic import *
ultrasonic=Ultrasonic()

from ADC import *
adc=Adc()

from Buzzer import *
buzzer=Buzzer()

def lab2_move():
    PWM.setMotorModel(1000,1000,1000,1000)      #Move forward 2 seconds
    time.sleep(2)
    PWM.setMotorModel(0, 0, 0, 0)
    time.sleep(1)
    
    PWM.setMotorModel(-1500,-1500,2000,2000)    #Rotate 90 degrees
    time.sleep(0.5)
    PWM.setMotorModel(0, 0, 0, 0)
    time.sleep(1)
    
    led.ledIndex(0x01,255,0,0)                  #LED 0 colored red
    time.sleep(2)
    
    PWM.setMotorModel(1000,1000,1000,1000)      #Move forward 2 seconds
    time.sleep(2)
    PWM.setMotorModel(0, 0, 0, 0)
    time.sleep(1)
    
    PWM.setMotorModel(-1500,-1500,2000,2000)    #Rotate 90 degrees
    time.sleep(0.5)
    PWM.setMotorModel(0, 0, 0, 0)
    time.sleep(1)
    
    led.ledIndex(0x02,0,0,255)                  #LED 1 colored blue
    time.sleep(1)
    
    PWM.setMotorModel(1000, 1000, 1000, 1000)   #Move forward 2 seconds
    time.sleep(2)
    PWM.setMotorModel(0, 0, 0, 0)
    time.sleep(1)
    
    PWM.setMotorModel(-1500,-1500,2000,2000)    #Rotate 90 degrees
    time.sleep(0.5)
    PWM.setMotorModel(0, 0, 0, 0)
    time.sleep(1)
    
    led.ledIndex(0x04, 0, 255, 0)               #LED 2 colored green
    time.sleep(1)
    
    PWM.setMotorModel(1000, 1000, 1000, 1000)   #Move forward 2 seconds
    time.sleep(2)
    PWM.setMotorModel(0, 0, 0, 0)
    time.sleep(1)
    
    PWM.setMotorModel(-1500,-1500,2000,2000)    #Rotate 90 degrees
    time.sleep(0.5)
    PWM.setMotorModel(0, 0, 0, 0)
    time.sleep(1)
    
    led.ledIndex(0x08, 255, 255, 0)             #LED 3 colored yellow
    time.sleep(1)
    
    buzzer.run('1')                             #Beep buzzer for 1 second
    time.sleep(1)
    buzzer.run('0')
    
    led.ledIndex(0x01, 0, 0, 0)
    led.ledIndex(0x02, 0, 0, 0)
    led.ledIndex(0x04, 0, 0, 0)
    led.ledIndex(0x08, 0, 0, 0)

if __name__ == '__main__':
    lab2_move()