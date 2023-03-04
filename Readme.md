- [Create a virtual environment](#create-a-virtual-environment)

```Powershell
python -m venv env
.\env\Scripts\activate
```

```bash
python3 -m venv env
```

Update pip install and install
```Powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

```bash
source env/bin/activate
pip3 install -r requirements.txt
```

- [Run the Flask app in local development](#run-locally)

```Powershell
flask run
```

```bash
export FLASK_APP=main.py
flask run
```

- [Deploy SCRAPYMike in Docker Ubuntu](#Deployment)

First check if the port is available
```bash
sudo nc localhost 5000 < /dev/null; echo $?
```

