import os
import torchvision.transforms as transforms
import cv2
import numpy as np

def add_grayscale(image, image_file, images_path):
    """give image as input, writes grayscale images in the path specified"""
    grayscale_transformation = transforms.Compose([transforms.ToPILImage(), transforms.Grayscale()])
    grayscale_image = grayscale_transformation(image)
    grayscale_image = np.asarray(grayscale_image)
    cv2.imwrite(os.path.join(images_path,image_file + '_' + 'grayscale' + '.jpg'), grayscale_image)

def blur_image(image, image_file, images_path):
    """give image as input, writes blurred images in the path specified"""
    blur_transformation = transforms.Compose([transforms.ToPILImage(), transforms.GaussianBlur(kernel_size=(7, 13), sigma=(1.5, 1.5))])
    blurred_image = blur_transformation(image)
    blurred_image = np.asarray(blurred_image)
    cv2.imwrite(os.path.join(images_path,image_file + '_' + 'blur' + '.jpg'), blurred_image)

if __name__ == '__main__':
    images_path = r'PAN'
    for image_file in os.listdir(images_path):
        image = cv2.imread(os.path.join(images_path, image_file), cv2.IMREAD_COLOR)
        image_file_renamed = image_file.replace('.jpg', '').replace('.png', '')
        add_grayscale(image, image_file_renamed, images_path)
        blur_image(image, image_file_renamed, images_path)
