FROM python:slim

WORKDIR /src/vci

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT [ "python", "./application.py" ]
