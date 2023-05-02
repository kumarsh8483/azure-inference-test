import requests
import json
import base64
import os

#parameters
inputs_dir = "inputs"
outputs_dir = "outputs"

input_files = {}
open_files = []

for fname in os.listdir(inputs_dir):
    f = open(os.path.join(inputs_dir, fname), 'rb')
    open_files.append(f)
    input_files[fname]=f
    
r = requests.post('https://nnunet-model-04131301522792.eastus2.inference.ml.azure.com/score', files=input_files)   

for f in open_files:
    f.close()

data = json.loads(r.text)
print(data)


for fname, content in data['result_files'].items():
    # convert string to bytes
    binary = base64.b64decode(content.encode("utf-8"))
    #write bytes to a file 
    with open(os.path.join(outputs_dir, fname), "wb") as f:
        f.write(binary)
