import requests
from datetime import date
import zipfile
import redis
import csv
import json


def get_bahv_add_to_redis() -> None:
    redis_connection = redis.Redis(host='localhost', port=6379, db=0)
    current_date = date.today().strftime("%d%m%y")
    file_name = "EQ" + current_date + "_CSV.ZIP"
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        BSE_zip_file = requests.get(
            "https://www.bseindia.com/download/BhavCopy/Equity/" + file_name, headers=headers)
        open(file_name, "wb").write(BSE_zip_file.content)

        with zipfile.ZipFile(file_name, "r") as zip_ref:
            zip_ref.extractall(".")

        with open("EQ" + current_date+".CSV", encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data = json.dumps({"Code": row["SC_CODE"].rstrip(), "Name": row["SC_NAME"].rstrip(), "Open": row["OPEN"].rstrip(),
                                   "High": row["HIGH"].rstrip(), "Low": row["LOW"].rstrip(), "Close": row["CLOSE"].rstrip()})
                key = row["SC_NAME"].rstrip()
                redis_connection.set(key, data)
        print("Successfully parse and inserted BSE data for " + current_date)

    except requests.ConnectionError:
        print("Could not connect")
