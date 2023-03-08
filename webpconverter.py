import os
from PIL import Image

fileCount = 0;

for file in os.listdir("/home/ilindley/Downloads"):
    if (file.endswith(".webp")):
        #base, ext = os.path.splitext(file)
        #os.replace(ext, '.png')
        #file = base + '.png'
        #file.replace('.webp', '.png')
        
        fileCount += 1


if fileCount > 0:
    print("Script Complete!")
    print("# of files changed:", fileCount)
else:
    print("No files to convert")