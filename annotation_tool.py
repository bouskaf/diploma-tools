import cv2
import os
import glob

box_size = 5
os.chdir("data/prague/")


def draw_bbox(event, x, y, flags, param):
    global ix, iy

    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.rectangle(res_img, (x - box_size, y - box_size), (x + box_size, y + box_size), (255, 0, 0), 1)
        ix, iy = x, y

def load_show_csv(img_name):
    if os.path.isfile(img_name[0:img_name.rfind(".")] + '.csv'):
        with open(img_name[0:img_name.rfind(".")] + '.csv', 'r') as my_file:
            for line in my_file:
                x = int(line.split(',')[0])
                y = int(line.split(',')[1])
                type = int(line.split(',')[2])
                size = int(line.split(',')[3])

                if type == 1:
                    cv2.rectangle(res_img, (x - size, y - size), (x + size, y + size), (0, 255, 0), 1)
                elif type == 2:
                    cv2.rectangle(res_img, (x - size, y - size), (x + size, y + size), (255, 0, 0), 1)
                elif type == 3:
                    cv2.rectangle(res_img, (x - size, y - size), (x + size, y + size), (0, 0, 255), 1)
                elif type == 4:
                    cv2.rectangle(res_img, (x - size, y - size), (x + size, y + size), (85, 26, 139), 1)


def write_clicks(x, y, type, size):
    with open(img_name[0:img_name.rfind(".")] + '.csv', 'a') as my_file:
        for i in range(len(x)):
            my_file.write(str(int(x[i])) + ',' + str(int(y[i])) + ',' + str(type[i]) + ',' + str(int(size[i])) + '\n')


ix, iy = -1, -1

images_names = []
for file in glob.glob("*.jpg"):
        images_names.append(file)


if not os.path.isfile('index.csv'):
    with open('index.csv', 'w') as my_file:
        my_file.write("0")

with open('index.csv', 'r') as my_file:
    image_index = int(my_file.readline())


img_name = images_names[image_index]

img = cv2.imread(img_name)
height, width = img.shape[:2]
res_img = cv2.resize(img, (width, height))

cv2.namedWindow('imageWindow')
cv2.setMouseCallback('imageWindow', draw_bbox)


list_x = []
list_y = []
list_type = []
list_size = []



show_bbox = 1
while 1:

    cv2.imshow('imageWindow', res_img)
    k = cv2.waitKey(20) & 0xFF

    if show_bbox:
        load_show_csv(img_name)
    else:
        img = cv2.imread(img_name)
        res_img = cv2.resize(img, (int(width), int(height)))

    # escape for exit
    if k == 27:
        write_clicks(list_x, list_y, list_type, list_size)

        with open('index.csv', 'w') as my_file:
            my_file.write(str(image_index))

        break


    elif k == ord("p"):
        with open(img_name[0:img_name.rfind(".")] + '.csv', 'w') as my_file:
            my_file.write("")
        print("bboxes reseted")

    # 1 for append annotation class = person clear
    elif k == ord("1"):
        list_x.append(ix)
        list_y.append(iy)
        list_type.append(1)
        list_size.append(box_size)
        print(ix, iy, 1, box_size)

    # 2 for append annotation class = person clear shadow
    elif k == ord("2"):
        list_x.append(ix)
        list_y.append(iy)
        list_type.append(2)
        list_size.append(box_size)
        print(ix, iy, 2, box_size)


    # 3 for append annotation class = person? not clear
    elif k == ord("3"):
        list_x.append(ix)
        list_y.append(iy)
        list_type.append(3)
        list_size.append(box_size)
        print(ix, iy, 3, box_size)

    # 4 for append annotation class = person? not clear
    elif k == ord("4"):
        list_x.append(ix)
        list_y.append(iy)
        list_type.append(4)
        list_size.append(box_size)
        print(ix, iy, 4, box_size)

    # r for toggle bboxes
    elif k == ord('r'):
        write_clicks(list_x, list_y, list_type, list_size)
        if show_bbox == 1:
            show_bbox = 0
        else:
            cv2.rectangle(res_img, (ix - box_size, iy - box_size), (ix + box_size, iy + box_size), (255, 0, 0), 1)
            show_bbox = 1

    elif k == ord('a'):
        write_clicks(list_x, list_y, list_type,list_size)
        list_x = []
        list_y = []
        list_type = []
        list_size = []
        image_index -= 1
        img_name = images_names[image_index]
        img = cv2.imread(img_name)
        height, width = img.shape[:2]
        res_img = cv2.resize(img, (width, height))
        load_show_csv(img_name)

    elif k == ord('d'):
        write_clicks(list_x, list_y, list_type, list_size)
        list_x = []
        list_y = []
        list_type = []
        list_size = []
        image_index += 1
        img_name = images_names[image_index]
        img = cv2.imread(img_name)
        height, width = img.shape[:2]
        res_img = cv2.resize(img, (width , height))
        load_show_csv(img_name)

    elif k == ord('w'):
        write_clicks(list_x, list_y, list_type, list_size)
        box_size += 1
        img = cv2.imread(img_name)
        res_img = cv2.resize(img, (width, height))
        cv2.rectangle(res_img, (ix - box_size, iy - box_size), (ix + box_size, iy + box_size), (255, 0, 0), 1)


    elif k == ord('s'):
        write_clicks(list_x, list_y, list_type, list_size)
        box_size -= 1
        img = cv2.imread(img_name)
        res_img = cv2.resize(img, (width, height))
        cv2.rectangle(res_img, (ix - box_size, iy - box_size), (ix + box_size, iy + box_size), (255, 0, 0), 1)


cv2.destroyAllWindows()
