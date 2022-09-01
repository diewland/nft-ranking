import os, sys, json, glob
from pprint import pprint as pp

# launchpad
LP_QUIXOTIC = 'quixotic'
LP_SPEEDBOAT = 'speedboat'

# config
SEP         = '|'
F_TOKEN     = '_token_id'
F_NAME      = '_name'
F_RANK      = '_rank'
F_SCORE     = '_score'
F_URL       = '_link'
F_MOVEMENT  = '📈'
ICO_UP      = '🟢'
ICO_DOWN    = '🔴'
ICO_SAME    = '🔵'
ICO_NEW     = '🟡'
CSV_FIELDS  = [
    F_RANK,
    #F_TOKEN,
    F_NAME,
    F_SCORE,
    F_URL,
    #..ATTRS
]
DEFAULT_VALUE = '-'

# detect compare_path
compare_path = None
compare_data = {}
if len(sys.argv) > 1:
    compare_path = sys.argv[1]
if compare_path != None:
    # inject movement field
    CSV_FIELDS[1:1] = [ F_MOVEMENT ]
    # prepare compare data
    c_file = open(compare_path, mode='r')
    c_lines = [ l.strip() for l in c_file.readlines() ]
    c_lines.pop(0) # rm header
    c_file.close()
    for l in c_lines:
        c_data = l.split(SEP)
        c_rank = int(c_data[0])
        try: # same format
            c_token_id = int(c_data[2].split('#')[1])
        except: # convert
            c_token_id = int(c_data[1].split('#')[1])
        compare_data[c_token_id] = c_rank

def rank(URL, ATTRS, launchpad=LP_QUIXOTIC):
    # prepare filename
    ll = []
    if launchpad == LP_SPEEDBOAT:
        ll = filter(lambda x: x.isnumeric(), os.listdir('json'))
        ll = sorted([ int(x) for x in ll ])
    else: # default: quixotic
        ll = filter(lambda x: x.endswith('.json'), os.listdir('json'))
        ll = sorted([ int(x.split('.')[0]) for x in ll ])

    # init items
    items = []
    attr_score = [{} for x in range(len(ATTRS))]

    # make attr mapping
    attr_mapping = {}
    for idx, attr in enumerate(ATTRS):
        attr_mapping[attr] = idx

    # fill basic attributes
    for token_id in ll:
        data = None
        if launchpad == LP_SPEEDBOAT:
            data = json.load(open('./json/%s' % token_id))
        else: # default: quixotic
            data = json.load(open('./json/%s.json' % token_id))
        name = data['name']
        attr = data['attributes']
        ftt = attr[0]['trait_type']
        # build item
        item = {}
        item[F_TOKEN] = token_id
        item[F_NAME] = name
        if URL.find("{}") > -1:
            item[F_URL] = URL.format(token_id)
        else:
            item[F_URL] = '%s/%s' % (URL, token_id)
        item[F_SCORE] = None
        for trait in attr:
            key = trait['trait_type']
            v = trait['value']
            idx = attr_mapping[key]
            item[key] = v
            # collect attr stat
            if attr_score[idx].get(v) is None:
                attr_score[idx][v] = 1
            else:
                attr_score[idx][v] += 1

        # add to list
        items.append(item)

    # calc score
    item_size = len(items)
    for item in items:
        # skip UR, unreveal
        if item[F_SCORE] is not None:
            continue
        # calc score from attributes
        score = 0
        for key in ATTRS:
            attr = item.get(key)
            if attr is None:
                continue
            idx = attr_mapping[key]
            div = attr_score[idx][attr]
            score += item_size / div
        item[F_SCORE] = score

    # calc ranking
    prev_score = 0
    prev_rank = 0
    items.sort(key=lambda it: it[F_SCORE], reverse=True)
    for idx, item in enumerate(items):
        cur_score = item[F_SCORE]
        # next rank
        if cur_score != prev_score:
            cur_rank = idx + 1
            prev_score = cur_score
            prev_rank = cur_rank
        # update rank
        item[F_RANK] = cur_rank
        # update movement
        if compare_path != None:
            movement = ICO_NEW
            token_id = item[F_TOKEN]
            prev_rank = compare_data.get(token_id)
            if prev_rank is None:
                pass
            elif cur_rank < prev_rank:
                movement = '%s+%s' % (ICO_UP, prev_rank-cur_rank)
            elif cur_rank > prev_rank:
                movement = '%s-%s' % (ICO_DOWN, cur_rank-prev_rank)
            elif cur_rank == prev_rank:
                movement = ICO_SAME
            else:
                raise Exception('invalid data (%s, %s)' % (prev_rank, cur_rank))
            item[F_MOVEMENT] = movement

    # print csv
    print(SEP.join(CSV_FIELDS))
    for item in items:
        row = [ item.get(k) or '' for k in CSV_FIELDS ]
        row = [ str(r) for r in row  ]
        print(SEP.join(row))

def rank2(URL, launchpad=LP_QUIXOTIC):
    # resolve all traits
    tt = []
    for f in glob.glob("json/*"):
        try:
            data = json.load(open(f))
            for t in data['attributes']:
                tt += [ str(t['trait_type']) ]
        except:
            print("skip {}".format(f))
    tt = list(set(tt))

    # update csv fields
    global CSV_FIELDS
    CSV_FIELDS += tt

    # calculate rank
    rank(URL, tt, launchpad)
