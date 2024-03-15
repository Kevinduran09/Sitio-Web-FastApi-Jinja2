import json


class dataController:
    def __init__(self) -> None:
        pass
    def load_data(self):
        with open('misdatos.json','r+') as archivo:
            try:
                datos = json.load(archivo)
                return datos
            except json.JSONDecodeError as error:
                print('error en la carga del archivo: {error}')
                return 'No hay datos en el sistema'
    def save_data(self,data:str):
        try:
            with open('misdatos.json','r+') as ar:
                try:
                    datos = json.load(ar)
                except json.JSONDecodeError:
                    datos = []
                
                datos.append(data)
                
                ar.seek(0)
                
                json.dump(datos,ar)
                
                ar.truncate()
        except FileNotFoundError:
            with open('misdatos.json','w') as ar:
                json.dump([data],ar)
        