
from typing import List
from typing import NewType

from pyutmodel.PyutField import PyutField
from pyutmodel.PyutMethod import PyutMethod

ClassName    = NewType('ClassName', str)
Implementors = NewType('Implementors', List[ClassName])
