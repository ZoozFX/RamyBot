from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

class Registration(BaseModel):
    name: str
    email: str
    phone: str
    broker: str

@app.get("/ar", response_class=HTMLResponse)
async def serve_ar():
    with open("html/form_ar.html", encoding="utf-8") as f:
        return f.read()

@app.get("/en", response_class=HTMLResponse)
async def serve_en():
    with open("html/form_en.html", encoding="utf-8") as f:
        return f.read()

@app.post("/register")
async def register(data: Registration):
    print("📩 Data received:", data.dict())
    # هنا يمكنك إرسال رسالة للبوت أو حفظها في قاعدة بيانات
    return {"status": "ok"}
