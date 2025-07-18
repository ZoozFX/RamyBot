from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/form_ar.html", response_class=HTMLResponse)
async def get_form_ar(request: Request):
    return templates.TemplateResponse("form_ar.html", {"request": request})

@app.get("/form_en.html", response_class=HTMLResponse)
async def get_form_en(request: Request):
    return templates.TemplateResponse("form_en.html", {"request": request})

@app.post("/submit")
async def submit_data(
    name: str = Form(...),
    email: str = Form(...),
    phone: str = Form(...),
    broker: str = Form(...)
):
    print(f"✅ New submission: {name} - {email} - {phone} - {broker}")
    return RedirectResponse(url="/thanks", status_code=303)

@app.get("/thanks", response_class=HTMLResponse)
async def thank_you(request: Request):
    return HTMLResponse("<h2>✅ شكراً لتسجيلك!</h2>")
