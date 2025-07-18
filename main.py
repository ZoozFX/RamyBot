from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/ar", response_class=HTMLResponse)
async def form_ar(request: Request):
    return templates.TemplateResponse("form_ar.html", {"request": request})

@app.get("/en", response_class=HTMLResponse)
async def form_en(request: Request):
    return templates.TemplateResponse("form_en.html", {"request": request})

@app.post("/register")
async def register(request: Request):
    data = await request.json()
    print("Received data:", data)  # يمكنك استبدال هذا بإرسال البيانات إلى البوت
    return {"status": "success"}
