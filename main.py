#Zip LED's together to have all 4 lights change at the same time.
#You can alter the the rgb values to change the color
All_LED = Kitronik_Move_Motor.create_move_motor_zipled(4)
All_LED.set_color(Kitronik_Move_Motor.colors(Kitronik_Move_Motor.rgb(255, 0, 255)))
All_LED.show()
basic.pause(1000)

#To control each light seperately, we've created a variable name (ex. LED_0 for the LED labeled 0)
#for each LED. Range will indicate which the Led you wish to control and how many subsequent
#lights respectively.  This allows for grouping as well. Set to the color of your choice and show.

#Changes LED 0 to purple.
LED_0 = All_LED.range(0, 1)
LED_0.set_color(Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.PURPLE))
LED_0.show()

#Changes LED 0 to red.
LED_1 = All_LED.range(1, 1)
LED_1.set_color(Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.RED))
LED_1.show()

#Changes LED 0 to blue.
LED_2 = All_LED.range(2, 1)
LED_2.set_color(Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.BLUE))
LED_2.show()

#Changes LED 0 to green.
LED_3 = All_LED.range(3, 1)
LED_3.set_color(Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.GREEN))
LED_3.show()

#The Robot will move forward until something is within 15cm of its distance sensor.
#If something is in the way, it will stop, honk and resume moving in 3 seconds.
def Do_not_cut_me_off():
    if Kitronik_Move_Motor.measure() < 15:
        Kitronik_Move_Motor.stop()
        Kitronik_Move_Motor.beep_horn()
        basic.pause(3000)
    else: Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.FORWARD, 20)

        
basic.forever(Do_not_cut_me_off)