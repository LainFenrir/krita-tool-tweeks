"""
    Collection of utilities to make plugins in krita
    Copyright (C) 2022  LunarKreatures

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
# For autocomplete
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .PyKrita import *
else:
    from krita import *
from PyQt5.QtWidgets import *

def getCurrentLayer():
    app = Krita.instance()
    doc = app.activeDocument()
    currentLayer = doc.activeNode()
    return currentLayer


def getCurrentDoc():
    app = Krita.instance()
    doc = app.activeDocument()
    return doc


def getSelectedLayers():
    w = Krita.instance().activeWindow()
    v = w.activeView()
    selectedNodes = v.selectedNodes()
    return selectedNodes


def findTypeInList(list,type):
    for item in list:
        if isinstance(item,type):
            return item
    return None

# Returns options of the tool in the tool options docker
# todo check if its none
def getToolOptionsFor(toolName):
    qdock = next((w for w in Krita.instance().dockers() if w.objectName() == 'sharedtooldocker'), None)
    wobj = qdock.findChild(QWidget,toolName)
    return wobj

# returns True if the there is a label with the content.
# useful find options in dockers
def childContainLabelWith(list,content):
    for c in list.children():
        if isinstance(c,QLabel):
            if c.text() == content:
                return True
    return False

# Returns the index of the a setting that contains a label with the settingName
# if it doesnt find it will return -1, so you need to check for this
def findSettingPosInListByLabel(list,settingName):
    for lChild in list:
        for child in lChild.children():
            if childContainLabelWith(child,settingName):
                return list.index(lChild)
    return -1

# Returns the position for a setting in the tooloptions docker
# Will return -1 if its not found
def findSettingPosInToolOptionsByName(toolName,settingName):
    toolW = getToolOptionsFor(toolName)
    dockerChildren = toolW.children()
    pos = findSettingPosInListByLabel(dockerChildren,settingName)
    return pos
    