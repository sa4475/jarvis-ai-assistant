import cv2

# Try to open the default camera (0)
cap = cv2.VideoCapture(0)

# Read one frame
ret, frame = cap.read()

# Print result
print("Camera status:", ret)

# Release the camera
cap.release()
