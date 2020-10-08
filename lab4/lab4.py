import http.client as httplib
import time
from urllib.parse import urlencode
key = "Q8Q641YS7OO6EC83"  # MY own key l3-t-4a
lab_key = "AT68QYQ94MQEWXL3" # lab4key

items = ["L3-T-4", "rodrigofierro@cmail.carleton.ca", "A"]


def upload(i):
    while True:
        params = urlencode({'field1': i, 'key':lab_key })
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = httplib.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print(i)
            print(response.status, response.reason)
            conn.close()
            time.sleep(1)
        except:
            print ("connection failed")
        break


if __name__ == "__main__":
    for i in items:
        upload(i)
