from csv import writer
import csv
import json
import hashlib
import pandas as pd 



data = []
with open("HNGi9 CSV FILE - Sheet1.csv", "r") as file:
    csv_reader = csv.DictReader(file)
    for rows in csv_reader:
        data.append(
        {"format": "CHIP-0007",
        "name": rows.get("Filename", ""),
        "description": rows.get("Description", "",),
        "minting_tool": rows.get("TEAM NAMES"),
        "sensitive_content": rows.get("sensitive_content", False),
        "series_number": rows.get("Series Number", ""),
        "series_total": "420",
        "attributes": rows.get("Attributes").split(";"),
            
        "UUID": rows.get("UUID", ""),

        "collection": {
                    "name": rows.get("name", ""),
                    "id": rows.get("UUID", "")
                    },
        })

NFT_data = {}
NFT_data["names"] = data
path = "HNGi9 file.json"
with open(path, "w") as jsonf:
    json.dump(NFT_data, jsonf, indent=4)

# with open("filename.output.csv", "w") as output:
#     writer = csv.writer(output)
#     writer.writerow("HNGi9 CSV FILE - Sheet1.csv")

df = pd.read_csv("HNGi9 CSV FILE - Sheet1.csv")
df.to_csv("filename.output.csv")

sha256_hash = hashlib.sha256()
with open(path, "rb") as json_file:
    for byte_block in iter(lambda: json_file.read(4096),b""):
        sha256_hash.update(byte_block)
        hashString = sha256_hash.hexdigest()
        with open("filename.output.csv", "a") as file:
            writer_object = writer(file)
            writer_object.writerow(hashString)
          


# Import writer class from csv module
# from csv import writer
# writer = csv.writer(file)
    # writer.writerow(data)
# List that we want to add as a new row
# List = [6, 'William', 5532, 1, 'UAE']

# Open our existing CSV file in append mode
# Create a file object for this file
# with open('event.csv', 'a') as f_object:

	# Pass this file object to csv.writer()
	# and get a writer object
	# writer_object = writer(f_object)

	# Pass the list as an argument into
	# the writerow()
	# writer_object.writerow(List)

	# Close the file object
	# f_object.close()




# filename = input("Enter the input file name: ")
# sha256_hash = hashlib.sha256()
# with open(filename,"rb") as f:
#     # Read and update hash string value in blocks of 4K
#     for byte_block in iter(lambda: f.read(4096),b""):
#         sha256_hash.update(byte_block)
#     print(sha256_hash.hexdigest())

# json_file = json.dumps(Chip_007, indent=4)
#             with open(f'json/{file_name}.json', 'w') as output:
#                 output.write(json_file)
#             output.close()
#             filename = f'json/{file_name}.json'
#             sha256_hash = hashlib.sha256()
#             with open(filename,"rb") as f:
#                 for byte_block in iter(lambda: f.read(4096),b""):
#                     sha256_hash.update(byte_block)
#             hashString = sha256_hash.hexdigest()
#             row.append(f'{hashString}')
#             writer.writerow(row)






# attr_pair = data["attributes"].split(";")
# hair = attr_pair[0]
            # hair_value = hair.split(":")[1].strip()
            # eyes = attr_pair[1]
            # eyes_value = eyes.split(":")[1].strip()
            # teeth = attr_pair[2]
            # teeth_value = teeth.split(":")[1].strip()
            # clothing = attr_pair[3]
            # clothing_value = clothing.split(":")[1].strip()
            # accesories = attr_pair[4]
            # accesories_value = accesories.split(":")[1].strip()
            # expression = attr_pair[5]
            # expression_value = expression.split(":")[1].strip()
            # strengths = attr_pair[6]
            # strengths_value = strengths.split(":")[1].strip()
            # try:
            #     weakness = attr_pair[7]
            #     weakness_value = weakness.split(":")[1].strip()
            # except IndexError:
            #     continue
            
            # def sample(trait_type,value):
            #     return {"trait_type":trait_type,"value":value}
            # attr = []
            # all = [["gender",gender],["hair",hair_value],["eyes",eyes_value],["teeth",teeth_value],["clothing",clothing_value],["accessories",accesories_value],["expression",expression_value],["strengths",strengths_value],["weakness",weakness_value]]
            # for item in all:
            #     if item[1] != "none": 
            #         attr.append(sample(item[0],item[1])),
 

# with open("HNGteam.json", "r") as json_file:
#     formatted_json =json.load(json_file)
#     for content in formatted_json:
#         content = hashlib.sha256(content).hexdigest() 
#         data.append(content)

# with open("hashed.csv" "w") as new_file:
#     json.dump(data, new_file, indent=4)
        
    





# {
#     "format": "CHIP-0007",
#     "name": "Pikachu",
#     "description": "Electric-type Pokémon with stretchy cheeks",
#     "minting_tool": "SuperMinter/2.5.2",
#     "sensitive_content": false,
#     "series_number": 22,
#     "series_total": 1000,
#     "attributes": [
#         {
#             "trait_type": "Species",
#             "value": "Mouse"
#         },
#         {
#             "trait_type": "Color",
#             "value": "Yellow"
#         },
#         {
#             "trait_type": "Friendship",
#             "value": 50,
#             "min_value": 0,
#             "max_value": 255
#         }
#     ],
#     "collection": {
#         "name": "Example Pokémon Collection",
#         "id": "e43fcfe6-1d5c-4d6e-82da-5de3aa8b3b57",
#         "attributes": [
#             {
#                 "type": "description",
#                 "value": "Example Pokémon Collection is the best Pokémon collection. Get yours today!"
#             },
#             {
#                 "type": "icon",
#                 "value": "https://examplepokemoncollection.com/image/icon.png"
#             },
#             {
#                 "type": "banner",
#                 "value": "https://examplepokemoncollection.com/image/banner.png"
#             },
#             {
#                 "type": "twitter",
#                 "value": "ExamplePokemonCollection"
#             },
#             {
#                 "type": "website",
#                 "value": "https://examplepokemoncollection.com/"
#             }
#         ]
#     },
#     "data": {
#         "example_data": "VGhpcyBpcyBhbiBleGFtcGxlIG9mIGRhdGEgdGhhdCB5b3UgbWlnaHQgd2FudCB0byBzdG9yZSBpbiB0aGUgZGF0YSBvYmplY3QuIE5GVCBhdHRyaWJ1dGVzIHdoaWNoIGFyZSBub3QgaHVtYW4gcmVhZGFibGUgc2hvdWxkIGJlIHBsYWNlZCB3aXRoaW4gdGhpcyBvYmplY3QsIGFuZCB0aGUgYXR0cmlidXRlcyBhcnJheSB1c2VkIG9ubHkgZm9yIGluZm9ybWF0aW9uIHdoaWNoIGlzIGludGVuZGVkIHRvIGJlIHJlYWQgYnkgdGhlIHVzZXIu"
#     }
# }
