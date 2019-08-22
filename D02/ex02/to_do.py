import requests


# Ervin Howell, Patricia Lebsack et Glenna Reichert
# 2, 4, 9

def req_users() :
    dict_users = {
            "Ervin Howell": "",
            "Patricia Lebsack": "",
            "Glenna Reichert": ""
            }
    json_obj = requests.get('https://jsonplaceholder.typicode.com/users')
    json_obj = json_obj.json()
    for  name in json_obj :
        if name['name'] == "Ervin Howell" :
            dict_users["Ervin Howell"] = name['id']
        elif name['name'] == "Patricia Lebsack" :
            dict_users["Patricia Lebsack"] = name['id']
        elif name['name'] == "Glenna Reichert" :
            dict_users["Glenna Reichert"] = name['id']

    json_todo = requests.get('https://jsonplaceholder.typicode.com/todos')
    json_todo = json_todo.json()
    dict_todo = {
            dict_users["Ervin Howell"] : 0,
            dict_users["Patricia Lebsack"] : 0 ,
            dict_users["Glenna Reichert"] : 0 
            }
    for x in json_todo :
        if x['userId'] == dict_users["Ervin Howell"] and not x['completed'] :
            dict_todo[dict_users["Ervin Howell"]] += 1
        elif x['userId'] == dict_users["Patricia Lebsack"] and not x['completed']:
            dict_todo[dict_users["Patricia Lebsack"]] += 1
        elif x['userId'] == dict_users["Glenna Reichert"] and not x['completed']:
            dict_todo[dict_users["Glenna Reichert"]] += 1


    print("Ervin Howell =" , dict_todo[dict_users["Ervin Howell"]], "todo uncompleted")
    print("Patricia Lebsack =" , dict_todo[dict_users["Patricia Lebsack"]], "todo uncompleted")
    print("Glenna Reichert =" , dict_todo[dict_users["Glenna Reichert"]], "todo uncompleted")

if __name__ == '__main__':
    req_users()
