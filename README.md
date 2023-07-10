# azure-inference-test
test-codes for azure nnunet pipeline inference

# how it works?
1. Clone this repository

       git clone https://github.com/tekmen0/azure-inference-test.git
   
3. Move to repository folder

       cd azure-inference-test
   
5. (Optional) Activate python virtual environment.
   
6. Install the inference test server
   
       python -m pip install azureml-inference-server-http
   
7. Move to server directory

       cd azure-inference-test

8. Start inference server

       azmlinfsrv --entry_script azure-inference-test/score.py

Now your scoring is deployed locally, running at 127.0.0.1:5001

You can send request to endpoint 127.0.0.1:5001/score for executing the 'run' function in score.py

Example request using python can be found in request.py, you may also want to use curl or postman
