from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="src/webserver/static"), name="static")


templates = Jinja2Templates(directory="src/webserver/templates")

@app.get('/', response_class=HTMLResponse)
async def main(request: Request):
    return templates.TemplateResponse(request=request, name='index.html')

@app.get('/upload-document', response_class=HTMLResponse)
async def upload_document(request: Request):
    return templates.TemplateResponse(request=request, name='upload-document.html')


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8080)