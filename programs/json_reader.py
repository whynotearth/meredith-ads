import json

def read(filename):
    file = open(filename, 'r')
    content = file.read()
    file.close()
    return content

json_file = read("fake.json")

json_data = json.loads(json_file)

print(json_data["app_id"])
