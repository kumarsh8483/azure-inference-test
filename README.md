# azure-inference-test
test-codes for azure nnunet pipeline inference

## how it works?

### Deployment with docker file :

1. Build dockerfile

       docker build -t nnunet_local_inference_env .

2. Run dockerfile

       docker run -v $(pwd):/app nnunet_local_inference_env

Note : If you are running from docker dekstop, don't forget to mount project root directory to /app directory

### Deployment with bare python environment :

Quick note : Workflow tested with python 3.10.6

1. Clone this repository

       git clone https://github.com/tekmen0/azure-inference-test.git
   
3. Move to repository folder

       cd azure-inference-test
   
5. (Optional) Activate python virtual environment.
   
6. Install the inference test server
   
       python -m pip install azureml-inference-server-http

7. Install requirements.

       pip3 install requirements.txt 
   
8. Move to server directory

       cd server

9. Start inference server

       azmlinfsrv --entry_script score.py

Now your scoring is deployed locally, running at 127.0.0.1:5001

You can send request to endpoint 127.0.0.1:5001/score for executing the 'run' function in score.py

Example request using python can be found in request.py, you may also want to use curl or postman
