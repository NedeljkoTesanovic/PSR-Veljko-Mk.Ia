import requests #used for communication over http
import shutil, json, time   


#gets a list of all of the content on the sd card
#in the JSON format, and processes the data to get the name of the latest taken photo
def getLatestPictureName():
    r = requests.get('http://10.5.5.9:8080/gp/gpMediaList')
    data = r.json()

    index_of_latest = 0
    value_of_latest = 0

    for index,x in enumerate(data['media'][0]['fs']):
        if x['n'][:4] == "GOPR" :
            if int(x['n'][4:8]) > value_of_latest:
                value_of_latest = int(x['n'][4:8])
                index_of_latest = index

    picture = data['media'][0]['fs'][index_of_latest]['n']
    return picture


#sends commands over http to the camera server
def takePicture():
    r = requests.get('http://10.5.5.9/camera/CM?t=goprohero&p=%01') #changes the mode of the camera to photo mode
    time.sleep(2)   #sleeps for 2 seconds, in order to allow the processing of the command on the side of the camera
    
    p = requests.get('http://10.5.5.9/bacpac/SH?t=goprohero&p=%01') #activates the shutter, thus taking a picture
    time.sleep(2)

    #checks whether either of the http requests failed, code 200 denotes successful completion
    if p.status_code != 200 or r.status_code != 200:
        print("ERROR, http request failed!")

#takes a picture name as a parameter, then downloads said picture saving it in the desired directory
def downloadPicture(picture_name):
    url = 'http://10.5.5.9:8080/videos/DCIM/100GOPRO/' + picture_name
    response = requests.get(url, stream=True)
    
    path = "C:\\Users\\nedel\\Desktop\\PSR 'Veljko' Mk.Ia\\Files\\Pictures\\AcquisitionedPhotos\\" + picture_name
    
    with open(path, 'wb') as out_file: #both the directory and the file name can be changed
        shutil.copyfileobj(response.raw, out_file)
    del response

#function calls all the other functions, allowing for simpler execution
def executeCamera():
    takePicture()
    picture = getLatestPictureName()
    downloadPicture(picture)
    return str( "C:\\Users\\nedel\\Desktop\\PSR 'Veljko' Mk.Ia\\Files\\Pictures\\AcquisitionedPhotos\\" + picture)

executeCamera()
