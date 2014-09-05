import pickle
from textblob import TextBlob
import matplotlib.pyplot as plt
#################################################

def read_data2():
    f = open("../testSet.txt", "r")
    text = []
    n = 0  # number of line
    for line in f.read().split("\n"):

        if line == "":
            continue
        st = line
        tt = st.split('\t', 3)
        # print(tt)
        na, textt = tt
        try:
            textt = textt.encode("UTF-8")
        except:
            continue
        # print(textt)
        n += 1

        text.append((int(na), textt))
    print "number of lines:", n

    return text


def read_data(x):
    f = open("../Sentiment Analysis Dataset.csv", "r")
    text = []
    n = 0  # number of line
    for line in f.read().split("\n"):
        if n == 0:
            n = 1
            continue

        if line == "":
            continue
        st = line
        tt = st.split(',', 3)
        # print(tt)
        num, na, s, textt = tt
        try:
            textt = textt.encode("UTF-8")
        except:
            continue

        n += 1
        if n == x:
            break

        text.append((int(na), textt))

    return text


def test(text):

    list_1 = []
    for line in text:
        sentences = line[1]
        list_1.append(check2(sentences))

    # print(list_1)
    res = []    # result list

    text_len = len(text)

    delta = 0.25
    middle = -0.15
    while middle < 0.16:
        middle += 0.05

        skiped_1 = 0
        skiped_0 = 0
        correct = 0
        line_num = 0
        wrongs = [0,0]
        summa = 0
        for x in list_1:
            line = text[line_num]
            line_num += 1


            d = 2
            if middle + delta <= x:
                d = 1
            elif middle - delta >= x:
                d = 0

            if d == 2:
                if line[0] == 0:
                    skiped_0 += 1
                if line[0] == 1:
                    skiped_1 += 1
                continue

            summa += d
            if d == line[0]:
                correct += 1
            else:
                wrongs[(d+1)%2] += 1


        if text_len - skiped_1 - skiped_0 > 0:
            accurancy = float(correct) / (text_len - skiped_1 - skiped_0)
        else:
            accurancy = 0

        if skiped_0+skiped_1 > 0:
            sk1 = float(skiped_1)/(skiped_0+skiped_1)
        else:
            sk1 = 0

        res.append((accurancy, skiped_0, skiped_1, middle, sk1, wrongs, (wrongs[1]+skiped_1)/(sum(wrongs)+skiped_1+float(skiped_0)),summa))

    return res


def check2(text):
    return TextBlob(text).sentiment.polarity


def save(x, name):
    na_file = open(name, 'w')
    pickle.dump(x, na_file)
    na_file.close()


def main():
    # read train set
    text = read_data(500000)

    n = len(text)/5

    # calc number of positive examples in train set
    sumx = 0
    for i in text[:n]:
        sumx += i[0]
    n1 = sumx/float(n)
    print "% positive in first 10^5:", n1

    sumx = 0
    for i in text[n:5*n]:
        sumx += i[0]
    n2 = sumx/float(4*n)
    print "% positive in last 4*10^5:", n2


    # test classifier
    res_list = test(text[:n])
    res_list_check = test(text[n:5*n])

    # save
    save(res_list, "res_list.txt")
    save(res_list_check, "res_list_check.txt")

    # print
    print("res_list")
    for i in res_list:
        print(i)

    print("res_list_check")
    for i in res_list_check:
        print(i)

    # plot

    x = [res_list[i][3] for i in range(len(res_list))]
    # y1 = [res_list[i][0]*(n-res_list[i][2]-res_list[i][1])/(res_list[i][2]+res_list[i][1])*res_list[i][6]/n1 for i in range(len(res_list))]
    # y2 = [res_list_check[i][0]*(5*n-res_list_check[i][2]-res_list_check[i][1])/(res_list_check[i][2]+res_list_check[i][1])*res_list_check[i][6]/n2 for i in range(len(res_list))]
    y1 = [res_list[i][7]/float(n-res_list[i][1]-res_list[i][2]) for i in range(len(res_list))]
    y2 = [res_list_check[i][7]/float(n*5-res_list_check[i][1]-res_list_check[i][2]) for i in range(len(res_list_check))]
    y3 = [n1 for i in range(len(res_list))]
    y4 = [n2 for i in range(len(res_list_check))]
    print(y1)
    print(y2)

    plt.plot(x, y1)
    plt.plot(x,y3)
    plt.show()

    plt.plot(x, y2)
    plt.plot(x,y4)
    plt.show()


main()
