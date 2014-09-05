import pickle

from work import map

States_ok = {
    'New Jersey':  438.00,
    'Rhode Island':   387.35,
    'Massachusetts':   312.68,
    'Connecticut':	  271.40,
    'Maryland':   209.23,
    'New York':    155.18,
    'Delaware':    154.87,
    'Florida':     114.43,
    'Ohio':	 107.05,
    'Pennsylvania':	 105.80,
    'Illinois':    86.27,
    'California':  83.85,
    'Hawaii':  72.83,
    'Virginia':    69.03,
    'Michigan':    67.55,
    'Indiana':    65.46,
    'North Carolina':  63.80,
    'Georgia':     54.59,
    'Tennessee':   53.29,
    'New Hampshire':   53.20,
    'South Carolina':  51.45,
    'Louisiana':   39.61,
    'Kentucky':   39.28,
    'Wisconsin':  38.13,
    'Washington':  34.20,
    'Alabama':     33.84,
    'Missouri':    31.36,
    'Texas':   30.75,
    'West Virginia':   29.00,
    'Vermont':     25.41,
    'Minnesota':  23.86,
    'Mississippi':	 23.42,
    'Iowa':	 20.22,
    'Arkansas':    19.82,
    'Oklahoma':    19.40,
    'Arizona':     17.43,
    'Colorado':    16.01,
    'Maine':  15.95,
    'Oregon':  13.76,
    'Kansas':  12.69,
    'Utah':	 10.50,
    'Nebraska':    8.60,
    'Nevada':  7.03,
    'Idaho':   6.04,
    'New Mexico':  5.79,
    'South Dakota':	 3.84,
    'North Dakota':	 3.59,
    'Montana':     2.39,
    'Wyoming':      1.96,
    'Alaska':     0.42}


def calc_param(x):
    return float(x[1])/(x[0]+x[1])*100

def test():
    na_file = open('../dict.txt', 'r')
    States = pickle.load(na_file)
    na_file = open('../dict3.txt', 'r')
    States2 = pickle.load(na_file)
    print(States)
    print(States2)
    list1 = []
    for i in States.keys():
        if i in States2.keys():
            if sum(States2[i]) > 100 and sum(States[i]) > 100:
                list1.append((abs(calc_param(States[i])-calc_param(States2[i])),i,calc_param(States[i]),calc_param(States2[i])))
    list1 = sorted(list1)
    for i in list1:
        print(i)
    #     print(i[0],i[1]-i[2])

def test_by_order():
    na_file = open('../dict4.txt', 'r')
    States = pickle.load(na_file)
    na_file = open('../dict2.txt', 'r')
    States2 = pickle.load(na_file)
    na_file = open('../dict3.txt', 'r')
    States3 = pickle.load(na_file)
    print(States)
    print(States2)
    print(States3)
    list1 = []
    list2 = []
    list3 = []
    States4 ={}
    for i in States.keys():
        States4[i] = []
        States4[i].append(States[i][0]+States2[i][0]+States3[i][0])
        States4[i].append(States[i][1]+States2[i][1]+States3[i][1])
    print(States4)
    list4 = []

    for i in States.keys():
        if i in States2.keys():
            if sum(States2[i]) > 100 and sum(States[i]) > 100 and sum(States3[i]) > 100 and sum(States4[i])>100:
                list1.append((calc_param(States[i]),i))
                list2.append((calc_param(States2[i]),i))
                list3.append((calc_param(States3[i]),i))
                list4.append((calc_param(States4[i]),i))
    list1 = sorted(list1)
    list2 = sorted(list2)
    list3 = sorted(list3)
    list4 = sorted(list4)
    for i in range(len(list1)):
        print(list1[i][1], list2[i][1], list3[i][1], list4[i])
    for i in States4.keys():
        if i in States_ok.keys():
            States4[i] = calc_param(States4[i])
        for i in States_ok:
            if i not in States4.keys():
                States4[i] = 0
    # map.visualize(States4)

def normalize(x):
    a = 1./30
    b = -1*40.0/30
    # return a*x+b
    return x


def main():
    na_file = open('../dict.txt', 'r')
    States = pickle.load(na_file)
    print States
    for i in States_ok.keys():
        States_ok[i] = normalize(40)
    for state in States.keys():
        if sum(States[state])>100:
            States_ok[state] = normalize(calc_param(States[state]))
            print(state,States_ok[state])
        else:
            States_ok[state] = normalize(40)

    map.visualize(States_ok)

# test()
# main()
# test_by_order()
def test2():
    na_file = open('../dict.txt', 'r')
    States = pickle.load(na_file)
    ls = []
    for i in States.keys():
        if sum(States[i]) > 100:
            ls.append((States[i][1]/float(sum(States[i])),i))
            print i,States[i],States[i][1]/float(sum(States[i]))
    ls = sorted(ls)
    for i in ls:
        print(i)

    print(len(States))

test2()




