import os
import cv2


def predict(path, model, ext):
    file_name = os.path.split(path)[1].split('.')[0]
    x = path.replace('\\', '/')
    x = cv2.imread(x)
    img_y, image_info = model.detect(x)
    dst_dir = r'./tmp/'
    os.makedirs(dst_dir, exist_ok=True)
    cv2.imwrite('./tmp/{}.{}'.format(file_name, ext), img_y)
    return img_y, image_info
