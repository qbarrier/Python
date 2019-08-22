import requests
def ft_codes():
    req = requests.get('https://httpbin.org./status/200')
    print ("Le code 200 a pour reason : \"" + req.reason+ "\"")
    req = requests.get('https://httpbin.org./status/201')
    print ("Le code 201 a pour reason : \"" + req.reason+ "\"")
    req = requests.get('https://httpbin.org./status/401')
    print ("Le code 401 a pour reason : \"" + req.reason+ "\"")
    req = requests.get('https://httpbin.org./status/403')
    print ("Le code 403 a pour reason : \"" + req.reason+ "\"")
    req = requests.get('https://httpbin.org./status/404')
    print ("Le code 404 a pour reason : \"" + req.reason+ "\"")
    req = requests.get('https://httpbin.org./status/500')
    print ("Le code 500 a pour reason : \"" + req.reason+ "\"")
    req = requests.get('https://httpbin.org./status/502')
    print ("Le code 502 a pour reason : \"" + req.reason+ "\"")

if __name__ == '__main__':
    ft_codes()
