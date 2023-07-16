# Serialization: using the json.dumps() which returns a json file-like object
import json

# create a python dictionary
data = {
        "Name": "Romy",
        "Gender": "Female"
}
print("_________________________")
with open("data.json", mode='w') as file:
        json.dump(data, file)           # code serializes the  data  dictionary into JSON format
                                        # and writes it to a file named "data.json". 

print("Before deserialization: {}".format(type(data)))
# read the generated data.json file
with open ("data.json", mode="r") as file:
        json_data = file.read()
print("_________________________")
#Process the JSON data as a string
data = json.loads(json_data)

print("After serialization: {}".format(type(json_data)))
# Access the data
print(data)
print("_________________________")