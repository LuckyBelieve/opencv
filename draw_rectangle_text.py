import cv2

# reading the image
image = cv2.imread("assignment-001-given.jpg")

# Draw a green rectangle on the image
cv2.rectangle(image, (270, 213), (981, 924), (0, 255, 0), 9)


text = "RAH972U"
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 2
thickness = 6
text_color = (0, 255, 0)

(text_width, text_height), baseline = cv2.getTextSize(
    text, cv2.FONT_HERSHEY_SIMPLEX, 2, 6
)

x, y = 900, 180

overlay = image.copy()

background_start = (x, y - text_height - 15)
background_end   = (x + text_width, y + 15)

cv2.rectangle(overlay, background_start, background_end, (0, 0, 0), -1)

cv2.addWeighted(overlay, 0.4, image, 1 - 0.4, 0, image)

cv2.putText(image, text, (x, y), font, 2, (0, 255, 0), 6, cv2.LINE_AA)

cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.imwrite("assignment-001-result.jpg", image)
cv2.destroyAllWindows()