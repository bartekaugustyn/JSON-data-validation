# JSON validation project

## 1 Purpose
The goal of the project is to validate a JSON format file in a way that is compliant with [`AWS::IAM::Role Policy`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-role-policy.html).

In the task, the emphasis was on verifying the content of the *`Resource`* field and base on that in case it contained a single asterisk (*), the validation function should return a logical **False** value and in any other case a logical **True** value.

## 2 Setup

### Clone the Repository [JSON-data-validation](https://github.com/bartekaugustyn/JSON-data-validation)
```bash
git clone https://github.com/bartekaugustyn/JSON-data-validation.git
```
### Application launching
Script that verifies the contents of a field Resource
```bash
python json_validator.py
```
Additional unit tests for function is script sample_file.py
```bash
python unit_tests.py
```

## 3 Prepared Files 
- validation_schema.json
- sample_file.json
- json_validator.py
- unit_tests.py

## 4 Detailed Files Description

- The `validation_schema.json` file contains a validation scheme prepared according to the structure of the json file under examination. It does not have any set required parameters due to the task foundation.

- The `json_validator.py` file contains a python code with function that verifies the contents of the *`Resource`* field of the `sample_file.json` with the prepared schema, then validates the file using the validate function from the jsonschema library and validationerror from jsonschema.exceptions.

- The `unit_tests.py` file contains additional application of unit tests for the function from the `json_validator.py` file. **Test** verifying its compliance with the schema, skipping the resource field. **Test** with case assuming a invalid file and **test** with use of an empty file. 
In addition, the unittest library wes used.

