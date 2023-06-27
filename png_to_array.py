import matplotlib.pyplot as plt
im = plt.imread('/mnt/ssd/Repos/PicoProject/imgs/apple.png')

print(im)

print(im.shape)

plt.imshow(im)
plt.show()

with open("/mnt/ssd/Repos/PicoProject/imgs/data.txt", "w") as f:
    f.write("[")
    for row in im:
        for col in row:
            rgb = "["
            for value in col:
                rgb += f"{value},"
            rgb += "],\n"
            f.write(rgb)
    f.write("]")