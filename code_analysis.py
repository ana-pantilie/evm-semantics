import xml.etree.ElementTree as ET
import tempfile 
import subprocess
import os
import sys
import re

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
        coverage_kmap = tree.getroot().find('analysis').text
        # veeery slow
        # parser = re.compile(r'(?:\s|.)*(\"coverage\"\s\|->(?:\s+SetItem\s\(\s[0-9]+\s\))+)(?:\s|.)*') 
        # match = parser.match('abcdefg\n "coverage" |-> SetItem ( 0 ) \n SetItem ( 2 )   \n lalalalala ')
        # if match:
        #     print(match.group(1))
        #     # pcounts = [x for x in match.group(1).split() if x.isdigit()]
        #     # print(pcounts)
        # else:
        #     print("nope")
        first = coverage_kmap.index('"coverage"') + len('"coverage" |->')
        setitem_len = len('SetItem ( ')
        buf = list(coverage_kmap)
        # print(buf)
        c = first
        pcounters = []
        while buf[c] == '\n' or buf[c] == ' ' or buf[c] == 'S':
            print(buf[c])
            if buf[c] == 'S':
                c = c + setitem_len
                num = []
                while buf[c].isdigit():
                    num.append(buf[c])
                    c = c + 1
                pcounters.append(num)
                c = c + len(' )')
            if buf[c] == '\n' or buf[c] == ' ':
                c = c + 1
        print(pcounters)
    # except:
    finally:
        krun_output_file.close()

if __name__ == "__main__":
    main()
