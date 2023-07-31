

### go to directory
cd xxx

### install virtual env
python3 -m venv venv

### activate virtual env
source venv/bin/activate

### install required packages
pip install -r requirements.txt



### run app on local
python index.py

Go to http://127.0.0.1:3000/testing





### build docker
docker build -t data_refresh1 .

### run docker
docker run -p 3000:3000 data_refresh1

Go to http://127.0.0.1:3000/testing




