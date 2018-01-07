import PIL
from PIL import Image
dim = 5

basewidth = 8250

for k in range(1, 21):
    file_name = 'prague/' + str(k).zfill(3) + '.jpg'
    dot = file_name.rfind(".")
    slash = file_name.rfind("/")

    im = Image.open(file_name)
    wpercent = (basewidth / float(im.size[0]))
    hsize = int((float(im.size[1]) * float(wpercent)))
    im = im.resize((basewidth, hsize), PIL.Image.ANTIALIAS)

    width, height = im.size


    step_w = int(width / dim)
    step_h = int(height / dim)



    for i in range(dim):
        for j in range(dim):
            crop_rectangle = (j * step_w, i * step_h, (j+1) * step_w, (i+1) * step_h)
            cropped_im = im.crop(crop_rectangle)

            name = file_name[slash:dot] + '_' + str(i) + '_' + str(j) + '.jpg'


            cropped_im.save('prague/small/' + name, 'JPEG')

    print(str(k).zfill(3) + '.jpg done')