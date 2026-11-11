import json
def generate_output(file_name, file_type, statistics, content):
    output = {'file_name' : file_name,
              'file_type' : file_type,
              'statistics' : statistics,
              'content' : content}
    json_output = json.dumps(output, indent=4)
    return json_output