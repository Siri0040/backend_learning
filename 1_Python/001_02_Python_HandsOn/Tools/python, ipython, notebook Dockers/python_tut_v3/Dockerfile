FROM python:2.7.15

WORKDIR /usr/src/app

RUN pip install --upgrade setuptools pip
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY notebook.sh ./

RUN chmod +x notebook.sh

EXPOSE 8888

CMD [ "./notebook.sh"]
