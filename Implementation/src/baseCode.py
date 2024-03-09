from myCustomPackages import pp1_Resizing


def resizePreProcessing(input_dir, output_dir):
    """
    This function is used to resize images in a directory using different interpolation techniques.
    :param input_dir: The directory containing the images to be resized.
    :param output_dir: The directory where the resized images will be saved.
    """
    # Create a resizer that uses Bicubic interpolation
    resizeTechnique = ['Bilinear', 'BiCubic', 'Lanczos']
    target_size = (224, 224)
    for technique in resizeTechnique:
        # Create an instance of ImageResizing and use it to resize all images in the input directory
        image_resizing = pp1_Resizing.ImageResizing(input_dir, f"{output_dir}/{technique}", target_size)
        image_resizing.resize_images(technique)



"""_summary_
    Entry Point of the code.
"""
if __name__ == "__main__":
    input_dirs = ['Implementation/data/train/unProcessed', 'Implementation/data/test/unProcessed']
    output_dirs = ['Implementation/data/train/preProcessed/resizedData', 'Implementation/data/test/preProcessed/resizedData']

    # Pre-Processing Step 1: Resize the images
    for i in range(len(input_dirs)):
        resizePreProcessing(input_dirs[i], output_dirs[i])