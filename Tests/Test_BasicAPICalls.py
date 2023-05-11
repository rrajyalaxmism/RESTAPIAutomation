import requests
import json

URL = "https://todo.pixegami.io"
def test_GET():
    response=requests.get(URL)
    Status_Code=response.status_code
    assert Status_Code==200

def test_PUT():
    json_file = open("../TestData/PUT_Payload.json","r").read()
    payload = json.loads(json_file)

    response = requests.put(URL+"/create-task",json= payload)
    Status_Code = response.status_code
    assert Status_Code == 200

    data=response.json()
    task_id= data["task"]["task_id"]
    endpt= f"/get-task/{task_id}"
    response = requests.get(URL + endpt)
    Status_Code = response.status_code
    assert Status_Code == 200
