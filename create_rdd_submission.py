import os
from PIL import Image
import csv
path = "runs/detect/exp2/"

all_files = [img_path for img_path in os.listdir(path) if os.path.isfile(os.path.join(path, img_path))]
print(all_files[-1])


def yolo_to_rdd(c, bbox, w, h):
    # x_center, y_center width heigth
    w_half_len = (bbox[2] * w) / 2
    h_half_len = (bbox[3] * h) / 2
    xmin = int((bbox[0] * w) - w_half_len)
    ymin = int((bbox[1] * h) - h_half_len)
    xmax = int((bbox[0] * w) + w_half_len)
    ymax = int((bbox[1] * h) + h_half_len)
    return f'{c+1} {xmin} {ymin} {xmax} {ymax}'

superstring = []
rdd_string = ''
for pred in all_files:
    predpath = f'{path}labels/{pred[:-3]}txt'
    rdd_string = ''

    image = Image.open(f'{path}{pred}')
    w,h = image.size
    if os.path.exists(predpath):
        #print('true')
        with open(predpath, 'r') as f:

            all_preds = [line for line in f.readlines()]
            rdd_pred = []

            for yolopred in all_preds:
                aslist = yolopred.split()
                c = int(aslist.pop(0))
                bbox = [float(x) for x in aslist]
                rdd_pred.append(yolo_to_rdd(c, bbox, w, h))
            
            for i, line in enumerate(rdd_pred):
                if i == 0:
                    rdd_string = line
                    continue 
                rdd_string = rdd_string + ' ' + line
        #rdd_string = ',' + rdd_string
            

 
    currentstring = pred + ",".join(rdd_string)
    superstring.append([pred, rdd_string])
    #
with open('rdd_preds22.csv', 'w') as f:
    writer = csv.writer(f)
    for line in superstring:
        #f.write(line+'\n')
        writer.writerow(line)


        



        