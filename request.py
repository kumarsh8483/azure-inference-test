# python client for sending nnunet inference requests to online/local endpoints

import requests
import json
import base64
import os

# You can change below variables w.r.t you input & output directory paths : 
#   Prostate task has modularity of 2, 
#   so two files for inference should be added in inputs
inputs_dir = "./request_inputs"
outputs_dir = "./request_outputs" # prediction results will be saved to outputs dir
endpoint = 'http://127.0.0.1:5001/score' # check from azure endpoints tab
# Variables end here

input_files = {}
open_files = []

for fname in os.listdir(inputs_dir):
    f = open(os.path.join(inputs_dir, fname), 'rb')
    open_files.append(f)
    input_files[fname]=f
    
r = requests.post(endpoint, files=input_files)   

for f in open_files:
    f.close()

data = json.loads(r.text)

for fname, content in data['result_files'].items():
    # convert string to bytes
    binary = base64.b64decode(content.encode("utf-8"))
    # write bytes to a file 
    with open(os.path.join(outputs_dir, fname), "wb") as f:
        f.write(binary)
        
print(f"Inference finished, check {outputs_dir} for outputs")
