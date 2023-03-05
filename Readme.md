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

Check if the port is available
```bash
sudo nc localhost 5000 < /dev/null; echo $?
```

Start the server in docker
```bash
sudo bash start.sh
```
List of container status
```bash
sudo docker ps
```

Stop the server in docker
```bash
sudo docker stop container {CONTAINER_ID}
```

OPTION: push image onto Docker repositories
1. login in bash with docker account
2. tag image
3. push

```bash
sudo docker login
sudo docker tag {app} {username}/{repo-folder-name}
sudo docker push {username}/{repo-folder-name}
```
