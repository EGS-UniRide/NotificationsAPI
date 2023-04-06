# EmailAPI
EmailAPI

# Install
```
$ pip install fastapi-mail
```

# How to run

Create Virtual Environment and Install Dependencies
```
python3 -m venv venv
source venv/bin/activate

pip install fastapi fastapi_mail
pip install uvicorn[standard]
```
While in the API directory type in the terminal `$ uvicorn EmailSenderAPI:app --reload` to launch the API.
