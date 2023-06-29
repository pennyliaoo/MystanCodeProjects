"""
File: blur.py
Name:
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    new_img = SimpleImage.blank(img.width,img.height)
    for x in range(img.width):
        for y in range(img.height):
            new_img_p = new_img.get_pixel(x,y)
            redsum = 0
            greensum = 0
            bluesum = 0
            cnt = 0
            for pixel_x in range(x-1,x+2): # pixel_x = x-1,x,x+1
                for pixel_y in range(y-1,y+2): # pixel_y = y-1,y,y+1
                    if 0 <= pixel_x < img.width:
                        if 0 <= pixel_y < img.height:
                            oldimg_pixel = img.get_pixel(pixel_x,pixel_y)
                            redsum += oldimg_pixel.red
                            greensum += oldimg_pixel.green
                            bluesum += oldimg_pixel.blue
                            cnt += 1
            new_img_p.red = redsum / cnt
            new_img_p.green = greensum / cnt
            new_img_p.blue = bluesum /cnt
    return new_img

def main():
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(10):
        blurred_img = blur(blurred_img)
    blurred_img.show()


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
