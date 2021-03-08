import sys
import os

from PIL import Image

# arg 1 is img folder, output is arg 2
path = sys.argv[1]
op = sys.argv[2]

print(path, op)

if not os.path.exists(op):
  os.makedirs(op)

for filename in os.listdir(path):
  img = Image.open(f"{path}{filename}")
  cleanname = os.path.splitext(filename)[0]
  img.save(f"{op}{cleanname}.png", "png")

print("all done")
