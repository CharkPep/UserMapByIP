import folium
import requests
import json
import time
#56973b4e2b66415b8bad6f7312fe4d40
def get_city(ip_address):
    # Your API key, available from your account page
    YOUR_GEOLOCATION_KEY = '56973b4e2b66415b8bad6f7312fe4d40'
    response = requests.get('https://ipgeolocation.abstractapi.com/v1/?api_key=' + YOUR_GEOLOCATION_KEY + '&ip_address=' + ip_address + "&fields=longitude,latitude")
    result = json.loads(response.content)
    print(result)
    if(result["longitude"] != "None" or result["longitude"] != "None"):
        return result
    else:
        return [0,0]
n = int(input())
ip = []
for i in range(0,n):
    ip.append(input())
#print(ip)
coordinates = []
for i in range(0,n):
    #print(get_city(ip[i]))
    tmp = get_city(ip[i])
    if(type(tmp["longitude"]) == type(float(1))):
        coordinates.append([tmp["longitude"], tmp["latitude"]])
    #print(type(tmp["longitude"]))
    time.sleep(1) 
print(coordinates)
m = folium.Map(location=[33.65, 49.0333], zoom_start=12)
for i in range(len(coordinates)):
    folium.Marker([float(coordinates[i][1]),float(coordinates[i][0])]).add_to(m)
#folium.Marker([coordinates[0][1], coordinates[0][0]]).add_to(m)
m.save("/Users/Roma/Desktop/map.html")