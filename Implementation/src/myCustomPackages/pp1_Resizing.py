"""
This module contains classes for image resizing using different interpolation techniques.

Classes:
- BilinearInp: Implements the Bilinear interpolation technique to resize an image.
- BiCubicInp: Implements the Bicubic interpolation technique to resize an image.
- LanczosResampling: Implements the Lanczos Resampling technique to resize an image.
- ImageResizerFactory: Creates objects of different interpolation techniques to resize an image.
- ImageResizing: Resize Image in a directory.
"""

import os
import cv2
from tqdm import tqdm

class BilinearInp:
    """
    This class implements the Bilinear interpolation technique to resize an image.
    """

    def __init__(self, target_size):
        self.target_size = target_size

    def resize(self, image_path):
        image = cv2.imread(image_path)
        return cv2.resize(image, self.target_size, interpolation=cv2.INTER_LINEAR)

class BiCubicInp:
    """
    This class implements the Bicubic interpolation technique to resize an image.
    """

    def __init__(self, target_size):
        self.target_size = target_size

    def resize(self, image_path):
        image = cv2.imread(image_path)
        return cv2.resize(image, self.target_size, interpolation=cv2.INTER_CUBIC)



class LanczosResampling:
    """
    This class implements the Lanczos Resampling technique to resize an image.
    """

    def __init__(self, target_size):
        self.target_size = target_size

    def resize(self, image_path):
        image = cv2.imread(image_path)
        return cv2.resize(image, self.target_size, interpolation=cv2.INTER_LANCZOS4)



class ImageResizerFactory:
    """
    This class is a factory class for creating objects of different interpolation techniques.
    """

    def __init__(self,target_size):
        self.resizers = {
            'Bilinear': BilinearInp(target_size),
            'BiCubic': BiCubicInp(target_size),
            'Lanczos': LanczosResampling(target_size)
        }

    def resize(self, image_path, interpolation_technique):
        if interpolation_technique in self.resizers:
            return self.resizers[interpolation_technique].resize(image_path)
        else:
            raise ValueError("Invalid interpolation technique")



class ImageResizing:
    """
    This class is used to resize images in a directory using different interpolation techniques.
    """
    def __init__(self, input_dir, output_dir, target_size):
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.resizer_factory = ImageResizerFactory(target_size)

    def resize_images(self, technique):
        files = list(os.walk(self.input_dir))
        for root, dirs, files in tqdm(os.walk(self.input_dir), total=len(files), desc="Resizing images"):
            for file in files:
                if file.endswith(('.png', '.jpg', '.jpeg')):
                    input_path = os.path.join(root, file)
                    output_dir = root.replace(self.input_dir, self.output_dir)
                    os.makedirs(output_dir, exist_ok=True)
                    output_path = os.path.join(output_dir, file)
                    print(f"Processing Image : {input_path}")
                    try:
                        resized_image = self.resizer_factory.resize(input_path, technique)
                        cv2.imwrite(output_path, resized_image)
                    except Exception as e:
                        print(f"Error processing file {input_path}: {e}")