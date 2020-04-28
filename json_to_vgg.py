import os
import urllib.request
import shutil
import math
import json 



def bbox(ann):
    x=[]
    y=[]
    for f in range(len(ann[0])):
        if f%2==0:
            x.append(ann[0][f])
        else:
            y.append(ann[0][f])

    minx=min(x)
    maxx=max(x)
    miny=min(y)
    maxy=max(y)

    return [minx, miny, maxx, maxy]

def processVertices(Vertices):
    liste=[]
    for v in Vertices:
        x=v[0]
        y=v[1]
        liste.append(x)
        liste.append(y)
    liste=[liste]
    return liste
def processVerticesxy(Vertices):
    all_points_x=[i[0] for i in Vertices]
    all_points_y=[i[1] for i in Vertices]
    return (all_points_x,all_points_y)    
def area(ann):
    x=[]
    y=[]
    for f in range(len(ann[0])):
        if f%2==0:
            x.append(ann[0][f])
        else:
            y.append(ann[0][f])

    area=0
    n=len(x)
    for i in range(len(x)):
        j=(1+i) % n 
        area+= x[i]*y[j]
        area-= x[j]*y[i]
    area=abs(area)/2
    return area


## Path to the folder with json files

Json_path="D:/mask_data/test/json" ## TODO




##coco_format['info']={}
##coco_format['info']['contributor']="Naseef"
##coco_format['info']['date_created']='TODO'
##coco_format['info']['description']='TODO'
##coco_format['info']['url']='TODO'
##coco_format['info']['version']=1
##coco_format['info']['year']=2020


##
##coco_format['filename']=[]
##coco_format['regions']=[]
##coco_format['size']=[]
##Filling categories:

# It's better to put a loop here: This is just for clarification:

#coco_format['categories'].append({})
##coco_format['categories'].append({})
##coco_format['categories'].append({})


#coco_format['categories'][0]['supercategory']='rod'
#coco_format['categories'][0]['id']=1
#coco_format['categories'][0]['name']='rod'

##coco_format['categories'][1]['supercategory']='class2'
##coco_format['categories'][1]['id']=2
##coco_format['categories'][1]['name']='class3'
##
##coco_format['categories'][2]['supercategory']='class3'
##coco_format['categories'][2]['id']=3
##coco_format['categories'][2]['name']='class3'

## Filling images and annotations:

image_id=1
label_id=1

# VGG Image Annotator saves each image in the form:
# { 'filename': '28503151_5b5b7ec140_b.jpg',
#   'regions': {
#       '0': {
#           'region_attributes': {}
#           'shape_attributes': {
#               'all_points_x': [...],
#               'all_points_y': [...],
#               'name': 'polygon'}},
#       ... more regions ...
#   },
#   'size': 100202
# }




vgg_format={}
for f in os.listdir(Json_path):
    
    coco_format={}

    json_file=os.path.join(Json_path,f)
    own=json.load(open(json_file))

    labels=own['shapes']
    #print(labels[0])
    ## Filling images:
    coco_format['filename']=f[:-5]+'.jpg'
    coco_format['size']=-1

##    regions['id']
##    image['file_name']=f[:-5]+'.jpg' 
##    image['height']='TODO'   
##    image['width']='TODO'    
##    image['id']=image_id
##    image['date_captured']='TODO'
##    coco_format['images'].append(image)
    

    ##Filling annotations:
    #"region_attributes":{"name":"Plato","type":"human","image_quality":{"good_illumination":true}}}
    #shape_attributes:{#"name":"polygon",
    #"all_points_x":[116,94,176,343,383,385,369,406,398,364,310,297,304,244,158],
    #"all_points_y":[157,195,264,273,261,234,222,216,155,124,135,170,188,170,175]}


    for l in labels:
        #if l['shape_type']=='polygon':
            #continue
        
##        label['id']=label_id
##        #print(label_id)
##        label['image_id']=image_id
##        label['iscrowd']=0


        regions={}
        id={}
        id['region_attributes']={"name":"rod","type":"rod","image_quality":{"good_illumination":'true'}}
        id['shape_attributes']={}
        id['shape_attributes']['all_points_x']=processVerticesxy(l['points'])[0]
        id['shape_attributes']['all_points_y']=processVerticesxy(l['points'])[1]
        id['shape_attributes']['name']='polygon'
        regions[label_id]=id
        coco_format['regions']=regions


##        if l['label']=='rod':
##            label['category_id']=1
##        if l['label_class']=='class2':
##            label['category_id']=2
##        if l['label_class']=='class3':
##            label['category_id']=3
##        
##        v=processVertices(l['points'])
##        #print(v)
##
##        #label['all_points_x']=v[0]
##        #label['all_points_y']=v[1]
##        label['segmentation']=processVertices(l['points'])
##        label['area']=area(v)
##        label['bbox']=bbox(v)
        

        label_id+=1

        #print("label", label)
        #coco_format['annotations'].append(label)

    vgg_format[f[:-5]+'.jpg-1']=coco_format
    image_id+=1


with open("D:/mask_data/test/json/test1.json",'w') as fp:
    json.dump(vgg_format,fp)
