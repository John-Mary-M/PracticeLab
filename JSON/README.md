### In this directory I explore and learn to work with JSON in python
JSON stands for Java Script Object Notation.
Its' soul purpose is to to translate/interchange format to maintain the structure of the data.
 It supports data structures like arrays and objects and JSON documents that are rapidly executed on the server. It is also a Language-Independent format that is derived from JavaScript. 

 ##### Serialization and Deserialization.
 ## Deserialization is the process of decoding the data that is in JSON format into native data type. In Python, deserialization decodes JSON data into a dictionary.

 loads() : to deserialize a JSON document to a Python object.
   json.loads() method can be used to parse a valid JSON string and convert it into a Python Dictionary. It is mainly used for deserializing native string, byte, or byte array which consists of JSON data into Python Dictionary.


 load() : to deserialize a JSON formatted stream ( which supports reading from a file) to a Python object.
 json.load() takes a file object and returns the json object. A JSON object contains data in the form of key/value pair. The keys are strings and the values are the JSON types. Keys and values are separated by a colon. Each entry (key/value pair) is separated by a comma.
   `json.load(file_object)`
   Argument : It takes file object as a parameter.
   Return : It return json object.

After deserializing data into a py dict then u can use all dictionary methods available in python to manipulate it

### Serialization: converting python objects to json
The  json  module in Python provides a  json.dumps()  function that allows you to serialize Python objects into JSON format. This can be achived by using the:
        json.dumps(): This function is used to serialize a Python object into a JSON formatted string.

        json.dump(): This function is used to serialize a Python object and write it directly to a file-like object. It writes the JSON representation of the object to the specified file or file-like object.