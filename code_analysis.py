import xml.etree.ElementTree as ET
import tempfile 
import subprocess
import os
import sys
import re
from functools import reduce
from typing import List, Dict


# One way to parse the contents of <analysis> and extract the set of program counters
# from the "coverage" key is using the following regex:
#     r'(?:\s|.)*(\"coverage\"\s\|->(?:\s+SetItem\s\(\s[0-9]+\s\))+)(?:\s|.)*'
# and then compute the list of pcounters:
#     pcounts = [x for x in match.group(1).split() if x.isdigit()]
# This approach is very slow when the number of SetItems increases.
# The following function is fast and should return an equivalent result:
def parse_coverage(content: str) -> List[str]:
    # constants
    buf = list(content)
    buf_len = len(buf)
    setitem_len = len('SetItem ( ')
    # c = counter which first jumps over the "coverage" key in the K map
    c = content.index('"coverage"') + len('"coverage" |->')
    # pcounters: List[List[str]]
    pcounters = []
    # `and` is short circuiting so buf[c] will not throw an exception if c is too large
    while c < buf_len and (buf[c] == '\n' or buf[c] == ' ' or buf[c] == 'S'):
        if buf[c] == 'S':
            c = c + setitem_len
            # parse the program counter numbers
            num = []
            while buf[c].isdigit():
                num.append(buf[c])
                c = c + 1
            pcounters.append(num)
            c = c + len(' )')
        if buf[c] == '\n' or buf[c] == ' ':
            c = c + 1
    return [reduce(lambda s1, s2: s1 + s2, x, '') for x in pcounters]

def parse_program(content: str) -> Dict[str, str]:
    buf = list(content)
    buf_len = len(buf)
    op_len = len('|-> ')
    c = content.index('"currentProgram" |-> (') + len('"currentProgram" |-> (')
    program = {}
    while c < buf_len and buf[c] != ')':
        key = []
        value = []
        if buf[c].isdigit():
            while c < buf_len and buf[c].isdigit():
                key.append(buf[c])
                c = c + 1
            c = c + op_len
            while c < buf_len and buf[c] != '\n':
                print(buf[c])
                value.append(buf[c])
                c = c + 1
            program[''.join(key)] = ''.join(value)
        if buf[c] == '\n' or buf[c] == ' ':
            c = c + 1
    return program

# run: python code_analysis.py "tests/ethereum-tests/VMTests/vmArithmeticTest/fibbonacci_unrolled.json"
# TODO: error handling :)
def main():
   # mode = sys.argv[1]
   # schedule = sys.argv[2]
    test_file_path = sys.argv[1]
    os.environ['MODE'] = "COVERAGE"
    os.environ['SCHEDULE'] = "DEFAULT"
    try:
        krun_output_file = tempfile.NamedTemporaryFile()
        subprocess.run(args=["./kevm", "run", "--backend", "java",
                             test_file_path, "-w", "none", "--output-file",
                             krun_output_file.name])
        #               check=True)
        k_final_config = krun_output_file.read()
        tree = ET.ElementTree(ET.fromstring(k_final_config))
        coverage_kmap = tree.getroot().find('analysis').text
        print(parse_coverage(coverage_kmap))
    # except FileNotFoundError as fnf_error:
    #     print("file err")
    #     print(fnf_error)
    # except subprocess.SubprocessError as error:
    #     print("subproc err")
    #     print(error)
    finally:
        krun_output_file.close()

# if __name__ == "__main__":
#     main()
