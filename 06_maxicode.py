import zxing
import cv2
import numpy as np
import os

# Initialize the ZXing reader
reader = zxing.BarCodeReader()

# Load the MaxiCode image
image_path = "/home/assia/Downloads/OpenCV-Masterclass-main (2)/Decoding/image06.png"
image = cv2.imread(image_path)

# Preprocess if needed (for example, applying thresholding)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

# Save the preprocessed image temporarily
temp_image_path = 'processed_maxicode.png'
cv2.imwrite(temp_image_path, thresh)

# Decode the MaxiCode using ZXing by passing the file path of the preprocessed image
decoded = reader.decode(temp_image_path)

# Check if the MaxiCode was successfully decoded
if decoded:
    print(f"Decoded Data: {decoded.parsed}")
    print(f"Barcode Format: {decoded.format}")
    
    # Draw the bounding box around the MaxiCode (if points are available)
    if decoded.points:
        points = [(int(p.x), int(p.y)) for p in decoded.points]
        cv2.polylines(image, [np.array(points, dtype=np.int32)], True, (0, 255, 0), 2)
        
        # Annotate the decoded data beside the bounding box
        x, y = points[0]  # Take the first point of the bounding box
        cv2.putText(image, decoded.parsed, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    
    # Display the image with the MaxiCode highlighted and annotated
    cv2.imshow("MaxiCode with Annotation", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save the annotated image
    output_file = "decoded_maxicode.png"
    cv2.imwrite(output_file, image)
    print(f"Annotated image saved as {output_file}")
else:
    print("Failed to decode the MaxiCode.")
