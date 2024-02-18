import os
import cv2
from tqdm import tqdm


from myCustomPackages import pp1_Resizing


"""_summary_
    Image Preprocessing:
"""
class ImageResizing:
    def __init__(self, input_dir, output_dir, resizer):
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.resizer = resizer

    def resize_images(self):
        files = list(os.walk(self.input_dir))
        for root, dirs, files in tqdm(os.walk(self.input_dir), total=len(files), desc="Resizing images"):
            for file in files:
                if file.endswith(('.png', '.jpg', '.jpeg')):
                    input_path = os.path.join(root, file)
                    output_dir = root.replace(self.input_dir, self.output_dir)
                    os.makedirs(output_dir, exist_ok=True)
                    output_path = os.path.join(output_dir, file)
                    resized_image = self.resizer.resize(input_path)
                    cv2.imwrite(output_path, resized_image)

class ResizerSelector:
    def __init__(self, target_size):
        self.factory = pp1_Resizing.ImageResizerFactory(target_size)



"""_summary_
    Entry Point of the code.
"""
if __name__ == "__main__":
    input_dir = 'Implementation/data/unProcessed'
    output_dir = 'Implementation/data/preProcessed/resizedData'

    # Create a resizer that uses Bicubic interpolation
    resizeTechnique = ['Bilinear', 'BiCubic', 'Lanczos']
    factory = pp1_Resizing.ImageResizerFactory((224, 224))
    for technique in resizeTechnique:
        resizer = factory.resize[technique]

        # Create an instance of ImageResizing and use it to resize all images in the input directory
        image_resizing = ImageResizing(input_dir, f"{output_dir}/{technique}", resizer)
        image_resizing.resize_images()