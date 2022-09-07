import json, glob
from collections import OrderedDict
from pprint import pprint as pp

FROM_ID = 1
TO_ID = 4998
INPUT_DIR = 'json_original'
OUTPUT_DIR = 'json'

# helper
def find_index(lst, key, value):
    for i, dic in enumerate(lst):
        if dic[key] == value:
            return i
    return -1

# main
for token_id in range(FROM_ID, TO_ID+1):
    path = "{}/{}".format(INPUT_DIR, token_id)
    path_out = "{}/{}".format(OUTPUT_DIR, token_id)

    # load json
    data = json.load(open(path), object_pairs_hook=OrderedDict)
    attrs = data['attributes']

    # get current type
    idx = find_index(attrs, 'trait_type', 'Type')
    if idx == -1:
        print(path)
        pp(data)
        raise Exception("ERROR: type not found")
    info = attrs[idx]
    typez = info['value']

    # clean up type
    new_type = typez.split(" (")[0]
    info["value"] = new_type

    # update engine
    data['compiler'] = "Jigsaw Engine"

    # debug 1
    print("ID#{} [{}] -> [{}]".format(token_id, typez, new_type))

    # debug 2
    #print("--> {}".format(path))
    #pp(data)

    # write to file
    with open(path_out, "w") as f:
        json.dump(data, f)
