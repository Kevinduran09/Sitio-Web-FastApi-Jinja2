from fastapi import FastAPI,Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from services.dataController import dataController
import uvicorn


app = FastAPI()
app.mount('/static',StaticFiles(directory='static'),name='static')
templates = Jinja2Templates(directory='templates')


@app.get('/',response_class=HTMLResponse)
async def root(request:Request):
    service = dataController()
    return templates.TemplateResponse(name='index.html',context={'request':request,'todos':service.load_data()})


""" 
def guardar_info(data: str):
    try:
        # Abre el archivo en modo lectura y escritura
        with open('misdatos.json', 'r+') as ar:
            try:
                # Intenta cargar los datos JSON existentes
                datos = json.load(ar)
            except json.JSONDecodeError:
                # Si hay un error de JSONDecodeError, inicializa una lista vacía
                datos = []

            # Agrega el nuevo dato a la lista
            datos.append(data)

            # Lleva el puntero al principio del archivo
            ar.seek(0)

            # Escribe los datos actualizados en el archivo
            json.dump(datos, ar)

            # Trunca el archivo para eliminar cualquier contenido adicional
            ar.truncate()

    except FileNotFoundError:
        # Si el archivo no existe, crea uno nuevo con el nuevo dato
        with open('misdatos.json', 'w') as ar:
            json.dump([data], ar)

        
def cargar_info():
    try:
        with open('misdatos.json','r+') as ar:
            data = json.load(ar)
            print(data)
            return data
    except json.JSONDecodeError:
        print('no hay archivos en el sistema')
    return None

@app.get('/')
async def root():
    data = cargar_info()
    
    return {'data':data if data!=None else 'holamundo'}


@app.get('/item/{id}', response_class=HTMLResponse)
async def template(id:str,request:Request):
    guardar_info(id)
    return templates.TemplateResponse(
        request=request,name='index.html',context={'id':id}
        )
    
if __name__ == '__main__':
    uvicorn.run(app=app)
"""