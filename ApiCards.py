import requests # Se importa la libreria requests

api_url = "https://fakerapi.it/api/v1/credit_cards?_quantity=1" #Se crea una variable donde se almacena la dirección url de la API que se va a consumir. En este caso se consume una API que solicita datos de clientes con tarjeta de crédito.


response = requests.get(api_url) #Se crea una variable que almacena el resultado de realizar un método GET a la API que se está consumiendo.

print(response) #Se imprime el contenido de la variable 'response'. Si se ejecuta de manera correcta, debe imprimir el código de estado de la petición. Si la petición se realiza de manera correcta, el resultado es 'Response [200] '

if response.status_code == 200: #Se valida que el resultado del código de estado sea 200 para realizar el seguiente bloque de código.

    content = response.json()  # Se crea una variable que va a almacenar el contenido del Json que se obtiene de la petición GET a la API. La variable 'content' es un diccionario. 

    card = content['data'] #Se crea la variable 'card' que almacena únicamente el valor del atributo 'data' del Json obtenido en la solicitud GET donde vienen únicamente los datos de vinculados a la tarjeta de crédito, omitiendo los argumentos del Json que indican el estado y el código de estado.

    print(card) #Se imprime el contenido de la variable 'card'

    file = open('datos.txt', 'w')  #Se crea un archivo llamado 'datos' con extensión txt y permisos de escritura. 

    file.write(str(content)) #Se escribe el contenido de la variable 'content' en el archivo creado. 

    file.close() #Se cierra el archivo.

    

    print(content) #Se imprime en la terminal el Json obtenido tras la petición. 


