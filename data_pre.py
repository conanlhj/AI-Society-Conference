import os
import pandas as pd
import numpy as np
from shutil import copyfile
imagePath = "./UNBC-McMaster/images"
dataPath = "./Sequence_Labels/Frame_Labels/PSPI"
d = {}
cnt, file_cnt = 0, 48399
for subject_id in os.listdir(imagePath):
    for sequence_id in os.listdir(imagePath+'/'+subject_id):
        for imagename in os.listdir(imagePath+'/'+subject_id+'/'+sequence_id):
            filename = imagename.split('.')[0]
            f = open(dataPath+'/'+subject_id+'/'+sequence_id+'/'+filename+'_facs.txt', 'r', encoding='utf-8')
            str = f.read().strip()
            d[imagename] = eval(str)
            copyfile(imagePath+'/'+subject_id+'/'+sequence_id+'/'+imagename, './dataset/'+imagename)
            f.close()
            cnt += 1
            if cnt % 100 == 0:
                print("현재 완료한 개수: %d, 진행률: %f" % (cnt, cnt/file_cnt*100))
print("현재 완료한 개수: %d, 진행률: %f" % (cnt, cnt/file_cnt*100))
df = pd.DataFrame.from_dict(d, orient='index', columns=['PSPI'])
df.to_csv("./data_label.csv")