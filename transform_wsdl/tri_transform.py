import sys
from lxml import etree

def parsexml(xmlfile ):

    # get root element
    root = etree.parse(xmlfile)#fromstring(bytes(xml, 'utf-8'))

    # create empty list for news items
    arrayOfTypes = []
    arrayOfTypeElements = {}

    ns = {
        'wsdl': 'http://schemas.xmlsoap.org/wsdl/',
        'xsd': 'http://www.w3.org/2001/XMLSchema'}

    # wsdl:types/xsd:schema/xsd:complexType[@name=\'ArrayOfField\']
    # [@name[starts-with(.,\'ArrayOf\')]]

    for item in root.findall('wsdl:types/xsd:schema/xsd:complexType', ns):
        if item.attrib['name'].startswith('ArrayOf'):
            # print(item.attrib['name'])
            arrayOfTypes.append(item.attrib['name'])
            subTypeNameElement = item.find('xsd:sequence/xsd:element', ns)
            subTypeName = subTypeNameElement.attrib['type']
            subTypeName = subTypeName[subTypeName.find(':')+1:]

            print(item.attrib['name']+":"+subTypeName )
            arrayOfTypeElements[item.attrib['name']] = subTypeName
            # item.getparent().remove(item)


    # for arrayType in arrayOfTypes:
    SUBSTRING_LEN = len("tns:ArrayOf")

    for item in root.findall('.//xsd:element',ns):
        if item.attrib['type'].find("ArrayOf") > 0:
            prefix = item.attrib['type'][0:4]
            print('Processing:'+ item.attrib['type'])
            idx = item.attrib['type'][SUBSTRING_LEN:].find("Long")

            if item.attrib['type'][SUBSTRING_LEN:].find('Long') > -1:
                item.attrib['type'] = 'xsd:' + 'long'
            elif item.attrib['type'][SUBSTRING_LEN:].find('String') > -1:
                item.attrib['type'] = 'xsd:' + 'string'
            else:
                item.attrib['type'] = prefix + arrayOfTypeElements[item.attrib['type'][len(prefix):]]
                # item.attrib['type'][SUBSTRING_LEN:]

            item.attrib['maxOccurs'] = 'unbounded'

    return [etree, root]


def printwsdl(tree, root, filename):
    obj_xml = tree.tostring(root, pretty_print=True)

    # print(obj_xml)
    with open(filename, 'w') as f:
        f.write(str(obj_xml, 'utf-8'))


def main(inputfile, outputfile):
    # load rss from web to update existing xml file
    # loadRSS()

    # parse xml file
    inputWSDL = parsexml(inputfile)

    # store news items in a csv file
    printwsdl(inputWSDL[0], inputWSDL[1], outputfile)


if __name__ == "__main__":
    # calling main function
    main(sys.argv)
