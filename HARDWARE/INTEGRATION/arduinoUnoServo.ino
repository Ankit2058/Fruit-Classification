#include <Servo.h>
#include <LiquidCrystal_I2C.h>

Servo myServo;
LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
    myServo.attach(9);  // Attach servo to pin 9
    Serial.begin(9600); // Start serial communication at 9600 baud rate
    lcd.init();         // Initialize the LCD 
    lcd.backlight();    // Turn on the backlight 
    lcd.clear();  
    lcd.print(" FRUIT "); 
    lcd.setCursor(0, 1);
    lcd.print("SEGREGATION");
}

void loop() {
    if (Serial.available() > 0) {
        int input = Serial.parseInt(); // Read integer input

        if (input == 1) {
            lcd.clear();
            lcd.setCursor(0, 0);
            lcd.print("Moving 135"); // Display the action
            myServo.write(100);         // Move to 180 degrees
            delay(200);                // Hold for 1 second
            myServo.write(90);
        } 
        else if (input == 0) {
            lcd.clear();
            lcd.setCursor(0, 0);
            lcd.print("Moving 360");  // Display the action
            myServo.write(0);          // Move to 90 degrees
            delay(200);                // Hold for 1 second
            myServo.write(90);
        }

        // Clear the serial buffer to avoid repeated commands
        while (Serial.available() > 0) {
            Serial.read(); // Clear any remaining input in the buffer
        }
    }
}
