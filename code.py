#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def quota(s):
    return '"' + s + '"'

def _tuple(f, ts):
    s = '(' + f(ts[0])
    for t in ts[1:]:
        s += ', ' + f(t)
    s += ')'
    return s

def tuplea(*ts):
    return _tuple(lambda x: str(x), ts)

def tuplei(*ts):
    return _tuple(lambda x: str(int(x)), ts)

def tuplef(*ts):
    return _tuple(lambda x: str(float(x)), ts)

def tuples(*ts):
    return _tuple(lambda x: quota(x), ts)

def color2hex(color):
    r, g, b = 255, 255, 255
    if 'R' in color:
        r = color['R']
    if 'G' in color:
        g = color['G']
    if 'B' in color:
        b = color['B']
    def cs(n):
        return hex(n)[2:].zfill(2)
    return '0x' + cs(r) + cs(g) + cs(b)

def cline(*ls):
    s = ''
    for l in ls:
        s += str(l)
    s += ';\n'
    return s

def rmpathpre(s):
    if s[:11] == 'sxd-res/cn/':
        return s[11:]
    else:
        return s

def new(name, type):
    return 'var ' + name + ' = new ' + type + '();\n'

def setAnchorPoint(item):
    x, y = 0, 0
    if 'AnchorPoint' in item:
        ap = item['AnchorPoint']
        if 'ScaleX' in ap:
            x = ap['ScaleX']
        if 'ScaleY' in ap:
            y = ap['ScaleY']
    return cline(item['Name'], '.setAnchorPoint', tuplef(x, y))

def setContentSize(item):
    x, y = 0, 0
    if 'Size' in item:
        sz = item['Size']
        if 'X' in sz:
            x = sz['X']
        if 'Y' in sz:
            y = sz['Y']
    return cline(item['Name'], '.setContentSize', tuplei(x, y))

def setPosition(item):
    x = item['Position']['X']
    y = item['Position']['Y']
    return cline(item['Name'], '.setPosition', tuplef(x, y))

def setGlobalFontSize(item):
    return cline(item['Name'], '.setGlobalFontSize', tuplei(item['FontSize']))

def setGlobalFontColor(item):
    color = item['CColor']
    c_pi = 'pi.intToColor' + tuplea(color2hex(color))
    return cline(item['Name'], '.setGlobalFontColor', tuplea(c_pi))

def setGlobalAlignment(item):
    if 'HorizontalAlignmentType' in item:
        align = item['HorizontalAlignmentType']
        if align == 'HT_Center':
            return cline(item['Name'], '.setGlobalAlignment', tuplea('kPITextAlignment.Center'))
        elif align == 'HT_Right':
            return cline(item['Name'], '.setGlobalAlignment', tuplea('kPITextAlignment.Right'))
    return ""

def setText(item):
    s = item['LabelText']
    if s == '':
        return ''
    s = s.replace('\r\n', '\\n')
    s = s.replace('\n', '\\n')
    s = s.replace('\r', '\\n')
    return cline(item['Name'], '.setText(_T', tuples(s), ')')

def setImage(item):
    path = rmpathpre(item['FileData']['Path'])
    if path == 'Default/Sprite.png':
        return ''
    return cline(item['Name'], '.setImage', tuples(path))

def setImage_Button(item):
    # 无图片的按钮需要设置大小
    if not 'NormalFileData' in item:
        return setContentSize(item)
    path = rmpathpre(item['NormalFileData']['Path'])
    folder = '/'.join(path.split('/')[:-1])
    imgs = []
    def rimg(name):
        if name in item:
            path = rmpathpre(item[name]['Path'])
            img = path.split('/')[-1]
            imgs.append(img)
    rimg('NormalFileData')
    rimg('PressedFileData')
    rimg('DisabledFileData')
    return cline(item['Name'], '.setImage', tuples(folder, *imgs))

def setText_Button(item):
    name = item['Name']
    s = item['ButtonText']
    if s == '':
        return ''
    color = item['TextColor']
    size = item['FontSize']
    c_pi = 'pi.intToColor' + tuplea(color2hex(color))
    output = cline(item['Name'], '.setText', tuplea('_T(' + quota(s) + ')', c_pi, size))
    output += cline(name, '.spriteText()', '.setGlobalFontSize', tuplei(size))
    output += cline(name, '.spriteText()', '.setGlobalFontColor', tuplea(c_pi))
    return output

def clear(item):
    return cline(item['Name'], '.clear()')

def setDimension(item):
    w1, h1 = 0, 0
    w2, h2 = item['Scale9Width'], item['Scale9Height']
    if 'Scale9OriginX' in item:
        w1 = item['Scale9OriginX']
    if 'Scale9OriginY' in item:
        h1 = item['Scale9OriginY']

    output = ''
    name = item['Name']
    w3 = name + 'W3'
    h3 = name + 'H3'
    output += cline('var ', w3, ' = ', name, '.getWholeImage().getOriginalSize().width', ' - ', w1, ' - ', w2)
    output += cline('var ', h3, ' = ', name, '.getWholeImage().getOriginalSize().height', ' - ', h1, ' - ', h2)

    def dimone(type, w, h):
        tp = 'kPIEdgeType.' + type
        sz = 'cc.size' + tuplea(w, h)
        return cline(name, '.setDimension', tuplea(tp, sz))

    output += dimone('LeftTop', w1, h1)
    output += dimone('Top', w2, h1)
    output += dimone('RightTop', w3, h1)
    output += dimone('Left', w1, h2)
    output += dimone('Center', w2, h2)
    output += dimone('Right', w3, h2)
    output += dimone('LeftBottom', w1, h3)
    output += dimone('Bottom', w2, h3)
    output += dimone('RightBottom', w3, h3)
    return output

def setScale(item):
    scaleX = 1.0
    scaleY = 1.0
    if 'Scale' in item:
        scale = item['Scale']
        if 'ScaleX' in scale:
            scaleX = scale['ScaleX']
        if 'ScaleY' in scale:
            scaleY = scale['ScaleY']
    if scaleX == 1.0 and scaleY == 1.0:
        return ''
    else:
        return cline(item['Name'], '.setScale', tuplef(scaleX, scaleY))

def setVisible(item):
    vis = True
    if 'VisibleForFrame' in item:
        vis = item['VisibleForFrame']
    if vis == True:
        return ''
    else:
        return cline(item['Name'], '.setVisible', tuplea('false'))

def addChild(name_p, item):
    if item['IsPrefab']:
        return ''
    name_c = item['Name']
    if name_c == '_w_close':
        return cline(name_p, '.addChild', tuplea(name_c, 'pi.Int32Max'))
    return cline(name_p, '.addChild', tuplea(name_c))

def addChildren(parent, children, nodes):
    output = ''
    for child in children:
        # prefab
        if child['Name'][0] == '$':
            child['IsPrefab'] = True
            child['Name'] = child['Name'][1:]
            output += procPrefab(parent, child)
        else:
            child['IsPrefab'] = False
            output += procByType(parent, child)
            output += '\n'
            nodes.append(child['Name'])
            if 'Children' in child:
                output += addChildren(child['Name'], child["Children"], nodes)
    return output

def setNodeName(nodes):
    output = ''
    for n in nodes:
        if n.find('$') < 0:
            output += cline(n, '.setNodeName', tuples(n))
    output += '\n'
    return output

def saveNodes(parent, nodes):
    output = ''
    for n in nodes:
        if n.find('$') < 0:
            output += cline(parent, '.', n, ' = ', n)
    return output

def readFile(path):
    f = open(path, 'r')
    s = f.read()
    f.close()
    return s

def procByType(parent, child):
    output = ''
    type = child['ctype']
    if type == 'PanelObjectData':
        output += procPanel(parent, child)
    elif type == 'TextObjectData':
        output += procText(parent, child)
    elif type == 'SpriteObjectData':
        output += procSprite(parent, child)
    elif type == 'ImageViewObjectData':
        output += procImageView(parent, child)
    elif type == 'ButtonObjectData':
        output += procButton(parent, child)
    elif type == 'ListViewObjectData':
        output += procListView(parent, child)
    elif type == 'PageViewObjectData':
        output += procPageView(parent, child)
    else:
        print '未知控件类型：', type
        return ''
    return output

def procPrefab(parent, item):
    nodes = []
    name = item['Name']
    output = (
        'self.' + 'PF_' + name + ' = function() {\n'
        + procByType(parent, item)
        + '\n'
        + addChildren(name, item['Children'], nodes)
        + setNodeName(nodes)
        + saveNodes(name, nodes)
        + 'return '+ name + ';\n'
        + '};\n\n'
    )
    # 删去子节点
    item['Children'] = []
    return output

# cc.Node
def procPanel(parent, item):
    output = ''
    name = item['Name']

    # prefab 实例
    idx = name.find('$')
    if(idx >= 0):
        type = name[:idx]
        item['Name'] = name = name[idx+1:]
        output = 'var ' + name + ' = self.PF_' + type + '();\n'
    # 普通节点
    else:
        output = new(name, 'cc.Node')

    # 设置节点自有属性
    output = (
        output
        + setAnchorPoint(item)
        + setContentSize(item)
        + setPosition(item)
        + setVisible(item)
        + addChild(parent, item)
    )
    return output

# pi.Text
def procText(parent, item):
    name = item['Name']
    pre = name[:2]
    typet = 'pi.Text'
    if pre == 'lk':
        typet = 'pi.Link'
    elif pre == 'cd':
        typet = 'pi.CDTime'
    output = (
        new(name, typet)
        + setAnchorPoint(item)
        + setContentSize(item)
        + setPosition(item)
        + setGlobalFontSize(item)
        + setGlobalFontColor(item)
        + setGlobalAlignment(item)
        # + setText(item)
        + setVisible(item)
        + addChild(parent, item)
    )
    if pre != 'tx' and pre != 'cd':
        output += setText(item)
    return output

# pi.UIBase
def procSprite(parent, item):
    name = item['Name']
    output = (
        new(name, 'pi.UIBase')
        + setAnchorPoint(item)
        + setPosition(item)
        + setImage(item)
        + setScale(item)
        + setVisible(item)
        + addChild(parent, item)
    )
    return output

# pi.Scale9
def procImageView(parent, item):
    name = item['Name']
    output = (
        new(name, 'pi.Scale9')
        + setAnchorPoint(item)
        + setPosition(item)
        + clear(item)
        + setImage(item)
        + setDimension(item)
        + setContentSize(item)
        + setVisible(item)
        + addChild(parent, item)
    )
    return output

# pi.Button
def procButton(parent, item):
    name = item['Name']
    output = (
        new(name, 'pi.Button')
        + setAnchorPoint(item)
        + setPosition(item)
        + setImage_Button(item)
        + setText_Button(item)
        + setScale(item)
        + setVisible(item)
        + addChild(parent, item)
    )
    return output

# PIScroll
def procListView(parent, item):
    name = item['Name']
    output = (
        new(name, 'PIScroll')
        + setContentSize(item)
        + setAnchorPoint(item)
        + setPosition(item)
        + setVisible(item)
        + addChild(parent, item)
    )
    if 'DirectionType' in item and item['DirectionType'] == 'Vertical':
        output += cline(name, '.setVScroll()')
    else:
        output += cline(name, '.setHScroll()')
    
    if 'Children' in item:
        nodes = []
        output += '\n'
        output += 'self.' + name + '_NormalItem = function() {\n'
        output += 'var item = new cc.Node();\n'
        output += setContentSize({'Name': 'item', 'Size': item['Children'][0]['Size']})
        if 'Children' in item['Children'][0]:
            output += addChildren('item', item['Children'][0]['Children'], nodes)
        output += setNodeName(nodes)
        output += saveNodes('item', nodes)
        output += 'return item;\n'
        output += '};\n'
        # 删去子节点
        item['Children'] = []
    return output

# PIPageView
def procPageView(parent, item):
    name = item['Name']
    output = (
        new(name, 'PIPageView2')
        + setContentSize(item)
        + setAnchorPoint(item)
        + setPosition(item)
        + setVisible(item)
        + addChild(parent, item)
    )
    if 'Children' in item and 'Children' in item['Children'][0]:
        nodes = []
        output += name + '.bindLoad(function() {\n'
        output += 'var page = new cc.Node();\n'
        output += addChildren('page', item['Children'][0]['Children'], nodes)
        output += setNodeName(nodes)
        output += saveNodes('page', nodes)
        output += 'return page;\n'
        output += '});\n'
        # 删去子节点
        item['Children'] = []
    return output

# 复制到剪贴板
import subprocess
def write_to_clipboard(output):
    process = subprocess.Popen(
        'pbcopy', env={'LANG': 'zh_CN.UTF-8'}, stdin=subprocess.PIPE)
    process.communicate(output)

path = sys.argv[1]
nodes = []
root = json.loads(readFile(path))
children = root['Content']['Content']['ObjectData']['Children']
output = 'ctor: function() {\n'
output += 'this._super();\n'
output += 'this.setNodeName("UIRoot");\n'
output += 'var self = this;\n\n'
output += addChildren('self', children, nodes)
output += setNodeName(nodes)
output += saveNodes('self', nodes)
output += '}'
# print(output)
write_to_clipboard(output)
print('已复制到剪贴板')
