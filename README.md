# FastApi
Small tutorial of FastApi with python

Install Python 3.6.1 or newer  
install virtualenv with pip install virtualenv  
clone this repository with git bash `git clone https://github.com/ricardodarocha/FastApi.git`  
access the virtual env and activate  
```bash
cd env/Scripts
activate
```
will appear an venv tag

```bash
>(venv)
```
## Ready to programming

Now you can install all dependencies and shows up the application server

```
pip install requirements
uvicorn main:app --reload
```
## Try the api in the browser

**localhost:8000/**  
**locahost:8000/docs**

## Try it again

If are you not using virtual env, you can install FastApi and Uvicorn by yourself
```
pip install FastApi
pip install uvicorn
```
Check the documentation
https://fastapi.tiangolo.com/
