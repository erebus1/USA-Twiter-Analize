import pickle
from TwitterAPI import TwitterAPI
from textblob import TextBlob
import time
import map

States_coord = {'Wisconsin': [-92.8893, 42.4919, -86.8052, 47.0808], 'Mississippi': [-91.6499, 30.1739, -88.0976, 34.9962], 'Oklahoma': [-103.0026, 33.6160, -94.4314, 37.0023], 'Delaware': [-75.7886, 38.4510, -75.0489, 39.8395],
                'Minnesota': [-97.2399, 43.4993, -89.4918, 49.3853],
                'Appalachia': [-89.7679, 32.4827, -73.9359, 43.0952], 'Illinois': [-91.5129, 36.9701, -87.4952, 42.5084],
                'Arkansas': [-94.6192, 33.0042, -89.6419, 36.4996], 'New Mexico': [-109.0502, 31.3321, -103.0020, 37.0002],
                'Indiana': [-88.0975, 37.7717, -84.7846, 41.7607], 'Maryland': [-79.4872, 37.9120, -75.0492, 39.7231], 'Louisiana': [-94.0434, 28.9287, -88.8165, 33.0197], 'Texas': [-106.6460, 25.8371, -93.5083, 36.5007],
                'Wyoming': [-111.0563, 40.9946, -104.0518, 45.0060], 'Tennessee': [-90.3105, 34.9832, -81.6469, 36.6783], 'Arizona': [-114.8164, 31.332, -109.045, 37.0037], 'Iowa': [-96.6394, 40.3755, -90.1404, 43.5010],
                'Michigan': [-90.4185, 41.696, -82.4184, 48.191], 'Kansas': [-102.0518, 36.9929, -94.5886, 40.0033],
                'Utah': [-114.0531, 36.9978, -109.0415, 42.0017], 'Virginia': [-83.6752, 36.5408, -75.2418, 39.4659], 'Oregon': [-124.5664, 41.9920, -116.4633, 46.2938], 'Connecticut': [-73.7279, 40.9805, -71.7872, 42.0504],
                'Montana': [-116.0496, 44.3579, -104.0395, 49.0011],
                'California': [-124.4096, 32.5343, -114.1308, 42.0095], 'Idaho': [-117.2431, 41.9880, -111.0434, 49.0009], 'West Virginia': [ 	-82.6444, 37.2017, -77.7189, 40.6378],
                'South Carolina': [-83.3539, 32.0374, -78.5409, 35.2155], 'New Hampshire': [-72.5573, 42.6971, -70.7086, 45.3053], 'Massachusetts': [ 	-73.5081, 41.2381, -69.9282, 42.8868], 'Vermont': [-73.4382, 42.7268, -71.4651, 45.0165],
                'Georgia': [-85.6052, 30.3556, -80.8407, 35.0009], 'North Dakota': [-104.0489, 45.9350, -96.5548, 49.0007], 'Pennsylvania': [-80.5195, 39.7199, -74.6896, 42.2695],
                'Florida': [-87.6348, 24.521, -80.0307, 31.001], 'Alaska': [-179.1506, 51.2097, -129.9795, 71.441],
                'Kentucky': [-89.4168, 36.4968, -81.9650, 39.1481], 'Hawaii': [-160.2471, 18.9117, -154.8066, 22.2356], 'Nebraska': [-104.0537, 39.9999, -95.3082, 43.0017], 'Missouri': [-95.7744, 35.9042, -89.0987, 40.6136],
                'Ohio': [-84.8202, 38.4031, -80.5187, 41.9775], 'Alabama': [-88.4731, 30.2208, -84.8884, 35.0079],
                'Rhode Island': [-71.8865, 41.1461, -71.1207, 42.0191], 'South Dakota': [-104.0577, 42.4796, -96.4364, 45.9455], 'Colorado': [-109.0604, 36.9923, -102.0415, 41.0035],
                'New Jersey': [ 	-75.5598, 38.9289, -73.8937, 41.3576], 'Washington': [-124.7494, 45.5437, -116.9161, 49.0049], 'North Carolina': [-83.3539, 32.0374, -78.5409, 35.2155],
                'East Coast': [-87.6349, 24.521, -66.9326, 47.4598], 'New York': [-79.762, 40.496, -71.8562, 45.0128],
                'Nevada': [-120.0058, 35.0023, -114.0394, 42.0018], 'Maine': [-71.0843, 43.0648, -66.9406, 47.4598]}
States = {}
States_ok = {'Mississippi': 0.0, 'Oklahoma': 0.0, 'Delaware': 0.0, 'Minnesota': 0.0, 'Illinois': 0.0, 'Arkansas': 0.0,
             'New Mexico': 0.0, 'Indiana': 0.0, 'Louisiana': 0.0, 'Texas': 0.0, 'Wisconsin': 0.0, 'Kansas': 0.0,
             'Connecticut': 0.0, 'California': 0.0, 'West Virginia': 0.0, 'Georgia': 0.0, 'North Dakota': 0.0,
             'Pennsylvania': 0.0, 'Alaska': 0.0, 'Missouri': 0.0, 'South Dakota': 0.0, 'Colorado': 0.0,
             'New Jersey': 0.0, 'Washington': 0.0, 'New York': 0.0, 'Nevada': 0.0, 'Maryland': 0.0, 'Idaho': 0.0,
             'Wyoming': 0.0, 'Arizona': 0.0, 'Iowa': 0.0, 'Michigan': 0.0, 'Utah': 0.0, 'Virginia': 0.0, 'Oregon': 0.0,
             'Montana': 0.0, 'New Hampshire': 0.0, 'Massachusetts': 0.0, 'South Carolina': 0.0, 'Vermont': 0.0,
             'Florida': 0.0, 'Hawaii': 0.0, 'Kentucky': 0.0, 'Rhode Island': 0.0, 'Nebraska': 0.0, 'Ohio': 0.0,
             'Alabama': 0.0, 'North Carolina': 0.0, 'Tennessee': 0.0, 'Maine': 0.0}


def registerApi():
    api = TwitterAPI("BGMUpePgUoFU13l3NOd26DVUD",
                     "pmiwqlftwhj6tPEDBzRrxvObSw3E8Kt29PIUo0XjGW60jtpOZO",
                     "2719912512-l6a59JAHMpbs8s5t72BHLJqL19sCvUluBw9Ewhh",
                     "1QNsRQKJ6eRTxY9x8HQ3RcdwNd48IF4ywk0MWFI0ILqG7")
    return api


def registerTweetCallback(n):
    try:
        api = registerApi()
        # Stream tweets from New York City:
        r = api.request('statuses/filter', {'locations': '-179.1506, 18.9117, -66.9326, 71.4410'})
    except:
        return n

    try:
        for item in r.get_iterator():
            try:
                callback(item)
                n += 1
                if n >= 10000:
                    n = 0
                    save()

                if n % 1000 == 0:
                    print n
                    # print(item)
            except:
                continue
    except:
        return n


def callback(item):
    global States
    if item['coordinates'] != None:
        res = state(item['coordinates']['coordinates'])
        if res != None:
            d = 2
            try:
                line = item['text'].encode('utf-8')
                line = item['text'].encode('ascii')
            except:
                return

            d = check2(line)
            if d == 2:
                return

            if d == 1:
                States[res][1] += 1
            if d == 0:
                States[res][0] += 1

    return


def state(dot):
    x = dot[0]
    y = dot[1]
    for state in States_coord.keys():
        if States_coord[state][0] <= x <= States_coord[state][2] and States_coord[state][1] <= y <= States_coord[state][
            3]:
            return state
    return None


def check2(text):
    testimonial = TextBlob(text)
    if testimonial.sentiment.polarity >= 0.01:
        return 1
    if testimonial.sentiment.polarity <= -0.01:
        return 0

    return 2


def calc_param(x):
    if sum(x) == 0:
        return 0
    return float(x[1]) / (x[0] + x[1]) * 100


def save():
    # curr time
    t = str(time.time())

    # save curr values
    na_file = open('dict.txt', 'w')
    pickle.dump(States, na_file)
    na_file.close()

    # save history
    na_file = open('dicts/dict' + t + '.txt', 'w')
    pickle.dump(States, na_file)
    na_file.close()

    # save map
    for states in States:
        if states in States_ok:
            # check ranges
            temp = calc_param(States[states])
            if temp < 40:
                temp = 40
            elif temp > 70:
                temp = 70

            States_ok[states] = temp

    map.visualize(States_ok, t)


def load():
    global States
    try:
        na_file = open('dict.txt', 'r')
        States = pickle.load(na_file)
    except:
        pass

def check_bounding_boxes():
    inf = 99999
    maxx = -inf
    minx = inf
    maxy = -inf
    miny = inf
    for i in States_coord.values():
        if i[0]<minx:
            minx = i[0]
        if i[1]<miny:
            miny = i[1]
        if i[2]>maxx:
            maxx = i[2]
        if i[3]>maxy:
            maxy = i[3]
    print("minx",minx)
    print("miny",miny)
    print("maxx",maxx)
    print("maxy",maxy)

    k = ""
    maxx = -inf

    for i in States_coord.keys():
        if States_coord[i][2]>maxx:
            maxx = States_coord[i][2]
            k = i
    print(maxx,k)

if __name__ == "__main__":
    for i in States_coord.keys():
        States[i] = [0, 0]

    for i in States_ok.keys():
        States_ok[i] = 40

    load()
    print States

    n = 0
    while True:
        try:
            n = registerTweetCallback(n)
        except:
            pass


