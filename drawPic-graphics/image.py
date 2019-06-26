import os

def make_pic():
    imageFile = open("image.ppm", "w")
    
    #setup
    imageFile.write("P3\n500 500\n255\n")
    
    #drawImage
    for i in range(500):
        for n in range(500):
            r = 0
            g = 0
            b = i % 255
            imageFile.write("%d %d %d " % (r, g, b))

    imageFile.close()


if __name__ == "__main__":
    make_pic()