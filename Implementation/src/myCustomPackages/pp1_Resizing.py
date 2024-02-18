"""
This module contains classes for image resizing using different interpolation techniques.

Classes:
- BilinearInp: Implements the Bilinear interpolation technique to resize an image.
- BiCubicInp: Implements the Bicubic interpolation technique to resize an image.
- LanczosResampling: Implements the Lanczos Resampling technique to resize an image.
"""

import os
import cv2

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