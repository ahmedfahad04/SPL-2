from PIL import Image

# Open an image file

img = "D:\PICTURES\EID.jpg"
with Image.open(img) as im:
    # Resize the image
    im_resized = im.resize((128, 128))
    # Save the resized image
    im_resized.save('image_resized.jpg')