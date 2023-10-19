import xml.etree.ElementTree as ET


def main():
    # read from kotus-sanalista_v1.xml
    input_path = "kotus-sanalista_v1/kotus-sanalista_v1.xml"

    # parse the XML file
    tree = ET.parse(input_path)
    root = tree.getroot()

    eight_letter_words = []

    # loop through all s elements
    for s in root.iter('s'):
        if (len(s.text) == 8):
            eight_letter_words.append(s.text)


if __name__ == "__main__":
    main()