import json
import os
import uuid
from PIL import Image

# Works independandtly based on ordered trait lists and hierarchy of traits in main loop. 

#List trait key names
TR_NAME1 = "CATEGORY_NAME_1"
TR_NAME2 = "CATEGORY_NAME_2"
TR_NAME3 = "CATEGORY_NAME_3"
TR_NAME4 = "CATEGORY_NAME_4"
TR_NAME5 = "CATEGORY_NAME_5"
IMG_PARTS_PATH = "IMAGE_PART_FOLDERS_PARENT_PATH like /home/parts/"

JSON_OBJ_NAME = "Object name in the json - the collection's name"
IMG_BASE_URL = "Base URL for where the nft collection's images are stored www.imageserver.com/ "
TNAME = "Token Name in json"
TDESC = "Token description in json"
IMG_EXT = "image file extentions"


OUTPUT_PATH = "Output path for images and json file."
JSON_OUTPUT_FILE = OUTPUT_PATH + "tokens_md_ord.json"



#lists of image parts files for each trait, and for each their respective trait names
#Change trait name and file names as needed.

TRAIT1_DATA = [
  (IMG_PARTS_PATH + "T1Folder/trait1.png", "Trait 1.1 name."),
  (IMG_PARTS_PATH + "T1Folder/trait2.png", "Trait 1.2 name."),
  (IMG_PARTS_PATH + "T1Folder/trait3.png", "Trait 1.3 name.")
]

TRAIT2_DATA = [
  (IMG_PARTS_PATH + "T2Folder/trait1.png", "Trait 2.1 name."),
  (IMG_PARTS_PATH + "T2Folder/trait2.png", "Trait 2.2 name."),
  (IMG_PARTS_PATH + "T2Folder/trait3.png", "Trait 2.3 name.")
]

TRAIT3_DATA = [
  (IMG_PARTS_PATH + "T3Folder/trait1.png", "Trait 3.1 name."),
  (IMG_PARTS_PATH + "T3Folder/trait2.png", "Trait 3.2 name."),
  (IMG_PARTS_PATH + "T3Folder/trait3.png", "Trait 3.3 name.")
]

TRAIT4_DATA = [
  (IMG_PARTS_PATH + "T4Folder/trait1.png", "Trait 4.1 name."),
  (IMG_PARTS_PATH + "T4Folder/trait2.png", "Trait 4.2 name."),
  (IMG_PARTS_PATH + "T4Folder/trait3.png", "Trait 4.3 name.")
]

TRAIT5_DATA = [
  (IMG_PARTS_PATH + "T5Folder/trait1.png", "Trait 5.1 name."),
  (IMG_PARTS_PATH + "T5Folder/trait2.png", "Trait 5.2 name."),
  (IMG_PARTS_PATH + "T5Folder/trait3.png", "Trait 5.3 name.")
]


tokens_md = [] #List of tokens metadata as json objects
i=0
for t1_tuple in TRAIT1_DATA:
    for t2_tuple in TRAIT2_DATA:
        for t3_tuple in TRAIT3_DATA:
            for t4_tuple in TRAIT4_DATA:
                for t5_tuple in TRAIT5_DATA:
                    #Generate uuid for image file name and image url based on trait names (in the second position of our data tuple lists).
                    token_uid_by_trait = uuid.uuid5(uuid.NAMESPACE_DNS, t1_tuple[1] + t2_tuple[1] + t3_tuple[1] + t4_tuple[1] + t5_tuple[1]).hex
                    imgFileName = str(i) + '_' + str(token_uid_by_trait) + IMG_EXT
                    
                    #Create token metadata
                    token_traits = {
                        "token-id": i,
                        "image": IMG_BASE_URL + imgFileName,
                        "name": TNAME + str(i),
                        "description": TDESC + str(i),
                        "attributes": []
                    }
                    token_traits["attributes"].append({"trait_type": TR_NAME1, "value": t1_tuple[1]})
                    token_traits["attributes"].append({"trait_type": TR_NAME2, "value": t2_tuple[1]})
                    token_traits["attributes"].append({"trait_type": TR_NAME3, "value": t3_tuple[1]})
                    token_traits["attributes"].append({"trait_type": TR_NAME4, "value": t4_tuple[1]})
                    token_traits["attributes"].append({"trait_type": TR_NAME5, "value": t5_tuple[1]})
                    
                    #Add the metadata to list.
                    tokens_md.append(token_traits)
                    
                    #Open and combine image part files (in the first position of our data tuple lists).
                    #Order of layer combination doesn't matter if image parts don't overlap.
                    c12 = Image.alpha_composite(Image.open(t1_tuple[0]).convert("RGBA"), Image.open(t2_tuple[0]).convert("RGBA"))
                    c123 = Image.alpha_composite(c12, Image.open(t3_tuple[0]).convert("RGBA"))
                    c1234 = Image.alpha_composite(c123, Image.open(t4_tuple[0]).convert("RGBA"))
                    finished = Image.alpha_composite(c1234, Image.open(t5_tuple[0]).convert("RGBA"))
                    
                    #Save image file and increment token id.
                    finished.save(OUTPUT_PATH + imgFileName)
                    i=i+1

#Dump to json file
tokens_md_obj = {JSON_OBJ_NAME: tokens_md}
with open(JSON_OUTPUT_FILE, 'w') as outfile:
    json.dump(tokens_md_obj, outfile, indent=4)
