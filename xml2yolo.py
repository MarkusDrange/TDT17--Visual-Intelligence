import xml.etree.ElementTree as ET
import glob
import os
import json


def xml_to_yolo_bbox(bbox, w, h):
    # xmin, ymin, xmax, ymax
    x_center = ((bbox[2] + bbox[0]) / 2) / w
    y_center = ((bbox[3] + bbox[1]) / 2) / h
    width = (bbox[2] - bbox[0]) / w
    height = (bbox[3] - bbox[1]) / h
    return [x_center, y_center, width, height]


def yolo_to_xml_bbox(bbox, w, h):
    # x_center, y_center width heigth
    w_half_len = (bbox[2] * w) / 2
    h_half_len = (bbox[3] * h) / 2
    xmin = int((bbox[0] * w) - w_half_len)
    ymin = int((bbox[1] * h) - h_half_len)
    xmax = int((bbox[0] * w) + w_half_len)
    ymax = int((bbox[1] * h) + h_half_len)
    return [xmin, ymin, xmax, ymax]


classes = ["D00", "D10", "D20", "D40"]
input_dir = "Data/Norway/train/annotations/xmls"
output_dir = "Data/Norway/train/images/"
image_dir = "Data/Norway/train/images/"

# create the labels folder (output directory)
if not os.path.isdir(output_dir):
    os.mkdir(output_dir)

# identify all the xml files in the annotations folder (input directory)
files = glob.glob(os.path.join(input_dir, '*.xml'))
print(len(files))
counter = 0
discarded = 0
cropped = 0

# loop through each 
for fil in files:
    basename = os.path.basename(fil)

    # store filepath for train file

    filename = os.path.splitext(basename)[0]
    # if (basename[0]=='N'):
    #     var = True

    # else:
    #     var = False
    # check if the label contains the corresponding image file
    if not os.path.exists(os.path.join(image_dir, f"{filename}.jpg")):
        print(f"{filename} image does not exist!")
        continue

    result = []

    # parse the content of the xml file
    tree = ET.parse(fil)
    root = tree.getroot()
    width = int(root.find("size").find("width").text)
    height = int(root.find("size").find("height").text)


    xmax = 1920

    ymax = 1920


    for obj in root.findall('object'):
        label = obj.find("name").text
        # check for new classes and append to list
        if label not in classes:
            continue
        index = classes.index(label)
        pil_bbox = [int(float(x.text)) for x in obj.find("bndbox")]

        # if pil_bbox[0]>xmax:
        #     discarded += 1
        #     continue
        # if pil_bbox[1]>ymax:
        #     discarded += 1
        #     continue
        # if pil_bbox[2]>xmax:
        #     cropped += 1
        #     pil_bbox[2] = xmax
        # if pil_bbox[3]>ymax:
        #     cropped += 1
        #     pil_bbox[3] = ymax

        yolo_bbox = xml_to_yolo_bbox(pil_bbox, width, height)

      
        # convert data to string
        bbox_string = " ".join([str(x) for x in yolo_bbox])
        result.append(f"{index} {bbox_string}")

    if result:
        # generate a YOLO format text file for each xml file
        with open(os.path.join(output_dir, f"{filename}.txt"), "w", encoding="utf-8") as f:
            f.write("\n".join(result))

print(counter)
print('Cropped:', cropped)
print('Discarded:', discarded)

# generate the classes file as reference
with open('classes.txt', 'w', encoding='utf8') as f:
    f.write(json.dumps(classes))




