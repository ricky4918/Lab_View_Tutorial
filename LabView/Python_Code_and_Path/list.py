def listitems(userenter):
    listdata = ['python', 'tutorial', '6', 'test']
    listdata2 = ['test', 'is', 'successful']
    listdata.insert(0,userenter)
    listdata.pop(1)
    listdata.remove('test')
    listdata.extend(listdata2)
    listdata[1] = 'changed'
    return listdata