def findData(data):
    result = []
    for item in data:
        if(item['value'] >= 4):
            result.append(item)
    return result

def amendData(data):
    for item in data:
        #note this assumes all data does not already start with 'www.'
        item['domain'] = 'www.' + item['domain']
    return data

def cleanseData(data):
    for item in data:
        if(item['url'][0:5] == 'https'):
            if(not item['secure']):
                item['secure'] = True
        else:
            if(item['secure']):
                item['secure'] = False

    return data

def dataCalculation(data):
    sum = 0
    for item in data:
        sum += item['value']
    return sum