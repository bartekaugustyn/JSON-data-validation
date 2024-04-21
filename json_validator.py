import json
from jsonschema import validate
from jsonschema.exceptions import ValidationError

def file_validation(file):
    try:
        for key, value in file.items():
            if key != 'PolicyDocument':
                continue 
            else:
                for k,v in value.items():
                    if k != 'Statement':
                        pass
                    else:
                        for q,a in v[0].items():
                            if q == 'Resource':
                                if a == '*':
                                    return False
                                else:
                                    return True
        validate(instance = file, schema = schema)
    except ValidationError as e:
        print("Validation error:", e)
        return False
        
with open("sample_file.json") as f:
    file = json.load(f)

with open("validation_schema.json") as f:
    schema = json.load(f)

is_valid = file_validation(file)
print("Is valid:", is_valid)




