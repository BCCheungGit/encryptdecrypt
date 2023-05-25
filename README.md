# encryption decryption app
This program can encrypt and decrypt any message using fernel, a python library.

## Docker
This project also has a repository on DockerHub, but it is currently private and not for public use.

## Usage
1. Create python virtual env

```shell
pythom -m venv venv
```

2. Activate venv

```shell
source venv/Scripts/activate
```

3. Download requirements

```shell
pip install -r requirements.txt
```

4. Run in debug mode

```shell
python app.py
```

## ToDo
- [x] Beautify using bootstrap and css
- [x] add jinja template inheritance and flask functionality
- [ ] fix potential problems with having encrypt and decrypt on separate routes