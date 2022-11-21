"""
    moves the reference setting in the tool options to be on the top
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
from .kritaUtils import findTypeInList,getToolOptionsFor,findSettingPosInListByLabel

class ReferencePosition(object):
    def __init__(self):
        super()
        self.fillPosChanged = False
        self.enclosedPosChanged = False
        self.contiguosPosChanged = False
        self.similarPosChanged = False
        self.allPosChanged = False

    # fill tool - index 5
    def fillPosition(self): 
        toolW = getToolOptionsFor('KritaFill/KisToolFill')
        toolChildren = toolW.children()
        layout = self.grabLayout(toolChildren)
        refW = self.getReferenceWidget(toolChildren)
        layout.insertWidget(2,refW)
        self.fillPosChanged = True
        pass


    # enclosed fill tool - index 6
    def enclosedPosition(self):
        toolW = getToolOptionsFor('KisToolEncloseAndFill')
        toolChildren = toolW.children()
        layout = self.grabLayout(toolChildren)
        refW = self.getReferenceWidget(toolChildren)
        layout.insertWidget(1,refW)
        self.enclosedPosChanged = True
        pass


    # contiguos selection tool - index 4
    def contiguosPosition(self):
        toolW = getToolOptionsFor('KisToolSelectContiguousoption widget')
        toolChildren = toolW.children()
        layout = self.grabLayout(toolChildren)
        refW = self.getReferenceWidget(toolChildren)
        layout.insertWidget(1,refW)
        self.contiguosPosChanged = True
        pass

    # Similar color selection tool - index 4
    def similarPosition(self):
        toolW = getToolOptionsFor('KisToolSelectSimilaroption widget')
        toolChildren = toolW.children()
        layout = self.grabLayout(toolChildren)
        refW = self.getReferenceWidget(toolChildren)
        layout.insertWidget(1,refW)
        self.similarPosChanged = True
        pass

    ## *                  ##
    ## * Auxiliar methods ##
    ## *                  ##
 

    #finds the reference widget based on position
    def getReferenceWidget(self,toolChildren):
        pos = self.lookForReference(toolChildren)
        refW = toolChildren[pos]
        return refW
        pass

    # Looks for the reference widget based on the Qlabel 
    def lookForReference(self,toolChildren):
        pos = findSettingPosInListByLabel(toolChildren,"Reference")
        return pos
        pass

    def grabLayout(self,toolChildren):
        layout = findTypeInList(toolChildren,QBoxLayout)
        return layout
        pass


    ## *              ##
    ## * Check status ##
    ## *              ##

    def arePositionsChanged(self):
        return self.allPosChanged

    def setPositionsChanged(self):
        if  self.fillPosChanged and self.enclosedPosChanged and self.contiguosPosChanged and self.similarPosChanged:
            self.allPosChanged = True