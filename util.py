import pickle

def writer(file_name,content):
    with open(file_name,'wb+') as file:
        pickle.dump(content,file)

def reader(file_name):
    with open(file_name,'rb') as file:
        content=pickle.load(file)
    return content

def add_data(data):
    api_data=reader('api_data.pkl')
    csv_data=reader('csv_data.pkl')
    api_data.append(data)
    csv_data.append(data)
    writer('api_data.pkl',api_data)
    writer('csv_data.pkl',csv_data)

def api_request():
    response=reader('api_data.pkl')
    writer('api_data.pkl',[])
    #print("send form ",response)
    return response

def csv_request():
    content=reader('csv_data.pkl')
    writer('csv_data.pkl',[])
    return content