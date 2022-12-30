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
    NO_STEREOTYPE        = 'No Stereotype'

    @classmethod
    def toEnum(cls, strValue: str) -> 'PyutStereotype':
        """
        Converts the input string to the appropriate stereotype

        Args:
            strValue:   A string value

        Returns:  The stereotype enumeration;  Empty strings, multi-spaces strings, & None
        values return PyutStereotype.NO_STEREOTYPE
        """
        stereotype:   PyutStereotype = PyutStereotype.NO_STEREOTYPE
        if strValue is None:
            canonicalStr: str = ''  # Force None
        else:
            canonicalStr = strValue.strip(' ').lower()

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
            case '':
                pass    # No stereotype
            case _:
                print(f'Warning: did not recognize this  stereotype: {canonicalStr}')

        return stereotype
