import parse_konfig
import subprocess
import tempfile
import json
import os

def run_kevm_test(test_file_path):
    krun_output_file = tempfile.NamedTemporaryFile()
    os.environ['MODE'] = "COVERAGE"
    os.environ['SCHEDULE'] = "DEFAULT"
    subprocess.run(args=["./kevm", "run", "--backend", "java",
                         test_file_path, "-w", "none", "-o", "json", "--output-file",
                         krun_output_file.name])
    konfig = krun_output_file.read()
    konfig_dict = json.loads(konfig.decode('utf-8'))
    return konfig_dict 

def get_program_pcs(konfig_dict):
    analysis_contents = parse_konfig.get_analysis_cell_contents(konfig_dict)
    analysis_dict = parse_konfig.parse_kmap(analysis_contents)
    return list(parse_konfig.parse_kmap(analysis_dict['"currentProgram"']).keys())

def get_test_pcs(konfig_dict):
    analysis_contents = parse_konfig.get_analysis_cell_contents(konfig_dict)
    analysis_dict = parse_konfig.parse_kmap(analysis_contents)
    return parse_konfig.parse_kset(analysis_dict['"coverage"'])

def calculate_coverage(test_files):
    buf = test_files
    konfig_dict = run_kevm_test(buf[0])
    program_pcs = get_program_pcs(konfig_dict)
    test_pcs = get_test_pcs(konfig_dict)
    covered_pcs = []
    covered_pcs.extend(test_pcs)
    buf.pop(0)
    # maybe run this in parallel?
    for test in buf:
        konfig_dict = run_kevm_test(test)
        test_pcs = get_test_pcs(konfig_dict)
        covered_pcs.extend(test_pcs)
    covered_pcs = set(covered_pcs)
    print('Opcode coverage percentage: ', len(covered_pcs)/len(program_pcs)*100)



