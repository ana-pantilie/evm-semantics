import xml.etree.ElementTree as ET

# run krun with MODE=VMTESTS SCHEDULE=DEFAULT ./kevm run --backend java tests/ethereum-tests/VMTests/vmArithmeticTest/add0.json -w none --output-file <output-file-name>.xml
tree = ET.parse('test.xml')
pcounts = [x for x in tree.getroot().find('analysis').text.split() if x.isdigit()]
print(pcounts)
