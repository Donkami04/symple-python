import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/items', response_class=HTMLResponse)
async def read_items():
    return """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </htm>
    """

@app.get('/', response_class=HTMLResponse)
def get_list():
    return '''
    <html>
        <h1> Hola, soy tu titulo en Python </h1>
        <p> Y yo soy tu parrafor jejej </p>
    </html>
    
    '''

@app.get('/contact')
def get_list():
    return {'name': 'platzi'}


def run():
    store.get_categories()

if __name__ == '__main__':
    run()
    
hola = ''