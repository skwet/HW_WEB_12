import uvicorn
import fastapi
from src.routes import contacts,auth


app = fastapi.FastAPI(debug=True)


app.include_router(contacts.router, prefix = '/api')
app.include_router(auth.router, prefix = '/api')


if __name__ == '__main__':
    uvicorn.run(
        'main:app',host = 'localhost', port = 8000 , reload = True
    )