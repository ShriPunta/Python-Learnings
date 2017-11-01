from PIL import Image

img = Image.open((r'C:\Users\shrip\Pictures\url_downloads\85.jpeg'))
print(img.size)

#PNG,JPEG,etc
print(img.format)

#if its RGB, RGBA
print(img.mode)

r ,g ,b, a = img.split()

img2 = Image.merge("RGB", (g ,b ,a))
#img.show()
img2.show()