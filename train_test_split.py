
from sklearn.model_selection import train_test_split
import os
import shutil
# splitfolders.ratio("input", output="dataset",
#     seed=1337, ratio=(.8, .1, .1), group_prefix=2, move=True)


path = "Norway/train/images/"

all_files = os.listdir(path)

all_jpegs = [x for x in all_files if x.endswith('.jpg') and x[0]=='N']

print(all_jpegs[0])


imgs_with = []
imgs_without = []

for image_p in all_jpegs:
    if os.path.exists(f'{path}/{image_p[:-3]}txt'):
        imgs_with.append(image_p)
    else:
        imgs_without.append(image_p)


X_train, X_test_val = train_test_split(all_jpegs, test_size=0.2, random_state=42)

X_test, X_val = train_test_split(X_test_val, test_size=0.8, random_state=42)

data_path = '/lhome/markusmd/Desktop/vi/Data/Norway/train/images/'



train_dest ='/lhome/markusmd/Desktop/vi/yolo2/yolov7/final/train/'
test_dest = '/lhome/markusmd/Desktop/vi/yolo2/yolov7/final/test/'
val_dest = '/lhome/markusmd/Desktop/vi/yolo2/yolov7/final/val/'

for image_name in X_train:


    orig = f'{data_path}{image_name}'
    dest = f'{train_dest}{image_name}'

    shutil.move(orig, dest)

    if os.path.exists(f'{path}/{image_name[:-3]}txt'):

        shutil.move(f'{data_path}/{image_name[:-3]}txt', f'{train_dest}/{image_name[:-3]}txt')

for image_name in X_test:


    orig = f'{data_path}{image_name}'
    dest = f'{test_dest}{image_name}'

    shutil.move(orig, dest)

    if os.path.exists(f'{path}/{image_name[:-3]}txt'):

        shutil.move(f'{data_path}/{image_name[:-3]}txt', f'{test_dest}/{image_name[:-3]}txt')

for image_name in X_val:


    orig = f'{data_path}{image_name}'
    dest = f'{val_dest}{image_name}'

    shutil.move(orig, dest)

    if os.path.exists(f'{path}/{image_name[:-3]}txt'):

        shutil.move(f'{data_path}/{image_name[:-3]}txt', f'{val_dest}/{image_name[:-3]}txt')
    
    

    

# with open('train_images.txt', 'w') as f:

    
#     for x in X_train:

        
#         filename = data_path + str(x) + '\n'

#         f.write(filename)


# with open('test_images.txt', 'w') as c:

#     for x in X_test:
#         filename = data_path + str(x) + '\n'

#         c.write(filename)

# with open('val_images.txt', 'w') as c:

#     for x in X_val:
#         filename = data_path + str(x) + '\n'

#         c.write(filename)

