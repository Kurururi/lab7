# ************************

from PIL import Image
from PIL import ImageFilter

# ************************

img = Image.open(r"C:\уник\1.2\Программирование\картинки\picture1.jpg")
img1 = Image.open(r"C:\уник\1.2\Программирование\картинки\1.png")
img2 = Image.open(r"C:\уник\1.2\Программирование\картинки\2.png")
img3 = Image.open(r"C:\уник\1.2\Программирование\картинки\3.png")
img4 = Image.open(r"C:\уник\1.2\Программирование\картинки\4.png")
img5 = Image.open(r"C:\уник\1.2\Программирование\картинки\5.png")

# ************************


def ex1():
    img.show()
    size = img.size
    form = img.format
    mode = img.mode

    print(size, form, mode)

# ************************


def ex2():
    res_img = img.resize((img.width // 3, img.height // 3))
    res_img.save(r'C:\уник\1.2\Программирование\картинки\picture2.jpg')
    res_img.show()

    g_res_img = res_img.transpose(Image.FLIP_TOP_BOTTOM)
    g_res_img.save(r'C:\уник\1.2\Программирование\картинки\picture3.jpg')
    g_res_img.show()

    g_res_img = res_img.transpose(Image.FLIP_LEFT_RIGHT)
    g_res_img.save(r'C:\уник\1.2\Программирование\картинки\picture4.jpg')
    g_res_img.show()

# ************************


def ex3():
    n = 5
    i = 0
    simg = [img1, img2, img3, img4, img5]

    while i < n:
        emboss_image = simg[i].filter(ImageFilter.EMBOSS)

        i += 1

        emboss_image.save(r'C:\уник\1.2\Программирование\картинки\e' + str(i) + '.png')
        emboss_image.show()

# ************************


def ex4():
    logo = r"C:\уник\1.2\Программирование\картинки\logo.png"

    with Image.open(logo).convert("RGBA") as img_logo:
        img_logo.show()

    img1.paste(img_logo, (10, 10), img_logo)
    img1.show()


ex1()
ex2()
ex3()
ex4()
