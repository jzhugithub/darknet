import xml.etree.ElementTree as ET
import os

classes = ["ir", "ob"]

def convert(size, box):
    dw = 1./(size[0])
    dh = 1./(size[1])
    x = (box[0] + box[1])/2.0 - 1
    y = (box[2] + box[3])/2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

def convert_annotation(image_id, annotation_dir, label_dir):
    in_file = open(os.path.join(annotation_dir, image_id + '.xml'))
    out_file = open(os.path.join(label_dir, image_id + '.txt'), 'w')
    tree=ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult)==1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w,h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')


if __name__ == '__main__':
    set_dir = "/home/zj/database_temp/fisheye2_data_set/train(origin)"
    out_image_list_file = "image_list_train_origin.txt"

    label_dir = os.path.join(set_dir,'labels')
    image_dir = os.path.join(set_dir, 'images')
    annotation_dir = os.path.join(set_dir, 'annotations')
    if not os.path.exists(label_dir):
        os.mkdir(label_dir)
    out_image_list_file_path = os.path.join(set_dir, out_image_list_file)

    with open(out_image_list_file_path, 'w') as out_list:
        for root, dirs, files in os.walk(image_dir):
            for image_name in sorted(files):
                out_list.write(os.path.join(root, image_name) + '\n')
                convert_annotation(image_name[:-4], annotation_dir, label_dir)

