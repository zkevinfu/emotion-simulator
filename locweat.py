import requests
import Queue
import json

def get_loc():
    loc_url = 'http://freegeoip.net/json'
    r = requests.get(loc_url)
    j = json.loads(r.text)
    return (j['latitude'], j['longitude'])

def get_weat():
    ds_url_base = 'https://api.darksky.net/forecast'
    ds_api_key = '12caf1dbd09b0e555c8b4a27339abb75'
    exclude = '?exclude=minutely,hourly,daily,flags,alerts'
    lat_lon = get_loc()
    latitude, longitude = lat_lon[0], lat_lon[1]
    ds_request = '%s/%s/%s,%s%s'%(ds_url_base, ds_api_key,latitude,longitude,exclude)
    ds_r = requests.get(ds_request)
    ds_j = json.loads(ds_r.text)
    return ds_j['currently']

def get_stim():
    ds_j = get_weat()
    weat = ds_j['icon']
    temp = ds_j['temperature']

    clear = ['clear-day', 'clear-night', 'wind']
    p_cloudy = ['partly-cloudy-day', 'partly-cloudy-night']
    cloudy = ['cloudy', 'fog']
    rain = ['rain', 'sleet']
    snow = ['snow']

    e_queue = Queue.Queue()
    #TODO make this good
    if (any(weat == icon for icon in clear)):
        e_queue.put(('joy', 1))
    elif (any(weat == icon for icon in p_cloudy)):
        e_queue.put(('sadness', 1))
    elif (any(weat == icon for icon in cloudy)):
        e_queue.put(('sadness', 1.5))
    elif (any(weat == icon for icon in rain)):
        e_queue.put(('sadness', 1.5))
    elif (any(weat == icon for icon in snow)):
        e_queue.put(('joy', 1))

    if 40 <= temp <= 80
        e_queue.put(('joy', 1))
    elif temp < 40
        e_queue.put(('sadness', 1.5))
    elif temp > 80
        e_queue.put(('anger', 1.5))

    return e_queue
