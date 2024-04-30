# This script will converts jpg or any other picture file to png
import os
from PIL import Image, ImageFilter

# Here we will Set the path from the input and output folder.
input_folder = "./jpg"

# Here is the file path to the output folder
output_folder = "./png"

# If the output folder does not exist this will create it.
os.makedirs(output_folder, exist_ok=True)


# Here I will grab all of the files inside of the input folder.
for filename in os.listdir(input_folder):
    infile = os.path.join(input_folder, filename)

    # Here is where we will convert each file in the Jpeg folder to pngs
    base_name = os.path.splitext(os.path.basename(infile))[0]

    # Here we will save the converted image to the output folder
    # Construct the output filename in the output folder
    outfile = os.path.join(output_folder, base_name + ".png")  
    

    print("Input file:", infile)
    print("Output file:", outfile)  


    # If the file has already been converted and inside of the output folder, do not try to convert it again
    if infile != outfile:
        try:
            with Image.open(infile) as im:
                im.save(outfile)
        except OSError as e:
          raise RuntimeError(f"Cannot convert {infile}: {e}")