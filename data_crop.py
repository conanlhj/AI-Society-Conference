
from PIL import Image
from autocrop import Cropper
import pandas as pd
import numpy as np

df = pd.read_csv('data_label.csv')
df = df.drop([df.columns[0]], axis = 1)
df

failed_list = []
success, fail = 0, 0
for filename in df['ID']:
    cropper = Cropper()
    # Get a Numpy array of the cropped image
    cropped_array = cropper.crop('./dataset/'+filename)

    # Save the cropped image with PIL if a face was detected:
    try:
        cropped_image = Image.fromarray(cropped_array)
        cropped_image.save('./dataset_cropped/'+filename)
        success += 1
    except:
        failed_list.append(filename)
        fail += 1
    if (success+fail)%100 == 0:
        print("성공 : %5d | 실패 : %5d | 총 시도 개수 : %d" % (success, fail, success+fail))

df = df[df.ID not in failed_list]
df.to_csv("data_label_crop.csv")