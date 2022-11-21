# For autocomplete
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .PyKrita import *

from .toolTweeks import ToolTweeks

Krita.instance().addExtension(ToolTweeks(Krita.instance()))

