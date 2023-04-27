from xml.etree import ElementTree
import requests
import re

url = '../xml/fulldata_02_03_01_P_동물병원.xml'
tree = ElementTree.parse(url)
root = tree.getroot()

print(root)

for i in root:
    print(i)

print(root[0][0])
print(root[0][0][-6])







