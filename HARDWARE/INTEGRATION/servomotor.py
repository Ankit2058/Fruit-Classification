import serial
import time

# Initialize the serial connection to Arduino (replace 'COM3' with your actual port)
arduino = serial.Serial('COM3', 9600, timeout=1)  # Adjust 'COM3' based on your system
time.sleep(2)  # Allow time for the connection to establish

# Loop to continuously ask for input and send to Arduino
while True:
    # Get user input
    user_input = input("Enter 1 to rotate left, 0 to rotate right, 'exit' to exit the interface: ")
    
    if user_input == "exit":
        break  # Exit the loop if the user types 'exit'
    
    # Validate and send the input
    if user_input in ["1", "0"]:
        arduino.write(f"{user_input}\n".encode())  # Send the user input to Arduino
        print(f"Sent {user_input} to Arduino")
    else:
        print("Invalid input. Please enter 1, 0 or 'exit'.")

# Close the Arduino connection when done
arduino.close()
