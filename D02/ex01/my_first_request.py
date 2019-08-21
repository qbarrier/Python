import requests
def req_users() :
    json_obj = requests.get('https://jsonplaceholder.typicode.com/users')
    json_obj = json_obj.json()
    res = str("")
    for  name in json_obj :
        res +=  name['name'] + "\n"
    return (res)

if __name__ == '__main__':
    res = req_users()
    print(res, end = '')
