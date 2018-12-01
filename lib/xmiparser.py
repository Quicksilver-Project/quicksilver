# This file is to make sense of XMI formatted data
# Copyright (C) 2018 Logan Campos - @binaryflesh
#
# imports
import xml.etree.ElementTree as ET
from datetime import datetime


# https://www.omg.org/spec/XMI/2.5.1

"""
Every XMI schema consists of the following declarations:
• An XML version processing instruction. Example: <?XML version=”1.0”?>
• An optional encoding declaration that specifies the character set, which follows the ISO-10646 (also called extended
Unicode) standard. Example: <?XML version=”1.0” ENCODING=”UCS-2”?>
• Any other valid XML processing instructions.
• A schema XML element.
• An import XML element for the XMI namespace.
• Declarations for a specific model.
Every XMI document consists of the following declarations, unless the XMI is embedded in another XML document:
• An XML version processing instruction.
8 XML Metadata Interchange (XMI), v2.5.1
• An optional encoding declaration that specifies the character set.
• Any other valid XML processing instructions.
XMI imposes no ordering requirements beyond those defined by XML. XML Namespaces may also be declared in the
XMI element as described below.
The top element of the XMI information structure is either the XMI element, or an XML element corresponding to an
instance of a class in the MOF model. An XML document containing only XMI information will have XMI as the root
element of the document. It is possible for future XML exchange formats to be developed that extend XMI and embed
XMI elements within their XML elements.
"""

"""
<?XML version="1.0" encoding="UTF-8">
<xmi:XMI xmlns:xmi="http://www.omg.org/spec/XMI/20131001" xmlns:uml="http://www.omg.org/spec/UML/20161101" xmlns:mofext="http://www.omg.org/spec/MOF/20131001>
    <uml:Package xmi:type="uml:Package" xmi:id="_0" name="PrimitiveTypes" URI="http://www.omg.org/spec/PrimitiveTypes/20161101">
        <packagedElement xmi:type="uml:PrimitiveType" xmi:id="Boolean" name="Boolean">
			<ownedComment xmi:type="uml:Comment" xmi:id="Boolean-_ownedComment.0" annotatedElement="Boolean">
				<body>Boolean is used for logical expressions, consisting of the predefined values true and false.</body>
			</ownedComment>
		</packagedElement>
    </uml:Package>
</xmi:XMI>
"""

@dataclass
class Base_Documentation:
    """
        The Documentation class contains many fields to describe the document for
        non-computational purposes.
    """
    contact: str = field()
    exporter: str = field()
    exporterVersion: str = field()
    exporterID: str = field()
    longDescription: str = field()
    shortDescription: str = field()
    notice: str = field()
    owner: str = field()
    timestamp: datetime.timestamp = field()

@dataclass
class Base_Extension:
    """
     The Extension class contains the metadata for external information.
    """
    extender: str = field()
    extenderID: str = field()

@dataclass
class Base_Element:
    """
    """
    owner: Dict[str] = field(init=False)
    ownedElement: Dict[str] = field(init=False)

    def __add__(self, element=dict):
        try:
            self.item = element["ownedElement"]
            self.owner[self.item]["owner"] = element["owner"]
        except Exception as err:
            raise err
        finally:
            yield super(XMI.Difference(Base_Element))
        

#Everything needs to hook here so can change definitions
@dataclass
class XMI():
    """
    XMI 2.5.1 Definition
    """
    Documentation = Base_Documentation
    Extension = Base_Extension

    def __init__(self):
        #TODO: Defined ids
        #TODO: Defined types
        #TODO: Defined elements
        pass
    
    def Difference(self):
        pass

    def __add__(self, position): pass
    
    def __del__(self, object): pass # Call Difference


if __name__ == "__main__":
    PATH = "../data/UML/2.5.1/UML.xmi"
    tree = ET.parse(PATH)
    root = tree.getroot()
    for key, value in root.items():
        print(key, value)
        #print(dir(child))
        #pprint(f"{child.tag}\n\t{child.attrib}")