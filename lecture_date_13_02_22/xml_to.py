import xml.etree.ElementTree as ET
import csv


# Reads xml from path, and writes csv to dest_path (destination).
def from_xml_to_csv(path, dest_path):
    tree = ET.parse(path)
    root = tree.getroot()
    columns = []

    # Bring me the first tag that is inside root.
    example_food = root.find('food')

    # Go through all the tags inside example_food
    for inside_tag in example_food:
        # And for each one append it to a list.
        columns.append(inside_tag.tag)
    rows = []
    for tag in root:
        row = []
        for column in columns:
            cell = tag.find(column).text
            row.append(cell)
        if tag.tag == 'food':
            row.append('X')
        else:
            row.append('V')
        rows.append(row)
    columns.append('Is Good')
    with open(dest_path, 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(columns)
        csv_writer.writerows(rows)


if __name__ == '__main__':
    from_xml_to_csv('food.xml', 'new_food.csv')
