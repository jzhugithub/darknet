from voc_eval import voc_eval


# ./darknet detector train cfg/voc.data cfg/yolov3-voc.cfg backup/yolov3-voc_700.weights -gpu 0
# ./darknet detector valid cfg/voc.data cfg/yolov3-voc.cfg backup/yolov3-voc_900.weights -out voc900 -thresh 0.5 -gpu 0

# rec,prec,ap = voc_eval('/home/zj/my_workspace/darknet/results/{}.txt','/home/zj/database_temp/voc_2012/VOCdevkit/VOC2012/Annotations/{}.xml','/home/zj/database_temp/voc_2012/2012_val.txt', 'person', 'voc900person', '.')
#
# print('rec',rec)
# print('prec',prec)
# print('ap',ap)


# ./darknet detector train cfg/fisheye2.data cfg/yolov3-fisheye2.cfg yolov3.weights -gpu 0
# ./darknet detector valid cfg/fisheye2.data cfg/yolov3-fisheye2.cfg backup/yolov3-fisheye2_502000.weights -out fisheye -thresh 0.5 -gpu 0
# ./darknet detector test cfg/fisheye2.data cfg/yolov3-fisheye2.cfg backup/yolov3-fisheye2_502000.weights /home/zj/database_temp/fisheye2_data_set/val/images/out_fisheye01191_298_s.jpg
# ./darknet detector demo cfg/fisheye2.data cfg/yolov3-fisheye2.cfg backup/yolov3-fisheye2_502000.weights /home/zj/database/fisheye2_data/video/out_fisheye01191square.avi

rec,prec,ap = voc_eval('/home/zj/my_workspace/darknet/results/{}.txt','/home/zj/database_temp/voc_2012/VOCdevkit/VOC2007/Annotations/{}.xml','/home/zj/database_temp/voc_2012/VOCdevkit/VOC2007/image_list_val.txt', 'ir', 'fisheyeir', '.')

print('rec',rec)
print('prec',prec)
print('ap',ap)
