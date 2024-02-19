import os
import cv2


from myCustomPackages import pp1_Resizing



"""_summary_
    Entry Point of the code.
"""
if __name__ == "__main__":
    input_dir = 'Implementation/data/unProcessed'
    output_dir = 'Implementation/data/preProcessed/resizedData'

    # Create a resizer that uses Bicubic interpolation
    resizeTechnique = ['Bilinear', 'BiCubic', 'Lanczos']
    target_size = (224, 224)
    for technique in resizeTechnique:
        # Create an instance of ImageResizing and use it to resize all images in the input directory
        image_resizing = pp1_Resizing.ImageResizing(input_dir, f"{output_dir}/{technique}", target_size)
        image_resizing.resize_images(technique)