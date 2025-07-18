from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/form_ar.html", response_class=HTMLResponse)
async def form_ar(request: Request):
    return templates.TemplateResponse("form_ar.html", {"request": request})

@app.get("/form_en.html", response_class=HTMLResponse)
async def form_en(request: Request):
    return templates.TemplateResponse("form_en.html", {"request": request})
