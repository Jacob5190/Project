import linecache


def getList():
    file = open("save.txt", "r")
    datas = linecache.getlines("save.txt")
    file.close()
    return datas


def wirteFile(string):
    file = open("save.txt", "w")
    file.writelines(string)
    file.close()


class data:
    def __init__(self, index, name, days):
        self.index = index
        self.name = name
        self.days = days

    def getData(self):
        data = str(self.index)+"/"+self.name+"/"+str(self.days)+"\n"
        return data


def writeData():
    datas = getList()
    name = input("name: ")
    days = int(input("days: "))
    file = open("save.txt", "r")
    index = len(linecache.getlines("save.txt"))
    data_1 = data(index+1, name, days)
    string = data_1.getData()
    datas.append(string)
    wirteFile(datas)
    file.close()


def search(index):
    flag = False
    datas = getList()
    for i in range(0, len(datas)):
        ind = (datas[i].split("/"))[0]
        if int(ind) == index:
            flag = True
            return datas[i]
    if not flag:
        return None


def delete(index):
    datas = getList()
    for i in range(0, len(datas)):
        ind = (datas[i].split("/"))[0]
        if int(ind) == index:
            datas.pop(i)
            break
    wirteFile(datas)


writeData()
