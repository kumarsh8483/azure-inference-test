FROM python:3.10.8

WORKDIR /app

RUN pip3 install nnunet
RUN python3 -m pip install azureml-inference-server-http

COPY requirements.txt requirements.txt 
RUN pip3 install -r requirements.txt 

WORKDIR /app/server

ENTRYPOINT ["azmlinfsrv", "--entry_script", "score.py"]
