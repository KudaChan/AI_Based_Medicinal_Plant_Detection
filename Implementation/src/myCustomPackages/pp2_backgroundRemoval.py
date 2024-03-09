"""_summary_
    This module performs background removal on the images in a directory.
"""

import os
from rembg import remove
from PIL import Image
from io import BytesIO

class RemoveBackground:
    def __init__ (self, input_dir, output_dir):
        self.input_dir = input_dir
        self.output_dir = output_dir

    # Function to remove the background from the images in the input directory and save them to the output directory
    def remove_background(self):
        with open(self.input_dir, 'rb') as input_img:
            img = input_img.read()
            back_remove = remove(img, alpha_matting_background_threshold = 200)
            img_png = Image.open(BytesIO(back_remove))
            rgb_img = img_png.convert('RGB')
            rgb_img.save(self.output_dir, 'JPEG')


# C:\\Users\\kumar\\OneDrive\\Documents\\AI_Based_Medicinal_Plant_Detection\\Implementation\\temp_data\\preProcessed\\resizedData\\Lanczos\\Medicinal_leaf_dataset\\Aloevera\Aloevera_1.jpg

class Back_Removal_Initiator:
    def __init__ (self, input_dir, output_dir):
        self.input_dir = input_dir
        self.output_dir = output_dir

    def remove_background(self):
        files = list(os.walk(self.input_dir))
        for root, dirs, files in os.walk(self.input_dir):
            for file in files:
                if file.endswith(('.png', '.jpg', '.jpeg')):
                    input_path = os.path.join(root, file)
                    output_dir = root.replace(self.input_dir, self.output_dir)
                    os.makedirs(output_dir, exist_ok=True)
                    output_path = os.path.join(output_dir, file)
                    print(f"Processing Image : {input_path}")
                    RemoveBackground(input_path, output_path).remove_background()
                    print(f"Image Processed : {output_path}")

if __name__ == "__main__":
    input_dir = "Implementation\\temp\\preProcessed\\resizedData"
    output_dir = "Implementation\\temp\\preProcessed\\noBackgrnd"
    initiator = Back_Removal_Initiator(input_dir, output_dir)
    initiator.remove_background()