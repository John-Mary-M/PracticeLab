# Serialization: using the json.dumps() which returns a jsn str
import json

# create a python dictionary
data = {
        "Name": "Romy",
        "Gender": "Female"
}
print("Before serialization: {}".format(type(data)))
print("_________________________")
# serialize the py dict to json
json_data = json.dumps(data)

# print the serialized JSON data
print(json_data)
print("After serialization: {}".format(type(json_data)))
print("_________________________")