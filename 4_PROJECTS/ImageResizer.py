import cv2

# Configurable parameters
source = "PROJECTS\Resources\Akash.jpg"
destination = "Aakash.png"
scale_percent = 50

src = cv2.imread(source, cv2.IMREAD_UNCHANGED)

# Check if the image is loaded successfully
if src is None:
    print("Error: Unable to load image.")
else:
    # Calculate the 50% of the original dimensions
    new_width = int(src.shape[1] * scale_percent / 100)
    new_height = int(src.shape[0] * scale_percent / 100)

    # Resize image
    output = cv2.resize(src, (new_width, new_height))

    # Save resized image
    cv2.imwrite(destination, output)

    # Display resized image
    cv2.imshow(destination, output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
