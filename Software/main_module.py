import serial
import cv2
import numpy as np
import time
from model_module import BananaClassifier

# Arduino Serial Port
arduino_port = 'COM3'  # Replace with your COM port
baud_rate = 9600

# Path to the saved model parameters
model_path = r"C:\Users\Asus\Documents\College Project\Major\Software\resnet_model_parameters_3.0.pth"

# Initialize the classifier
classifier = BananaClassifier(model_path)

# Real-time classification with Arduino integration
def real_time_classification(classifier, arduino):
    cap = cv2.VideoCapture(0)  # Use the default camera
    print("Starting real-time banana classification...")
    last_capture_time = 0  # Track the time of the last capture
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame. Exiting...")
            break

        # Display the frame for visualization
        cv2.imshow("Banana Classifier", frame)
        current_time = time.time()
        if current_time - last_capture_time >= 4:
            # Update the last capture time
            last_capture_time = current_time
            # Classify the banana every few seconds
            start_time = time.time()
            prediction = classifier.classify(frame)
            end_time = time.time()

            # Output the result
            if prediction == 1:
                print(f"Rotten Banana Detected (Time: {end_time - start_time:.2f}s)")
                arduino.write(b'1\n')
            # I will probably return 1 later for hardware control
            else:
                print(f"Fresh Banana Detected (Time: {end_time - start_time:.2f}s)")
                arduino.write(b'0\n')
            # I will probably return 0 later for hardware control


        # Wait for a keypress to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
            break

    cap.release()
    cv2.destroyAllWindows()
    arduino.close()  # Close the serial connection

# Main function
if __name__ == "__main__":
    # Connect to Arduino
    arduino = serial.Serial(arduino_port, baud_rate, timeout=1)
    time.sleep(2)  # Wait for Arduino to initialize

    # Start real-time classification
    real_time_classification(classifier, arduino)
