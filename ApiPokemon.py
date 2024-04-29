import requests # Se importa la libreria requests

api_url = "https://fakerapi.it/api/v1/custom?_quantity=10&customfield1=pokemon" #Se crea una variable donde se almacena la dirección url de la API que se va a consumir. En este caso se consume una API que solicita nombres de pokemones de una API proporcionada por la página de 'fakerapi'. Se están solicitando a la API 10 nombres de pokemones.

response = requests.get(api_url) #Se crea una variable que almacena el resultado de realizar un método GET a la API que se está consumiendo.

print(response) #Se imprime el contenido de la variable 'response'. Si se ejecuta de manera correcta, debe imprimir el código de estado de la petición. Si la petición se realiza de manera correcta, el resultado es 'Response [200] '

if response.status_code == 200: #Se valida que el resultado del código de estado sea 200 para realizar el seguiente bloque de código.

    content = response.json()  # Se crea una variable que va a almacenar el contenido del Json que se obtiene de la petición GET a la API. La variable 'content' es un diccionario. 

    results = content.get('data',[]) #Se crea un variable que almacena los valores del Json cuya clave es 'data'

    if results: #Se valida que la variable 'results' no se encuentre vacía
        for pokemon in results:  #Se genera un ciclo for para listar los nombres de los pokemones obtenidos tras la petición GET

            name=pokemon['customfield1']
            print(name)
