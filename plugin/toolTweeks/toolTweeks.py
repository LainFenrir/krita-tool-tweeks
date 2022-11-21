"""
    tweeks 
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
from .referencePosition import ReferencePosition
from PyQt5.QtCore import QTimer

class ToolTweeks(Extension):
    def __init__(self, parent):
        super().__init__(parent)
        self.refPos = ReferencePosition()

    # Krita.instance() exists, so do any setup work
    def setup(self):
        # Setting up a notifier to only run the code when the window is ready
        # Its necessary to wait the window to be created otherwise qwindow() is null
        appNotifier  = Krita.instance().notifier()
        appNotifier.windowCreated.connect(self.connectActions)
        appNotifier.imageCreated.connect(self.createTimer)

        pass

    # called after setup(self)
    def createActions(self, window):
        pass

    def connectActions(self):
        Krita.instance().action('KritaFill/KisToolFill').triggered.connect(self.refPos.fillPosition)
        Krita.instance().action('KisToolEncloseAndFill').triggered.connect(self.refPos.enclosedPosition)
        Krita.instance().action('KisToolSelectSimilar').triggered.connect(self.refPos.similarPosition)
        Krita.instance().action('KisToolSelectContiguous').triggered.connect(self.refPos.contiguosPosition)
        pass
    
    def createTimer(self):
        if self.refPos.allPosChanged:
            return
        self.timer=QTimer()
        self.timer.singleShot(3000, self.triggerActions)
        
    def triggerActions(self):
        Krita.instance().action('KritaFill/KisToolFill').trigger()
        Krita.instance().action('KisToolEncloseAndFill').trigger()
        Krita.instance().action('KisToolSelectSimilar').trigger()
        Krita.instance().action('KisToolSelectContiguous').trigger()
        Krita.instance().action('KritaShape/KisToolBrush').trigger()