# test script to test the flask api
# uncomment the data list to first create the video objects
# you can then try to get a video by specific id
# you can as well put a new video into the database
# you can as well delete a specific video id
import requests

BASE = " http://127.0.0.1:5000/"
# uncomment from line 10 to 19
# this list of dictionaries creates 3 videos with id 0,1 and 2
data = [ {"likes":1560, "name":"How to cook", "views":10000} ,
        {"likes":15000, "name":"How to create a REST API", "views":200000} ,
        {"likes":12000, "name":"Recipe for weight loss", "views":44000},
       {"likes":120, "name":"This is a new video", "views":440} # uncomment this to test adding of new videos
       

]

for i in range (len(data)):
    response = requests.put(BASE + "video/" + str(i) , data[i])
    print(response.json())

response = requests.get(BASE + "videos")
print(response.json())
# test added video
# response = requests.get(BASE + "video/3")
# print(response.json())
# test delete by uncommenting code below
# response= requests.delete(BASE + "video/2")
# print(response)

