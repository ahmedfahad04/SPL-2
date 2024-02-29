import json
import os

with open("Resources\m_set3\image_data.json", "r") as json_file:
    image_tag_dict = json.load(json_file)
    
    # ? update the keys of image_tag_dict to remove set6/ from the value
    image_tag_dict = {key.replace("{}/".format(3), ""): value for key, value in image_tag_dict.items()}
    print("DICT: ", image_tag_dict)
    
    test_labels = [value for key, value in image_tag_dict.items() if "creation" not in key]
        
print("LABELS>>: ", test_labels)

        # # include only those values that are images
        # image_tag_dict = {key[2:]: value for key, value in image_tag_dict.items() if key[2:] in images}

        # # fill the image tags
        # image_tags = list(image_tag_dict.values())