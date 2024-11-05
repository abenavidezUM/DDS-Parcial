## Parcial - Diseño de Sistemas   
###### Agustin Benavidez
------------
### Test Coverage
<a href="https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-abenavidezUM/test_coverage"><img src="https://api.codeclimate.com/v1/badges/628e0630c53cad57ef7a/test_coverage" /></a>

-------------
# Ejecucion de la API

## Render
1) ### Crear un nuevo servicio

2) ### Seleccionar el repositorio y rama que va a desplegar 

   21) ### En build command y start command:
```bash
    pip install -r requirements.txt 
``` 
```bash
    uvicorn app.main:app --host 0.0.0.0 --port 8000
``` 
3) ### Desplegar el servicio

### Para el servicio ya desplegado

1) ### Ingresar a:
```bash
    https://dds-parcial-1.onrender.com
``` 
2) ### En postman usar un nuevo metodo POST y poner la siguiente URL:
```bash
    https://dds-parcial-1.onrender.com/mutant/
``` 
3) ### Configurar el Body de la solicitud 
```bash
    {
  "dna": ["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"]
    }
``` 
4) ### Enviar la solicitud y comprobar la devolucion
```bash
    {
    "message": "Mutant detected"
    }
``` 

## Local
1) ### Crear un entorno virtual
```bash
    python3 -m venv env
``` 
2) ### Activar el entorno virtual
```bash
    source env/bin/activate
``` 
3) ### Instalar las dependencias
```bash
    pip install -r requirements.txt
``` 
4) ### Ejecutar la aplicacion
```bash
    uvicorn app.main:app --reload
``` 
5) ### En un navegador iniciar el servidor para corroborar que funciona:
```bash
    http://127.0.0.1:8000/
``` 
6) ### Verificar desde postman:
```bash
    URL: http://127.0.0.1:8000/mutant/
    BODY: 
    {
  "dna": ["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"]
    }
``` 