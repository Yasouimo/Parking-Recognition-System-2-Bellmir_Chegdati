from ultralytics import YOLO
import cv2

# Load your YOLO model
model = YOLO('best.pt')  # Replace 'best.pt' with your model path

# Run inference on the image
results = model.predict(source='Parking-Lot-Accidents.jpg', show=False, line_width=1)  # Do not automatically show

# Render the results on the image
annotated_frame = results[0].plot()

# Display the image and keep the window open
cv2.imshow("YOLO Detections", annotated_frame)
cv2.waitKey(0)  # Wait indefinitely for a key press
cv2.destroyAllWindows()  # Close the window
