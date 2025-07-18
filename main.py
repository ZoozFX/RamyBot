from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def serve_form():
    with open("form.html", encoding="utf-8") as f:
        return f.read()
