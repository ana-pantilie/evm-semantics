import xml.etree.ElementTree as ET
import tempfile 
import subprocess
import os
import sys

# test run: python code_analysis.py "VMTESTS" "DEFAULT" "tests/ethereum-tests/VMTests/vmArithmeticTest/fibbonacci_unrolled.json"
# TODO: error handling :)
def main():
    mode = sys.argv[1]
    schedule = sys.argv[2]
    test_file_path = sys.argv[3]
    krun_output_file = tempfile.NamedTemporaryFile()
    os.environ['MODE'] = mode
    os.environ['SCHEDULE'] = schedule
    try:
        subprocess.run(["./kevm", "run", "--backend", "java",
                        test_file_path, "-w", "none", "--output-file",
                        krun_output_file.name])
        k_final_config = krun_output_file.read()
        tree = ET.ElementTree(ET.fromstring(k_final_config))
        # should switch to regex?
        pcounts = [x for x in tree.getroot().find('analysis').text.split() if x.isdigit()]
        print(pcounts)
    # except:
    finally:
        krun_output_file.close()

if __name__ == "__main__":
    main()
