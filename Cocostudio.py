# -*- coding:utf8 -*-
__author__ = 'George1994'

import os
import os.path
import json
import sys
from Tkinter import *
from tkFileDialog import askopenfilename
from tkFileDialog import asksaveasfilename

reload(sys)
sys.setdefaultencoding('utf8')

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
# 空格符
TAB_SPACE = "\t"

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


class LabelBMFont(Label):
    _file = ""
    _text = ""

    def __init__(self, name):
        Label.__init__(self, name)
        self._cls_name = "LabelBMFont"
        pass

    def setText(self, text):
        self._text = text
        pass

    def setFileName(self, file):
        self._file = file
        pass

class LabelTTF(Label):
    _file = ""
    _text = ""

    def __init__(self, name):
        Label.__init__(self, name)
        self._cls_name = "LabelBMFont"
        pass

    def setText(self, text):
        self._text = text
        pass

    def setFileName(self, file):
        self._file = file
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
    _maxLen = 10
    _secret = False
    _t_size = 18
    _text = ""
    _holder = ""
    _maxLenEnable = False
    _pwdEnable = False
    _pwdStyleText = ""

    """docstring for TextField"""
    def __init__(self, name):
        Node.__init__(self, name)
        self._cls_name = "TextField"
        pass

    def setText(self, text):
        self._text = text
        pass

    def setFontSize(self, size):
        self._t_size = size
        pass

    def setSecret(self, secret):
        self._secret = secret
        pass

    def setMaxLen(self, len):
        self._maxLen = len
        pass

    def setPlaceHolder(self, holder):
        self._holder = holder
        pass

    def setMaxLenEnable(self, enable):
        self._maxLenEnable = enable
        pass

    def setPwdEnable(self, enable):
        self._pwdEnable = enable
        pass

    def setPwdStyleText(self, text):
        self._pwdStyleText = text
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
        
class ImageView(Panel):
    """docstring for ImageView"""
    def __init__(self, name):
        Panel.__init__(self, name)
        self._cls_name = "ImageView"
        pass

class ListView(Panel):
    _dir = 0
    _inner_w = 0
    _inner_h = 0
    _margin = 0

    """docstring for ListView"""
    def __init__(self, name):
        Panel.__init__(self, name)
        self._cls_name = "ListView"
        pass
    
    def setDirection(self, dir):
        pass
    
    def setInnerSize(self, w, h):
        pass
    
    def setMargin(self, m):
        pass

class PageView(Panel):
    """docstring for PageView """
    def __init__(self, name):
        Panel.__init__(self, name)
        self._cls_name = "PageView"
        pass
        
class ScrollView(Panel):
    _clip_w = 0
    _clip_h = 0

    """docstring for ScrollView"""
    def __init__(self, name):
        Panel.__init__(self, name)
        self._cls_name = "ScrollView"
        pass

    def setClipSize(self, w, h):
        self._clip_w = w
        self._clip_h = h
        pass
        
class Solution :
    _node = None

    # 通用
    def __setAnchorPoint(self):
        global RESULT_OUPUT,TAB_SPACE
        RESULT_OUPUT += TAB_SPACE + self._node.getName() + ":setAnchorPoint(" + str(self._node._anchorX) + ", " + str(self._node._anchorY) + ")\n"
        pass

    def __setPosition(self):
        global RESULT_OUPUT, TAB_SPACE
        RESULT_OUPUT += TAB_SPACE + self._node.getName() + ":setPosition(" + str(self._node._x) + ", " + str(self._node._y) + ")\n"
        pass

    def __setScale(self):
        global RESULT_OUPUT, TAB_SPACE
        RESULT_OUPUT += TAB_SPACE + self._node.getName() + ":setScale(" + str(self._node._scaleX) + ", " + str(self._node._scaleY) + ")\n"
        pass

    def __setContentSize(self):
        global RESULT_OUPUT, TAB_SPACE
        RESULT_OUPUT += TAB_SPACE + self._node.getName() + ":setContentSize(" + str(self._node._width) + ", " + str(self._node._height) + ")\n"
        pass

    def __setVisible(self):
        global RESULT_OUPUT, TAB_SPACE
        RESULT_OUPUT += TAB_SPACE + self._node.getName() + ":setVisible(" + str(self._node._visible) +")\n"
        pass

    def __setRatation(self):
        global RESULT_OUPUT, TAB_SPACE
        RESULT_OUPUT += TAB_SPACE + self._node.getName() + ":setRatation(" + str(self._node._rotation) + ")\n"
        pass

    def __setZOrder(self):
        global RESULT_OUPUT, TAB_SPACE
        RESULT_OUPUT += TAB_SPACE + self._node.getName() + ":setZOrder(" + str(self._node._ZOrder) + ")\n"
        pass

    def __setTag(self):
        global RESULT_OUPUT, TAB_SPACE
        RESULT_OUPUT += TAB_SPACE + self._node.getName() + ":setTag(" + str(self._node._tag) + ")\n"
        pass

    # 限于Label和TextField使用
    def __setFontSize(self):
        global RESULT_OUPUT, TAB_SPACE
        RESULT_OUPUT += TAB_SPACE + self._node.getName() + ":setFontSize(" + str(self._node._t_size) + ")\n"
        pass

    # 限于Label和按钮使用
    def __setText(self):
        global RESULT_OUPUT, TAB_SPACE
        RESULT_OUPUT += TAB_SPACE + self._node.getName() + ":setText(\"" + self._node._text + "\")\n"
        pass

    # 限于TextField使用
    def __setPlaceHolder(self):
        global RESULT_OUPUT, TAB_SPACE
        RESULT_OUPUT += TAB_SPACE + self._node.getName() + ":setPlaceHolder(\"" + self._node._holder + "\")\n"
        pass

    def __setMaxLenEnable(self):
        global RESULT_OUPUT, TAB_SPACE
        RESULT_OUPUT += TAB_SPACE + self._node.getName() + ":setMaxLengthEnabled(" + str(self._node._maxLenEnable) + ")\n"
        pass

    def __setMaxLen(self):
        global RESULT_OUPUT, TAB_SPACE
        RESULT_OUPUT += TAB_SPACE + self._node.getName() + ":setMaxLength(" + str(self._node._maxLen) + ")\n"
        pass

    def __setPwdEnable(self):
        global RESULT_OUPUT, TAB_SPACE
        RESULT_OUPUT += TAB_SPACE + self._node.getName() + ":setPasswordEnable(" + str(self._node._pwdEnable) + ")\n"
        pass

    def __setPwdStyleText(self):
        global RESULT_OUPUT, TAB_SPACE
        RESULT_OUPUT += TAB_SPACE + self._node.getName() + ":setPasswordStyleText(\"" + self._node._pwdStyleText + "\")\n"
        pass

    # 只有跟节点变色，需要遍历子结点
    def __setRGB(self):
        global RESULT_OUPUT, TAB_SPACE
        RESULT_OUPUT += TAB_SPACE + self._node.getName() + ":setColor(ccc3(" + str(self._node._colorR) + ", " + str(self._node._colorG) + ", " + str(self._node._colorB) + "))\n"
        pass

    # 限于按钮使用
    def __setTouchEnable(self):
        global RESULT_OUPUT, TAB_SPACE
        RESULT_OUPUT += TAB_SPACE + self._node.getName() + ":setTouchEnable(" + str(self._node._touchEnable) + ")\n"
        pass

    def __setButtonImage(self):
        global RESULT_OUPUT, TAB_SPACE
        if self._node._n_img != "" and self._node._s_img != "" and self._node._d_img != "":
            RESULT_OUPUT += TAB_SPACE + self._node.getName() + ":setImage(\"" + self._node._n_img + "\", \"" + self._node._s_img + "\", \"" + self._node._d_img + "\")\n"
        elif self._node._n_img != "" and self._node._s_img != "":
            RESULT_OUPUT += TAB_SPACE + self._node.getName() + ":setImage(\"" + self._node._n_img + "\", \"" + self._node._s_img + "\")\n"
        elif self._node._n_img != "":
            RESULT_OUPUT += TAB_SPACE + self._node.getName() + ":setImage(\"" + self._node._n_img + "\")\n"
        pass

    # 限于图片和精灵使用
    def __setImage(self):
        global RESULT_OUPUT, TAB_SPACE
        if self._node._img != "":
            RESULT_OUPUT += TAB_SPACE + self._node.getName() + ":setImage(\"" + self._node._img + "\")\n"
        pass

    def create(self):
        global RESULT_OUPUT, TAB_SPACE
        if self._node.getClassName() == "LabelBMFont" :
            RESULT_OUPUT += TAB_SPACE + "local " + self._node.getName() + " = cc." + self._node.getClassName() + ":createWithBMFont(\"" + self._node._file + "\", \"" + self._node._text + "\")\n"
            pass
        elif self._node.getClassName() == "LabelTTF" :
            RESULT_OUPUT += TAB_SPACE + "local " + self._node.getName() + " = cc." + self._node.getClassName() + ":createWithTTF(\"" + self._node._file + "\", \"" + self._node._text + "\")\n"
            pass
        else :
            RESULT_OUPUT += TAB_SPACE + "local " + self._node.getName() + " = cc." + self._node.getClassName() + ":create()\n"
            pass
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
                if option["pressedData"]["path"] != None and option["disabledData"]["path"] != None:
                    self._node.setImage(option["normalData"]["path"], option["pressedData"]["path"], option["disabledData"]["path"])
                elif option["pressedData"]["path"] != None :
                    self._node.setImage(option["normalData"]["path"], option["pressedData"]["path"], "")
                else :
                    self._node.setImage(option["normalData"]["path"], "", "")
                pass
            elif node["classname"] == "Panel":
                print "正在解析Panel/parsing Panel"
                self._node = Panel(option["name"])
                if option["backGroundImageData"] != None:
                    if option["backGroundImageData"]["path"] != None:
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
                if option["fontFile"] != None:
                    self._node.setFileName(option["fontFile"])
                self._node.setText(option["fontSize"])
                self._node.setMaxLen(option["maxLength"])
                self._node.setMaxLenEnable(option["maxLengthEnable"])
                self._node.setPwdEnable(option["passwordEnable"])
                self._node.setPwdStyleText(option["passwordStyleText"])
                self._node.setPlaceHolder(option["placeHolder"])
                self._node.setText(option["text"])
                pass
            elif node["classname"] == "LabelBMFont":
                print "正在解析LabelBMFont/parsing LabelBMFont"
                self._node = LabelBMFont(option["name"])
                self._node.setFileName(option["fileNameData"]["path"])
                self._node.setText(option["text"])
                pass
            else:
                print "无法解析该格式" + option["name"] + "/can not parse the object" + option["name"]
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
        self.create()
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

        if self._node.getClassName() == "Label":
            self.__setFontSize()
            self.__setText()
            pass
        elif self._node.getClassName() == "Button":
            self.__setButtonImage()
            self.__setFontSize()
            self.__setText()
            pass
        elif self._node.getClassName() == "Panel":
            self.__setImage()
            pass
        elif self._node.getClassName() == "ImageView":
            self.__setImage()
            pass
        elif self._node.getClassName() == "ListView":
            self.__setImage()
            pass
        elif self._node.getClassName() == "ScrollView":
            self.__setImage()
            pass
        elif self._node.getClassName() == "PageView":
            self.__setImage()
            pass
        elif self._node.getClassName() == "Slider":

            pass
        elif self._node.getClassName() == "LoadingBar":

            pass
        elif self._node.getClassName() == "CheckBox":

            pass
        elif self._node.getClassName() == "TextField":
            self.__setFontSize()
            self.__setPlaceHolder()
            self.__setMaxLenEnable()
            self.__setMaxLen()
            self.__setPwdEnable()
            self.__setPwdStyleText()
            self.__setText()
            pass
        elif self._node.getClassName() == "LabelBMFont":

            pass
        else:
            print "无法解析该格式" + self._node.getClassName() + "/can not parse the object" + self._node.getClassName()
            return

        pass


# 获取json文件对象
def getWidgetTreeRoot(read_path) :
    if (os.path.exists(read_path)) :
        if (os.path.isfile(read_path)) :
            fp = open(read_path, 'r')
            rp = fp.read()
            return json.loads(rp)

# 写入文件
def saveFile(save_path):
    save = file(savePath, "a+")
    global RESULT_OUPUT
    save.write(RESULT_OUPUT)
    save.close()

# 处理json对象数据
def handleTree() :
    global DESIGN_WIDTH, DESIGN_HEIGHT, IMG_LIST, RESULT_OUPUT
    DESIGN_WIDTH = WIDGET_TREE_ROOT["designWidth"]
    DESIGN_HEIGHT = WIDGET_TREE_ROOT["designHeight"]
    IMG_LIST = WIDGET_TREE_ROOT["texturesPng"]

    addLayer()
    setTreeRoot(WIDGET_TREE_ROOT["widgetTree"])

    global RESULT_OUPUT,TAB_SPACE
    RESULT_OUPUT += TAB_SPACE + "layer:addChild(" + WIDGET_TREE_ROOT["widgetTree"]["options"]["name"] + ")\n\n"

    recursiveTree(WIDGET_TREE_ROOT["widgetTree"], WIDGET_TREE_ROOT["widgetTree"]["children"])

def setTreeRoot(root) :
    solution = Solution()
    option = root["options"]

    solution.initData(root, option)
    solution.handleData()

def setNode(parent, node) :
    if node == None or node == []:
        return
    solution = Solution()
    option = node["options"]

    solution.initData(node, option)
    solution.handleData()
    addChild(parent, node)

def addLayer():
    global RESULT_OUPUT,TAB_SPACE
    RESULT_OUPUT += TAB_SPACE + "local layer = cc.Layer:create()\n"
    pass

def addChild(parent, node):
    global RESULT_OUPUT,TAB_SPACE
    RESULT_OUPUT += TAB_SPACE + parent["options"]["name"] + ":addChild(" + node["options"]["name"] + ")\n"
    pass

# 腾笼换鸟
def addClass(clsName):
    global RESULT_OUPUT
    str1 = "local " + clsName + " = class(\"" + clsName + "\", cc.load(\"mvc\").ViewBase)\n"
    str2 = "function " + clsName + ":onCreate()\n"
    str3 = "end\n"
    str4 = "return " + clsName + "\n"
    RESULT_OUPUT = str1 + str2 + RESULT_OUPUT + str3 + str4
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

def getOpenFileName():
    fileName = askopenfilename()
    return fileName

def getSaveFileName():
    fileName = asksaveasfilename()
    return fileName

if __name__ == '__main__':
    # print "脚本名:", sys.argv[0]
    # for i in range(1, len(sys.argv)):
    #     print "参数", i, sys.argv[i]

    readPath = getOpenFileName()
    print readPath
    if (readPath == None) :
        print "文件路径不存在/The file is not exist"
        sys.exit(1)
    if (not readPath.endswith(".json")) :
        print "该文件不是json文件/The file is not json"
        sys.exit(1)

    WIDGET_TREE_ROOT = getWidgetTreeRoot(readPath)
    if WIDGET_TREE_ROOT == None :
        print "json对象为空/json object is null"
        sys.exit(1)

    handleTree()

    savePath = getSaveFileName()
    print savePath

    fileName = os.path.basename(savePath)
    idx = fileName.index(".")
    clsName = fileName[:idx]
    addClass(clsName)

    saveFile(savePath)

    print RESULT_OUPUT

# def abc():
#     name = askopenfilename()
#     print name
#
# root = Tk()
# root.title("Cocostudio")
# errmsg = 'Error!'
# Button(root, text='File Open', width=30, height=2, command = abc).pack()
# root.mainloop()