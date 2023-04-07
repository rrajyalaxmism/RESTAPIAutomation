import requests

URL = "https://todo.pixegami.io"
def test_GET():
    response=requests.get(URL)
    Status_Code=response.status_code
    assert Status_Code==200

def test_PUT():
    payload={
              "content": "Put test",
              "user_id": "rrl",
              "is_done": False
            }
    response = requests.put(URL+"/create-task",json=payload)
    Status_Code = response.status_code
    assert Status_Code == 200

    data=response.json()
    task_id= data["task"]["task_id"]
    endpt= f"/get-task/{task_id}"
    response = requests.get(URL + endpt)
    Status_Code = response.status_code
    assert Status_Code == 200
