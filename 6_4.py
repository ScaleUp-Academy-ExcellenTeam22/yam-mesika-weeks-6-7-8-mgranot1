import cv2

def find_code(path_image: str) -> str:
    """
    :param path_image: A path for an image in which a message is encrypted using black pixel locations.
    Go over the encrypted image column by column and find the black pixel.
    For each column the black pixel is converted to char.
    :return: A string of the encrypted message
    """
    image_with_code = cv2.imread(path_image)
    height = image_with_code.shape[0]
    width = image_with_code.shape[1]
    return "".join([chr(j) for i in range(width) for j in range(height) if image_with_code[j][i][0] != 255])


