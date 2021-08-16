import os
from PIL import Image

dir_from = "./data_cropped_classified"
dir_to = "./data_cropped_alexnet"

cnt = 0
for foldername in os.listdir(dir_from):
    for filename in os.listdir(dir_from+'/'+foldername):
        img = Image.open(dir_from+'/'+foldername+'/'+filename)

        img_resize = img.resize((224, 224), Image.LANCZOS)
        img_resize.save(dir_to+'/'+foldername+'/'+filename)
        cnt += 1
        if cnt % 1000 == 0:
            print("현재 완료된 파일 : %5d | 진행률 : %3.2f" % (cnt, cnt / 46931 * 100))
print("현재 완료된 파일 : %5d | 진행률 : %3.2f" % (cnt, cnt / 46931 * 100))
print("진행 완료!!")