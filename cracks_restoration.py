import cv2
import numpy as np

# Function to load and restore the damaged image
def restore_image(image_path):
    # Load the damaged photo
    image = cv2.imread(image_path)
    
    # Check if the image was loaded successfully
    if image is None:
        print("Error: Unable to load image. Please check the path.")
        return

    # Show the original damaged photo
    cv2.imshow('Original Damaged Photo', image)
    cv2.waitKey(0)

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Canny edge detection to find cracks
    edges = cv2.Canny(gray, threshold1=100, threshold2=200)

    # Check if edges were detected
    if edges is None:
        print("Error: No edges detected.")
        return

    # Dilate edges to make a thicker mask
    kernel = np.ones((5, 5), np.uint8)
    dilated_edges = cv2.dilate(edges, kernel, iterations=1)

    # Invert the mask to use it for inpainting
    mask = cv2.bitwise_not(dilated_edges)

    # Inpaint the image using the mask
    restored = cv2.inpaint(image, mask, inpaintRadius=3, flags=cv2.INPAINT_TELEA)

    # Show results
    cv2.imshow('Detected Cracks', dilated_edges)
    cv2.imshow('Restored Image', restored)
    
    # Wait for a key press and then close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Main code execution
if __name__ == "__main__":
    # Ask the user for the damaged image path
    image_path = input("Enter the path to the damaged image: ")
    restore_image(image_path)
