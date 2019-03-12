import json

test_set_json = '{"node":"KApply","label":"_Set_","variable":false,"arity":2,"args":[{"node":"KApply","label":"SetItem","variable":false,"arity":1,"args":[{"node":"KToken","sort":"Int","token":"0"}]},{"node":"KApply","label":"_Set_","variable":false,"arity":2,"args":[{"node":"KApply","label":"SetItem","variable":false,"arity":1,"args":[{"node":"KToken","sort":"Int","token":"33"}]},{"node":"KApply","label":"_Set_","variable":false,"arity":2,"args":[{"node":"KApply","label":"SetItem","variable":false,"arity":1,"args":[{"node":"KToken","sort":"Int","token":"66"}]},{"node":"KApply","label":"_Set_","variable":false,"arity":2,"args":[{"node":"KApply","label":"SetItem","variable":false,"arity":1,"args":[{"node":"KToken","sort":"Int","token":"67"}]},{"node":"KApply","label":"SetItem","variable":false,"arity":1,"args":[{"node":"KToken","sort":"Int","token":"69"}]}]}]}]}]}'

test_map_json = '{"node":"KApply","label":"_Map_","variable":false,"arity":2,"args":[{"node":"KApply","label":"_|->_","variable":false,"arity":2,"args":[{"node":"KToken","sort":"Int","token":"0"},{"node":"KApply","label":"PUSH","variable":false,"arity":2,"args":[{"node":"KToken","sort":"Int","token":"32"},{"node":"KToken","sort":"Int","token":"115792089237316195423570985008687907853269984665640564039457584007913129639935"}]}]},{"node":"KApply","label":"_Map_","variable":false,"arity":2,"args":[{"node":"KApply","label":"_|->_","variable":false,"arity":2,"args":[{"node":"KToken","sort":"Int","token":"33"},{"node":"KApply","label":"PUSH","variable":false,"arity":2,"args":[{"node":"KToken","sort":"Int","token":"32"},{"node":"KToken","sort":"Int","token":"115792089237316195423570985008687907853269984665640564039457584007913129639935"}]}]},{"node":"KApply","label":"_Map_","variable":false,"arity":2,"args":[{"node":"KApply","label":"_|->_","variable":false,"arity":2,"args":[{"node":"KToken","sort":"Int","token":"66"},{"node":"KApply","label":"ADD_EVM","variable":false,"arity":0,"args":[]}]},{"node":"KApply","label":"_Map_","variable":false,"arity":2,"args":[{"node":"KApply","label":"_|->_","variable":false,"arity":2,"args":[{"node":"KToken","sort":"Int","token":"67"},{"node":"KApply","label":"PUSH","variable":false,"arity":2,"args":[{"node":"KToken","sort":"Int","token":"1"},{"node":"KToken","sort":"Int","token":"0"}]}]},{"node":"KApply","label":"_|->_","variable":false,"arity":2,"args":[{"node":"KToken","sort":"Int","token":"69"},{"node":"KApply","label":"SSTORE_EVM","variable":false,"arity":0,"args":[]}]}]}]}]}]}'

test_map_json2 = r'{"node":"KApply","label":"_Map_","variable":false,"arity":2,"args":[{"node":"KApply","label":"_|->_","variable":false,"arity":2,"args":[{"node":"KToken","sort":"String","token":"\"coverage\""},{"node":"KApply","label":"_Set_","variable":false,"arity":2,"args":[{"node":"KApply","label":"SetItem","variable":false,"arity":1,"args":[{"node":"KToken","sort":"Int","token":"0"}]},{"node":"KApply","label":"_Set_","variable":false,"arity":2,"args":[{"node":"KApply","label":"SetItem","variable":false,"arity":1,"args":[{"node":"KToken","sort":"Int","token":"33"}]},{"node":"KApply","label":"_Set_","variable":false,"arity":2,"args":[{"node":"KApply","label":"SetItem","variable":false,"arity":1,"args":[{"node":"KToken","sort":"Int","token":"66"}]},{"node":"KApply","label":"_Set_","variable":false,"arity":2,"args":[{"node":"KApply","label":"SetItem","variable":false,"arity":1,"args":[{"node":"KToken","sort":"Int","token":"67"}]},{"node":"KApply","label":"SetItem","variable":false,"arity":1,"args":[{"node":"KToken","sort":"Int","token":"69"}]}]}]}]}]}]},{"node":"KApply","label":"_|->_","variable":false,"arity":2,"args":[{"node":"KToken","sort":"String","token":"\"currentProgram\""},{"node":"KApply","label":"_Map_","variable":false,"arity":2,"args":[{"node":"KApply","label":"_|->_","variable":false,"arity":2,"args":[{"node":"KToken","sort":"Int","token":"0"},{"node":"KApply","label":"PUSH","variable":false,"arity":2,"args":[{"node":"KToken","sort":"Int","token":"32"},{"node":"KToken","sort":"Int","token":"115792089237316195423570985008687907853269984665640564039457584007913129639935"}]}]},{"node":"KApply","label":"_Map_","variable":false,"arity":2,"args":[{"node":"KApply","label":"_|->_","variable":false,"arity":2,"args":[{"node":"KToken","sort":"Int","token":"33"},{"node":"KApply","label":"PUSH","variable":false,"arity":2,"args":[{"node":"KToken","sort":"Int","token":"32"},{"node":"KToken","sort":"Int","token":"115792089237316195423570985008687907853269984665640564039457584007913129639935"}]}]},{"node":"KApply","label":"_Map_","variable":false,"arity":2,"args":[{"node":"KApply","label":"_|->_","variable":false,"arity":2,"args":[{"node":"KToken","sort":"Int","token":"66"},{"node":"KApply","label":"ADD_EVM","variable":false,"arity":0,"args":[]}]},{"node":"KApply","label":"_Map_","variable":false,"arity":2,"args":[{"node":"KApply","label":"_|->_","variable":false,"arity":2,"args":[{"node":"KToken","sort":"Int","token":"67"},{"node":"KApply","label":"PUSH","variable":false,"arity":2,"args":[{"node":"KToken","sort":"Int","token":"1"},{"node":"KToken","sort":"Int","token":"0"}]}]},{"node":"KApply","label":"_|->_","variable":false,"arity":2,"args":[{"node":"KToken","sort":"Int","token":"69"},{"node":"KApply","label":"SSTORE_EVM","variable":false,"arity":0,"args":[]}]}]}]}]}]}]}]}'

def test_parse_kset():
    test_set = json.loads(test_set_json)
    print(parse_kset(test_set))

def test_parse_kmap():
    test_map = json.loads(test_map_json)
    print(parse_kmap(test_map).keys())

def test_parse_kmap2():
    test_map = json.loads(test_map_json2)
    print(parse_kmap(test_map).keys())

def test_parse_konfig():
    with open('testing-json-out.log') as koutput:
        koutput_dict = json.load(koutput)
        analysis_contents = get_analysis_cell_contents(koutput_dict)
        analysis_dict = parse_kmap(analysis_contents)
        print(parse_kset(analysis_dict['"coverage"']))
        print(list(parse_kmap(analysis_dict['"currentProgram"']).keys()))

def parse_kset(set_obj):
    setitem1 = set_obj['args'][0]['args'][0]['token']
    if set_obj['args'][1]['label'] == 'SetItem':
        setitem2 = set_obj['args'][1]['args'][0]['token']
        return [setitem1, setitem2]
    return [setitem1] + parse_kset(set_obj['args'][1])

def parse_kmap(map_obj):
    key1 = map_obj['args'][0]['args'][0]['token']
    value1 = map_obj['args'][0]['args'][1]
    cur_dict = {}
    cur_dict[key1] = value1
    if map_obj['args'][1]['label'] == '_|->_':
        key2 = map_obj['args'][1]['args'][0]['token']
        value2 = map_obj['args'][1]['args'][1]
        cur_dict[key2] = value2
        return cur_dict
    return {**cur_dict, **parse_kmap(map_obj['args'][1])}

def get_analysis_cell_contents(konfig_obj):
    return [x['args'][0]
            for x in konfig_obj['term']['args']
            if x['label'] == '<analysis>'][0]
