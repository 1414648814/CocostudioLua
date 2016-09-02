# -*- coding:utf8 -*-
__author__ = 'George1994'

import os
import json
import sys

# 文件读取目录
READ_FILE_PATH = ""
# 文件生成目录
GENERATE_FILE_PATH = ""
# json文件对象
WIDGET_TREE_ROOT = None
# 全局高
DESIGN_HEIGHT = 0
# 全局宽
DESIGN_WIDTH = 0
# 图片路径
IMG_LIST = {}

# 输出结果
RESULT_OUPUT = ""


class Node :
    # 通用
    def setAnchorPoint(self, posX, posY):

    def setPosition(self, posX, posY):

    def setScale(self, scaleX, scaleY):

    def setContentSize(self, w, h):

    def setVisible(self, visible):

    def setRatation(self, rotation):

    def setClassName(self, clsName):

    def getClassName(self):

    def getName(self):

    def setName(self, name):

    # 限于Label使用
    def setFontSize(self, size):

    def setHAlignment(self, alignment):

    # 限于Label和按钮使用
    def setText(self, text):

    def setRGB(self, r, g, b):


    # 限于按钮使用
    def setTouchEnable(self):

    def setButtonImage(self, norImg, selImg, disImg):

    # 限于图片和精灵使用
    def setImage(self, img):


# 获取json文件对象
def getWidgetTreeRoot(read_path) :
    global WIDGET_TREE_ROOT
    if (os.path.exists(read_path)) :
        if (os.path.isfile(read_path)) :
            fp = open(read_path, 'r')
            WIDGET_TREE_ROOT = json.loads(fp)
            return WIDGET_TREE_ROOT
    else :
        print "文件路径不存在/The file is not exist"
        return None


# 处理json对象数据
def handleTree() :
    if WIDGET_TREE_ROOT == None :
        print "json对象为空"
        return
    global DESIGN_WIDTH, DESIGN_HEIGHT, IMG_LIST
    DESIGN_WIDTH = WIDGET_TREE_ROOT["designWidth"]
    DESIGN_HEIGHT = WIDGET_TREE_ROOT["designHeight"]
    IMG_LIST = WIDGET_TREE_ROOT["texturesPng"]


def setNode(node) :
    global RESULT_OUPUT
    RESULT_OUPUT += "local" + node["options"]["name"] + " = cc." + node["classname"] + ".create()"


def recursiveTree(root) :
    if (root == None) :
        return


        child =  recursiveTree(root["children"])




