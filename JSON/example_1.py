# Deserialization: Example uses the load() function which is used to parse file 
# objects and convert them to python dictionary type
import json

# create json data as a string
data = '{"Name" : "Romy", "Gender" : "Female"}'

print("Datatype before deserialization : "
      + str(type(data)))

# deserializing the data
data = json.loads(data)
 
#print out data
for k, v in data:
        print(k, v)

print("Datatype after deserialization : "
      + str(type(data)))