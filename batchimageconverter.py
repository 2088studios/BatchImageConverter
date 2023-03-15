import os
import glob
from PIL import Image
from pathlib import Path

fileCount = 0

# Gets users' downloads folder path
path = Path.home() / "Downloads" #DEFAULT PATH

# Gathers all files
image_list = path.glob("*.webp") #DEFAULT CONVERSION

for file in image_list:

    fileName, ext = os.path.splitext(file)
    outFile = fileName + ".png" #DEFAULT CONVERSION
    image = Image.open(file)
    image.save(outFile)
    os.remove(file)  # Deletes old file
    fileCount += 1

# Print messages
if fileCount > 0:
    print("Script Complete!")
    print("# of files changed:", fileCount)
else:
    print("No files to convert")
