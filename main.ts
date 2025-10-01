// The Robot will move forward until something is within 10cm of its distance sensor.
// If something is in the way, it will stop, LEDS will change and resume moving in 3 seconds.
// Zip LED's together to have all 4 lights change at the same time
let All_LED = Kitronik_Move_Motor.createMoveMotorZIPLED(4)
function Do_not_cut_me_off() {
    Kitronik_Move_Motor.stop()
    // You can alter the the rgb values to change the color
    All_LED.setColor(Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.Red))
    All_LED.show()
    basic.pause(3000)
}

basic.forever(function on_forever2() {
    while (Kitronik_Move_Motor.measure() > 15) {
        All_LED.setColor(Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.Green))
        All_LED.show()
        Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.Forward, 10)
    }
    Do_not_cut_me_off()
})
