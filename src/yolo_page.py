import streamlit as st
import cv2
import numpy as np
from ultralytics import YOLO

# Constants
WEIGHTS_PATH = 'models/best.pt'
THRESHOLD = 0.5

# Initialize session state
if 'reserved_spots' not in st.session_state:
    st.session_state.reserved_spots = []
if 'model' not in st.session_state:
    st.session_state.model = YOLO(WEIGHTS_PATH)
if 'current_file' not in st.session_state:
    st.session_state.current_file = None

def process_image(image):
    """Process image with YOLO and handle reservations"""
    frame = cv2.imdecode(np.frombuffer(image, np.uint8), cv2.IMREAD_COLOR)
    if frame is None:
        st.error("Error: Unable to load image.")
        return

    results = st.session_state.model.predict(frame, conf=THRESHOLD)
    mask = frame.copy()

    # Store spot positions to maintain consistent numbering
    if 'spot_positions' not in st.session_state:
        st.session_state.spot_positions = []
        for result in results[0].boxes:
            x1, y1, x2, y2 = map(int, result.xyxy[0])
            st.session_state.spot_positions.append((x1, y1, x2, y2))

    # Process each detection
    for idx, result in enumerate(results[0].boxes):
        spot_id = idx + 1
        x1, y1, x2, y2 = map(int, result.xyxy[0])
        class_id = int(result.cls[0])  # 0 = empty, 1 = occupied
        
        # Determine color based on status
        if spot_id in st.session_state.reserved_spots:
            color = (255, 0, 0)  # Blue for reserved
        elif class_id == 1:
            color = (0, 0, 255)  # Red for occupied
        else:
            color = (0, 255, 0)  # Green for empty

        # Draw semi-transparent overlay
        overlay = mask.copy()
        cv2.rectangle(overlay, (x1, y1), (x2, y2), color, -1)
        cv2.addWeighted(overlay, 0.3, mask, 0.7, 0, mask)
        
        # Draw border
        cv2.rectangle(mask, (x1, y1), (x2, y2), color, 2)

        # Add spot number label inside the box
        label = f"#{spot_id}"
        font_scale = 0.7
        thickness = 2
        (text_w, text_h), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, font_scale, thickness)
        text_x = x1 + (x2 - x1 - text_w) // 2
        text_y = y1 + (y2 - y1 + text_h) // 2
        
        # Draw label background
        cv2.rectangle(mask, 
                     (text_x - 5, text_y - text_h - 5),
                     (text_x + text_w + 5, text_y + 5),
                     color, -1)
        # Draw label text
        cv2.putText(mask, label, (text_x, text_y), 
                    cv2.FONT_HERSHEY_SIMPLEX, font_scale, (255, 255, 255), thickness)

    return cv2.cvtColor(mask, cv2.COLOR_BGR2RGB)

def handle_reservation(spot_id, results):
    """Handle spot reservation with validation"""
    if not results or not results[0].boxes:
        st.error("No parking spots detected")
        return False

    if spot_id <= 0 or spot_id > len(results[0].boxes):
        st.error(f"Invalid spot number: {spot_id}")
        return False

    # Check if spot is already reserved
    if spot_id in st.session_state.reserved_spots:
        st.error(f"Spot #{spot_id} is already reserved")
        return False

    # Check if spot is occupied (class_id = 1)
    class_id = int(results[0].boxes[spot_id-1].cls[0])
    if class_id == 1:
        st.error(f"Spot #{spot_id} is occupied and cannot be reserved")
        return False

    # Add valid reservation
    st.session_state.reserved_spots.append(spot_id)
    st.success(f"Spot #{spot_id} reserved successfully!")
    return True

def run():
    """Main Streamlit interface"""
    st.title("Parking Space Detection with Reservation")

    # File upload
    uploaded_file = st.file_uploader("Upload image or video", type=["jpg", "jpeg", "png", "mp4"])

    # Check if file was removed
    if not uploaded_file and st.session_state.current_file is not None:
        st.session_state.reserved_spots = []
        st.session_state.current_file = None
        if 'spot_positions' in st.session_state:
            del st.session_state.spot_positions

    # Reservation interface
    col1, col2 = st.columns(2)
    with col1:
        spot_input = st.text_input("Enter spot number to reserve:")
    with col2:
        reserve_button = st.button("Reserve")

    if uploaded_file:
        # Update current file
        st.session_state.current_file = uploaded_file.name

        if "image" in uploaded_file.type:
            image = uploaded_file.read()
            results = st.session_state.model.predict(image, conf=THRESHOLD)
            
            if reserve_button and spot_input.isnumeric():
                handle_reservation(int(spot_input), results)
            
            result_image = process_image(image)
            st.image(result_image, caption="Processed image", use_column_width=True)

        elif "video" in uploaded_file.type:
            video_bytes = uploaded_file.read()
            temp_file = "temp_video.mp4"

            with open(temp_file, "wb") as f:
                f.write(video_bytes)

            cap = cv2.VideoCapture(temp_file)
            frame_placeholder = st.empty()

            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break

                # Process reservation if requested
                if reserve_button and spot_input.isnumeric():
                    results = st.session_state.model.predict(frame, conf=THRESHOLD)
                    handle_reservation(int(spot_input), results)
                    reserve_button = False  # Reset button

                # Process and display frame
                result_frame = process_image(cv2.imencode('.jpg', frame)[1].tobytes())
                frame_placeholder.image(result_frame, caption="Processing...", use_column_width=True)

            cap.release()

if __name__ == "__main__":
    run()
