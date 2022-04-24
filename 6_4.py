import cv2

def find_code(path_image):
    """
    :param path_image: Image path containing pixels encrypted in pixels
    Go over the encrypted image column by column and find the black pixel.
    For each column the black pixel is converted to char.
    :return: A string of the encrypted message
    """
    image_with_code = cv2.imread(path_image)
    height, width, channels = image_with_code.shape
    return "".join([chr(j) for i in range(width) for j in range(height) if image_with_code[j][i][0] != 255])


