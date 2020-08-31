# -*- coding: utf-8 -*-
# @Author: caoyang
# @Date:   2020-01-04 16:41:43
# @E-mail:   cy915822zs@gmail.com
# @Last Modified time: 2020-08-24 15:58:16
# @Description: Python解析XML；修改xml标注文件中的绝对路径，用相对路径表示

from xml.dom.minidom import parse
import re
import os
import cv2


def updateXML():
    """
    批量修改xml文件
    """
    # 标注文件路径
    labelDir = 'data/Annotations/'
    # 训练图像路径
    picDir ='data/images/'
    files = os.listdir(labelDir)
    for file in files:
        domTree = parse(labelDir+file)
        # 文档根元素
        rootNode = domTree.documentElement
        # 查找对应节点
        widthNode = rootNode.getElementsByTagName("width")
        heightNode = rootNode.getElementsByTagName("height")
        fileNameNode = rootNode.getElementsByTagName("filename")
        pathNode = rootNode.getElementsByTagName("path")

        basename = os.path.basename(file).replace('xml','png')

        try:
            image = cv2.imread(picDir+basename)
            w = image.shape[0]
            h = image.shape[1]
            widthNode[0].childNodes[0].data = w # 修改图像宽
            heightNode[0].childNodes[0].data = h #修改图像高
            fileNameNode[0].childNodes[0].data = basename # 修改文件名
            new_path = os.path.join('..','PNGImages',basename)
            pathNode[0].childNodes[0].data = new_path #修改为相对路径
            print(new_path,image.shape[0],image.shape[1]) # 打印修改后的结果，检查
        except Exception as e:
            print("Exception: ", e)
            print("The error picture: ",basename)

        # 执行后，将修改写入xml文件
        with open(labelDir+file, 'w') as f:
            domTree.writexml(f, encoding='utf-8')


if __name__ == '__main__':
    updateXML()