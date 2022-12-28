from enum import Enum


class PyutStereotype(Enum):
    """
    Class Stereotype
    """
    AUXILIARY            = 'auxiliary'
    FOCUS                = 'focus'
    IMPLEMENTATION_CLASS = 'implementationClass'
    METACLASS            = 'metaclass'
    TYPE                 = 'type'
    UTILITY              = 'utility'

    @classmethod
    def toEnum(cls, strValue: str) -> 'PyutStereotype':
        """
        Converts the input string to the appropriate stereotype
        Args:
            strValue:   A string value
        Returns:  The stereotype enumeration
        """
        canonicalStr: str            = strValue.strip(' ').lower()
        stereotype:   PyutStereotype = PyutStereotype.TYPE
        match canonicalStr:
            case PyutStereotype.AUXILIARY.value:
                stereotype = PyutStereotype.AUXILIARY
            case PyutStereotype.FOCUS.value:
                stereotype = PyutStereotype.FOCUS
            case PyutStereotype.IMPLEMENTATION_CLASS.value:
                stereotype = PyutStereotype.IMPLEMENTATION_CLASS
            case PyutStereotype.METACLASS.value:
                stereotype = PyutStereotype.METACLASS
            case PyutStereotype.TYPE.value:
                stereotype = PyutStereotype.TYPE
            case PyutStereotype.UTILITY.value:
                stereotype = PyutStereotype.UTILITY
            case _:
                print(f'Warning: did not recognize this  stereotype: {canonicalStr}')

        return stereotype
