import cv2
import pyautogui
import numpy as np

# Select the region of interest (ROI)
roi = cv2.selectROI("Select the region of interest:")

# Start the video writer
out = cv2.VideoWriter("output.mp4", cv2.VideoWriter_fourcc(*'mp4v'), 30, (roi[2], roi[3]))

# Capture frames
while True:
    # Capture a screenshot
    img = pyautogui.screenshot()

    # Convert the screenshot to a numpy array
    frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

    # Get the ROI from the frame
    roi_frame = frame[int(roi[1]):int(roi[1] + roi[3]), int(roi[0]):int(roi[0] + roi[2])]

    # Write the ROI frame to the output file
    out.write(roi_frame)

    # Display the frame
    cv2.imshow("Frame", frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video writer
out.release()

# Close all windows
cv2.destroyAllWindows()
