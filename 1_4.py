import xml.etree.ElementTree as et


tree = et.ElementTree(file="cont.xml")
root = tree.getroot()

for elem in root:
    # print(elem.attrib["name"])
    if elem.attrib["name"]=="新加坡":    
        neighbor = et.SubElement(elem,"neighbor")
        neighbor.set("name","亞特蘭提斯")
        neighbor.set("direction","南")
    
    if elem.attrib["name"]=="愛爾蘭":
        gdppc = elem.find("gdppc")
        gdppc.text="88888"
tree.write("cont2.xml",encoding="utf-8")

newtree = et.ElementTree(file="cont2.xml")
root2 = newtree.getroot()
for elem in root2:
    # print(elem)
    country = elem.attrib["name"]
    neighbor_list = elem.findall("neighbor")
    for neighbors in neighbor_list:
        print(f"{country}:{neighbors.attrib['name']}")
        print(f"{neighbors.attrib['name']}:{country}")
        