from csv import writer
from csv import reader
import csv
import json
import hashlib

json_path = "HNGi9 file.json"
input_path = "HNGi9 CSV FILE - Sheet1.csv"
sha256_hash = hashlib.sha256()

data = []
with open(input_path, "r") as file:
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

with open(json_path, "w") as jsonf:
    json.dump(NFT_data, jsonf, indent=4)


with open(json_path, "rb") as json_file:
    for byte_block in iter(lambda: json_file.read(4096),b""):
        sha256_hash.update(byte_block)
        hashString = sha256_hash.hexdigest()
        with open(input_path, "r") as read_obj, \
            open("filename.output.csv", "w", newline="") as write_obj:
            csv_reader = reader(read_obj)
            next(csv_reader)
            csv_writer = writer(write_obj)
            for row in csv_reader:
                row.append(hashString)
                csv_writer.writerow(row)
