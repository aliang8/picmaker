import random

header = "P3\n"
resolution = "500 500 255\n"

image = ""
width = [3,4,5]

for i in range(500):
    for j in range(500):
        for num in width:
            if i % num == 0 or j % num == 0:
                image += "%d %d %d\n" % (random.randrange(255)+1, random.randrange(255)+1, random.randrange(255)+1)
            else:
                image += "0 0 0\n"
                

f = open("pic.ppm","w")
f.write(header + resolution + image)
f.close()

