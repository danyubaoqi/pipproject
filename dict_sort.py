class Dict_sort():
    def __init__(self, data):
        self.data = data

    def sort(self, reserve=True):
        dataall = self.data
        a, b = [], []
        for x in dataall:
            a.append(x)
            b.append(dataall[x])
        c=[]
        for i in range(len(a)):
            c.append([a[i],b[i]])
        c=sorted(c,key=lambda x: x[1], reverse=reserve)
        return c
