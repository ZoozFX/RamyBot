from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/form_ar.html", response_class=HTMLResponse)
async def serve_form_ar(request: Request):
    return templates.TemplateResponse("form_ar.html", {"request": request})

@app.get("/form_en.html", response_class=HTMLResponse)
async def serve_form_en(request: Request):
    return templates.TemplateResponse("form_en.html", {"request": request})
