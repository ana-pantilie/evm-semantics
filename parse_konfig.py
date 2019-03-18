import json

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
