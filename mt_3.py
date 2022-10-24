import xml.etree.ElementTree as et
tree = et.ElementTree(file="data1.xml")
root = tree.getroot()
newrow = et.Element("row")
root.append(newrow)
sno = et.SubElement(newrow,"sno")
sno.text = "1033"
sna = et.SubElement(newrow,"sna")
sna.text="家樂福新店店"
tot = et.SubElement(newrow,"tot")
tot.text = "30"
sbi = et.SubElement(newrow,"sbi")
sbi.text="29"
sarea = et.SubElement(newrow,"sarea")
sarea.text="新店區"
for elem in root:
    if elem.find("sno").text =="1018":
        elem.find("sbi").text ="0"
tree.write("data2.xml",encoding="utf-8")

newtree = et.ElementTree(file="data2.xml")
root2 = newtree.getroot()
for elem in root2:
    if elem.find("sarea").text == "新店區":
        print(elem.find("sno").text,elem.find("sna").text,elem.find("tot").text,elem.find("sbi").text)
