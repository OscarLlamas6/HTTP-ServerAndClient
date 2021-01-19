import http.client
import json


myConnection = http.client.HTTPConnection('localhost', 8000, timeout=10)

#Headers texto plano
headers = {
        "Content-type": "text/plain"
    }

#Headers json
headersJson = {
        "Content-type": "application/json"
    }
#Data texto plano
postData = "Test http.server from http.client :D"

#Variables para simular credenciales
username = "Oscar"
password = "123"

#Data en formato json
jsonData = { "username": username, "password": password }
myJson = json.dumps(jsonData)


#METODO POST CON TEXTO PLANO
def Root():
    myConnection.request("POST", "/", postData, headers)
    response = myConnection.getresponse()
    print("POST: Status: {} and reason: {}".format(response.status, response.reason))
    if response.status == 200:       
        data = response.read()
        result = data.decode("utf-8")
        print(result)
    myConnection.close()



#JOIN CON METODO POST
def CheckLog():
    myConnection.request("POST", "/checkLogin", myJson, headersJson)
    response = myConnection.getresponse()
    print("POST: Status: {} and reason: {}".format(response.status, response.reason))
    if response.status == 200:       
        data = response.read()
        result = data.decode("utf-8")
        if result == "true":
            print("Usuario loggeado correctamente.")
        elif result == "error":
            print("Ha ocurrido un error.")
        else:
            print("Datos invalidos o usuario inexistente.")
    else:
        print("Ha ocurrido un error.")
    myConnection.close()

#CREATE USER CON METODO POST
def CreateUser():
    myConnection.request("POST", "/createUser", myJson, headersJson)
    response = myConnection.getresponse()
    print("POST: Status: {} and reason: {}".format(response.status, response.reason))
    if response.status == 200:       
        data = response.read()
        result = data.decode("utf-8")
        if result == "false":
            print("Usuario creado correctamente.")
        elif result == "error":
            print("Ha ocurrido un error.")
        else:
            print("Usuario ya existe actualmente, intente con otro username.")
    else:
        print("Ha ocurrido un error.")
    myConnection.close()

#GET USERS CON METODO GET
def GetUsers():
    myConnection.request("GET", "/getUsers", "", headersJson)
    response = myConnection.getresponse()
    print("GET: Status: {} and reason: {}".format(response.status, response.reason))
    if response.status == 200:       
        data = response.read()   
        print(data.decode("utf-8"))
    myConnection.close()


GetUsers()