from PIL import Image, ImageFilter

img = Image.open("./astro.jpg")
print(img.size)

# resize
new_img = img.resize((400, 400))
new_img.save("resize.jpg")

# thumbnail
img.thumbnail((400, 400))
img.save("thumbnail.jpg")
