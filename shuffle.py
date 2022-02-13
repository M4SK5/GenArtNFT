import os, random
import json

# Expects full json corresponding to image files. And image files with name <Index>_<TRAITS_UUID>.png

IMAGES_DIR = r"/mnt/c/Users/rings/Desktop/Assets/output/"
JSON_IN_FILE = r"/mnt/c/Users/rings/Desktop/Assets/output/tokens_md_ord.json"
JSON_OBJ_NAME = "Genesys_1024_Mumbai"
BASE_URL = "http://M4sk5.art/" + JSON_OBJ_NAME + "/"
TNAME_PREF = '#'
TDESC_PREF = '#'
JSON_OUT_FILE = "tokens_md_shuff.json"

def getFilenameWithNewIndex(old_url, new_index):
    uuid_and_ext_no_index = old_url.split('/').pop().split('_',1).pop()
    return str(new_index) + "_" + uuid_and_ext_no_index

#"Main" starts here.
os.chdir(IMAGES_DIR)
with open(JSON_IN_FILE, 'r') as input:
        md_json = json.load(input)[JSON_OBJ_NAME]

shuffled_list = []
for token_md in md_json:
    shuffled_list.append(token_md)

random.shuffle(shuffled_list)

#change token-id, name, description, image url and image file name (retain orig uuid).
#assume json ordered by token-id starting at 0
for i in range(len(shuffled_list)):
    #Retain original token id and image filename
    orig_tid = str(shuffled_list[i]["token-id"])
    orig_fn = shuffled_list[i]["image"].split('/').pop()


    shuffled_list[i]["token-id"] = i
    shuffled_list[i]["name"] = shuffled_list[i]["name"].replace( TNAME_PREF + orig_tid, TNAME_PREF + str(i))
    shuffled_list[i]["description"] = shuffled_list[i]["description"].replace(TDESC_PREF + orig_tid, TDESC_PREF + str(i))
    #change image url and file name (retain orig uuid).
    newfn = getFilenameWithNewIndex(shuffled_list[i]["image"], i)
    shuffled_list[i]["image"] = BASE_URL + newfn
    os.rename(orig_fn,newfn)

#Dump to json file
tokens_md_obj = {JSON_OBJ_NAME: shuffled_list}
with open(JSON_OUT_FILE, 'w') as outfile:
    json.dump(tokens_md_obj, outfile, indent=4)


