# Alias -meaning that everytime I'm using the name ET
# I'm actually referring to ElementTree.
import xml.etree.ElementTree as ET

path = './/food.xml'

# Reads the file in path and desearilize it from XML to tree (object).
tree = ET.parse(path)
root = tree.getroot()

foods = root.findall('food')
for food in foods:
    # Looking for tags named 'name' and 'price' and returns its value:
    name = food.find('name').text
    price = food.find('price').text

    # Printing it
    print('The food name is {} and its price is {}'.format(name, price))
# for product in root:
#     if product.tag=='good':
#         print(product.find('name'))
