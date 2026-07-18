#!/usr/bin/env python3
"""Module to serialize and deserialize dictionaries using XML."""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serializes a Python dictionary to an XML file."""
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """Deserializes an XML file to a Python dictionary."""
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        
        result_dict = {}
        for child in root:
            result_dict[child.tag] = child.text
            
        return result_dict
    except Exception:
        return None
