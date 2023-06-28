
## Note:
I am about 90% sure that a bug in Boto3 causes the image uploading to fail some of the time on vercel, but not locally. Both the local and vercel sites request to the same API.

## Running Locally

Instructions to run locally:
Note: this assumes you are running linux. I have no idea how windows works
1. clone the repo
```bash
git clone https://github.com/hump-day/front/
```
2. cd into the repo directory
```bash
cd front
```
3. install the requirements
  ```bash
python3 -m venv env
source env/bin/activate
python3 -m pip install -r requirements.txt
```
4. runserver
  ```bash
  python3 manage.py runserver
```
or
```bash
./manage.py runserver
```
