# Deserialization: Example uses the load() function which is used to parse file 
# objects and convert them to python dictionary type
import json

# create json data as a string
data = '{"Name" : "Romy", "Gender" : "Female"}'

print("Datatype before deserialization : "
      + str(type(data)))

# deserializing the data
data = json.loads(data)
 
#print out data in key: Value format
for key, value in data.items():         # items() from the dictionary data type because data at this point is a dictionary
        print(key + ": " + value)

print("Datatype after deserialization : "
      + str(type(data)))