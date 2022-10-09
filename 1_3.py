import xml.etree.ElementTree as et
import json
# import pandas_read_xml as pdx
import xmltodict

def print_tree(root):
    for child in root:
        print('tag:', child.tag, 'attributes:', child.attrib)
        for grandchild in child:
            print('\ttag:', grandchild.tag, 'attributes:', grandchild.attrib)
tree = et.ElementTree(file='menu.xml')
root = tree.getroot()
data=[["beer","$10"],["skewers","$20"],["barbecue","$15"]]
Ns = et.Element("Nightsnack")
root.append(Ns)
Ns.set("hours","21-23")
for i in range(3):
    item = et.SubElement(Ns,"item")
    item.set("price",data[i][1])
    item.text=data[i][0]
    
# print_tree(root)
et.indent(tree)
tree.write("output.xml",encoding="utf-8")
with open("output.xml","r") as xml:
    tojson = xmltodict.parse(xml.read())
    with open("menuu.json","w",encoding="utf8") as mm :
        json.dump(tojson,mm) 

    # df = pdx.read_xml("output.xml")
    # tojson=df.to_json()
    # with open("menu.json","w",encoding="utf-8") as mm:
    #     json.dump(jsonf,mm, indent=2)