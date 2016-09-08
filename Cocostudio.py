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

class Node:
    _cls_name = ""
    _name = ""
    _ZOrder = 0
    _colorR = 255
    _colorG = 255
    _colorB = 255
    _height = 0
    _anchorX = 0
    _anchorY = 0
    _width = 0
    _height = 0
    _rotation = 0
    _tag = 0
    _scaleX = 1
    _scaleY = 1
    _visible = "true"
    _touchEnable = "true"
    _x = 0
    _y = 0


    """docstring for Node"""
    def __init__(self, name):
        self._name = name
        self._cls_name = "Node"
        pass

    def getClassName(self):
        return self._cls_name

    def getName(self):
        return self._name

    def setAnchorPoint(self, anchorX, anchorY):
        self._anchorX = anchorX
        self._anchorY = anchorY
        pass
    
    def setColor(self, r, g, b):
        self._colorR = r
        self._colorG = g
        self._colorB = b
        pass

    def setContentSize(self, width, height):
        self._width = width
        self._height = height
        pass

    def setScale(self, scaleX, scaleY):
        self._scaleX = scaleX
        self._scaleY = scaleY
        pass

    def setRatation(self, rotation):
        self._rotation = rotation
        pass

    def setZOrder(self, zorder):
        self._ZOrder = zorder
        pass

    def setPosition(self, x, y):
        self._x = x
        self._y = y
        pass

    def setTag(self, tag):
        self._tag = tag
        pass

    def setVisible(self, visible):
        self._visible = visible
        pass

    def setTouchEnable(self, enable):
        self._touchEnable = enable
        pass

class Button(Node):
    _n_img = ""
    _s_img = ""
    _d_img = ""
    _text = ""
    _t_R = 255
    _t_G = 255
    _t_B = 255
    _t_size = 18

    """docstring for Button"""
    def __init__(self, name):
        Node.__init__(self, name)
        self._cls_name = "Button"
        pass

    def setImage(self, normalImg, selectImg, disableImg):
        self._n_img = normalImg
        self._s_img = selectImg
        self._d_img = disableImg
        pass
        
    def setText(self, text):
        self._text = text
        pass

    def setTextColor(self, r, g, b):
        self._t_R = r
        self._t_G = g
        self._t_B = b
        pass

    def setTextSize(self, size):
        self._t_size = size
        pass
    
class Label(Node):
    _text = ""
    _t_R = 255
    _t_G = 255
    _t_B = 255
    _t_size = 18

    """docstring for Label"""
    def __init__(self, name):
        Node.__init__(self, name)
        self._cls_name = "Label"
        pass

    def setText(self, text):
        self._text = text
        pass

    def setTextColor(self, r, g, b):
        self._t_R = r
        self._t_G = g
        self._t_B = b
        pass

    def setTextSize(self, size):
        self._t_size = size
        pass

class CheckBox(Node):
    _select = False
    """docstring for CheckBox"""
    def __init__(self, name):
        Node.__init__(self, name)
        self._cls_name = "CheckBox"
        pass

    def setImage(self, normalImg, selectImg, disableImg):
        pass

    def serMarkImage(self, normalImg, disableImg):
        pass

    def setSelect(self, select):
        pass
        
class LoadingBar(Node):
    _percent = 0

    """docstring for LoadingBar"""
    def __init__(self, name):
        Node.__init__(self, name)
        self._cls_name = "LoadingBar"
        pass

    def setImage(self, img):
        pass

    def setPercent(self, percent):
        pass

class Slider(Node):
    _percent = 0
    _select = "false"

    """docstring for Slider"""
    def __init__(self, name):
        Node.__init__(self, name)
        self._cls_name = "Slider"
        pass
        
    def setImage(self, img):
        pass

    def setInnerImage(self, img):
        pass

    def setSelect(self, select):
        pass

    def setButtonImage(self, normalImg, selectImg, disableImg):
        pass

    def setPercent(self, img):
        pass

class TextField(Node):
    """docstring for TextField"""
    def __init__(self, name):
        Node.__init__(self, name)
        self._cls_name = "TextField"
        pass

    def setOccupyText(self, text):
        pass

    def setText(self, text):
        pass

    def setFontSize(self, size):
        pass

    def setSecret(self, secret):
        pass

    def setMaxLen(self, len):
        pass

class Panel(Node):
    _img = ""

    """docstring for Panel"""
    def __init__(self, name):
        Node.__init__(self, name)
        self._cls_name = "Panel"
        pass

    def setImage(self, img):
        self._img = img
        pass
        
class ImageView(Node):
    """docstring for ImageView"""
    def __init__(self, name):
        Node.__init__(self, name)
        self._cls_name = "ImageView"
        pass
    
    def setImage(self, img):
        pass

class ListView(Node):
    _dir = 0
    _inner_w = 0
    _inner_h = 0
    _margin = 0

    """docstring for ListView"""
    def __init__(self, name):
        Node.__init__(self, name)
        self._cls_name = "ListView"
        pass

    def setImage(self, img):
        pass
    
    def setDirection(self, dir):
        pass
    
    def setInnerSize(self, w, h):
        pass
    
    def setMargin(self, m):
        pass

class PageView(Node):
    """docstring for PageView """
    def __init__(self, name):
        Node.__init__(self, name)
        self._cls_name = "PageView"
        pass

    def setImage(self, img):
        pass
        
class ScrollView(Node):
    """docstring for ScrollView"""
    def __init__(self, name):
        Node.__init__(self, name)
        self._cls_name = "ScrollView"
        pass
    
    def setImage(self, img):
        pass

    def setClipSize(self, w, h):
        pass
        
class Solution :
    _node = None

    # 通用
    def __setAnchorPoint(self):
        global RESULT_OUPUT
        RESULT_OUPUT += self._node.getName() + ":setAnchorPoint(" + str(self._node._anchorX) + "," + str(self._node._anchorY) + ")\n"
        pass

    def __setPosition(self):
        global RESULT_OUPUT
        RESULT_OUPUT += self._node.getName() + ":setPosition(" + str(self._node._x) + "," + str(self._node._y) + ")\n"
        pass

    def __setScale(self):
        global RESULT_OUPUT
        RESULT_OUPUT += self._node.getName() + ":setScale(" + str(self._node._scaleX) + "," + str(self._node._scaleY) + ")\n"
        pass

    def __setContentSize(self):
        global RESULT_OUPUT
        RESULT_OUPUT += self._node.getName() + ":setContentSize(" + str(self._node._width) + "," + str(self._node._height) + ")\n"
        pass

    def __setVisible(self):
        global RESULT_OUPUT
        RESULT_OUPUT += self._node.getName() + ":setVisible(" + str(self._node._visible) +")\n"
        pass

    def __setRatation(self):
        global RESULT_OUPUT
        RESULT_OUPUT += self._node.getName() + ":setRatation(" + str(self._node._rotation) + ")\n"
        pass

    def __setZOrder(self):
        global RESULT_OUPUT
        RESULT_OUPUT += self._node.getName() + ":setZOrder(" + str(self._node._ZOrder) + ")\n"
        pass

    def __setTag(self):
        global RESULT_OUPUT
        RESULT_OUPUT += self._node.getName() + ":setTag(" + str(self._node._tag) + ")\n"
        pass

    # 限于Label使用
    def __setFontSize(self):
        global RESULT_OUPUT
        RESULT_OUPUT += self._node.getName() + ":setFontSize(" + str(self._node._t_size) + ")\n"
        pass

    # 限于Label和按钮使用
    def __setText(self):
        global RESULT_OUPUT
        RESULT_OUPUT += self._node.getName() + ":setText(" + self._node._text + ")\n"
        pass

    # 只有跟节点变色，需要遍历子结点
    def __setRGB(self):
        global RESULT_OUPUT
        RESULT_OUPUT += self._node.getName() + ":setColor(ccc3(" + str(self._node._colorR) + "," + str(self._node._colorG) + "," + str(self._node._colorB) + "))\n"
        pass

    # 限于按钮使用
    def __setTouchEnable(self):
        global RESULT_OUPUT
        RESULT_OUPUT += self._node.getName() + ":setTouchEnable(" + str(self._node._touchEnable) + ")\n"
        pass

    def __setButtonImage(self):
        global RESULT_OUPUT
        RESULT_OUPUT += self._node.getName() + ":setColor(" + self._node._n_img + "," + self._node._s_img + "," + self._node._d_img + ")\n"
        pass

    # 限于图片和精灵使用
    def __setImage(self):
        global RESULT_OUPUT
        RESULT_OUPUT += self._node.getName() + ":setImage(" + self._node._img + ")\n"
        pass

    def initData(self, node, option):
        if "classname" in node:
            if node["classname"] == "Label":
                print "正在解析Label/parsing Label"
                self._node = Label(option["name"])
                self._node.setText(option["text"])
                self._node.setTextColor(option["colorR"], option["colorG"], option["colorB"])
                self._node.setTextSize(option["fontSize"])
                pass
            elif node["classname"] == "Button":
                print "正在解析Button/parsing Button"
                self._node = Button(option["name"])
                self._node.setText(option["text"])
                self._node.setTextColor(option["colorR"], option["colorG"], option["colorB"])
                self._node.setTextSize(option["fontSize"])
                self._node.setImage(option["normalData"]["path"], option["pressedData"]["path"], option["disabledData"]["path"])
                pass
            elif node["classname"] == "Panel":
                print "正在解析Panel/parsing Panel"
                self._node = Panel(option["name"])
                self._node.setImage(option["backGroundImageData"]["path"])
                pass
            elif node["classname"] == "ImageView":
                print "正在解析ImageView/parsing ImageView"
                self._node = ImageView(option["name"])
                self._node.setImage(option["fileNameData"]["path"])
                pass
            elif node["classname"] == "ListView":
                print "正在解析ListView/parsing ListView"
                self._node = ListView(option["name"])
                self._node.setImage(option["backGroundImage"])
                self._node.setInnerSize(option["innerWidth"], option["innerHeight"])
                self._node.setMargin(option["itemMargin"])
                self._node.setDirection(option["direction"])
                pass
            elif node["classname"] == "ScrollView":
                print "正在解析ScrollView/parsing ScrollView"
                self._node = ScrollView(option["name"])
                pass
            elif node["classname"] == "PageView":
                print "正在解析PageView/parsing PageView"
                self._node = PageView(option["name"])
                pass
            elif node["classname"] == "Slider":
                print "正在解析Slider/parsing Slider"
                self._node = Slider(option["name"])
                pass
            elif node["classname"] == "LoadingBar":
                print "正在解析LoadingBar/parsing LoadingBar"
                self._node = LoadingBar(option["name"])
                pass
            elif node["classname"] == "CheckBox":
                print "正在解析CheckBox/parsing CheckBox"
                self._node = CheckBox(option["name"])
                pass
            elif node["classname"] == "TextField":
                print "正在解析TextField/parsing TextField"
                self._node = TextField(option["name"])
                pass
            else:
                print "无法解析该格式/can not parse the object"
                return

            self._node.setAnchorPoint(option["anchorPointX"], option["anchorPointY"])
            self._node.setPosition(option["x"], option["y"])
            self._node.setScale(option["scaleX"], option["scaleY"])
            self._node.setTag(option["tag"])
            self._node.setVisible(option["visible"])
            self._node.setZOrder(option["ZOrder"])
            self._node.setContentSize(option["width"], option["height"])
            self._node.setTouchEnable(option["touchAble"])
            self._node.setColor(option["colorR"], option["colorG"], option["colorB"])
            self._node.setRatation(option["rotation"])
            self._node.setTouchEnable(option["touchAble"])

        pass

    def  handleData(self):
        self.__setAnchorPoint()
        self.__setPosition()
        self.__setScale()
        self.__setTag()
        self.__setVisible()
        self.__setZOrder()
        self.__setContentSize()
        self.__setRatation()
        self.__setTouchEnable()
        self.__setRGB()
        pass
        

# 获取json文件对象
def getWidgetTreeRoot(read_path) :
    if (os.path.exists(read_path)) :
        if (os.path.isfile(read_path)) :
            fp = open(read_path, 'r')
            rp = fp.read()
            return json.loads(rp)
    else :
        print "文件路径不存在/The file is not exist"
        return None


# 处理json对象数据
def handleTree() :
    global DESIGN_WIDTH, DESIGN_HEIGHT, IMG_LIST
    DESIGN_WIDTH = WIDGET_TREE_ROOT["designWidth"]
    DESIGN_HEIGHT = WIDGET_TREE_ROOT["designHeight"]
    IMG_LIST = WIDGET_TREE_ROOT["texturesPng"]

    global RESULT_OUPUT

    RESULT_OUPUT += "local "
    recursiveTree(WIDGET_TREE_ROOT["widgetTree"], WIDGET_TREE_ROOT["widgetTree"]["children"])

def setNode(parent, node) :
    if node == None or node == []:
        return
    solution = Solution()
    option = node["options"]

    create(node)
    solution.initData(node, option)
    solution.handleData()
    addChild(parent, node)

def create(node):
    global RESULT_OUPUT
    RESULT_OUPUT += "local " + node["options"]["name"] + " = cc." + node["options"]["classname"] + ":create()\n"
    pass

def addChild(parent, node):
    global RESULT_OUPUT
    RESULT_OUPUT += parent["options"]["name"] + ":addChild(" + node["options"]["name"] + ")\n"
    pass

def recursiveTree(parent, root) :
    if root == []:
        return
    global RESULT_OUPUT
    for node in root:
        setNode(parent, node)
        RESULT_OUPUT += "\n"
        if "children" in node:
            recursiveTree(node, node["children"])
        else:
            print "没有children/no esixt children"

if __name__ == '__main__':
    # path = "ui/game-loading.json"
    


    WIDGET_TREE_ROOT = getWidgetTreeRoot(path)
    if WIDGET_TREE_ROOT == None :
        print "json对象为空/json object is null"
        return 
    handleTree()

    print RESULT_OUPUT