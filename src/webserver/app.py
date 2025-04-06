from fastapi import FastAPI, Request, UploadFile, File, BackgroundTasks
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from src.parser import extract_data
from pathlib import Path
import os
import asyncio

app = FastAPI()

app.mount("/static", StaticFiles(directory="src/webserver/static"), name="static")
app.mount("/temp", StaticFiles(directory="src/webserver/temp"), name="temp")

templates = Jinja2Templates(directory="src/webserver/templates")

async def delete_temp_file(file_name: str):
    await asyncio.sleep(600)
    try:
        os.remove(f"src/webserver/temp/{file_name}")
    except:
        print('Could not remove temp file')
    else:
        print('Temp file removed')

@app.get('/', response_class=HTMLResponse)
async def main(request: Request):
    return templates.TemplateResponse(request=request, name='index.html')

@app.get('/upload-document', response_class=HTMLResponse)
async def upload_document(request: Request):
    return templates.TemplateResponse(request=request, name='upload-document.html')

@app.post('/upload-document')
async def hanlde_file(request: Request,file: UploadFile):
    with open(f'src/webserver/temp/{file.filename}', 'wb') as f:
        f.write(await file.read())
    return RedirectResponse(f'/document-info/{file.filename}', status_code=303)

@app.get('/document-info/{file_name}')
async def document_info(request: Request, file_name: str, background_tasks: BackgroundTasks):
    _file = Path(f"src/webserver/temp/{file_name}")
    content_iterator = extract_data(_file)
    items = extract_data(_file)
    speakers = set()
    for item in content_iterator:
        speakers.add(item.speaker.title())
    ctx = {
        'file_name':file_name,
        'speakers':speakers,
        'items':items
    }
    background_tasks.add_task(delete_temp_file, file_name)
    return templates.TemplateResponse(request=request, name='document-info.html', context=ctx)

@app.delete('delete-temp/{file_name}')
async def delete_temp(request: Request, file_name: str):
    try:
        os.remove(f"src/webserver/temp/{file_name}")
    except:
        print('Could not remove temp file')
    else:
        print('Temp file removed')
    return

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8080)