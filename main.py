from fastapi import FastAPI

app = FastAPI(title='test deploy', version="0.1.0", description="test deploy fastapi")


@app.get('/')
def index():
    return {"message": "Hello World!"}



@app.get("/health")
def health():
    return {"status": "ok"}


@app.get('/greet')
def greet():
    return {"message": "Привет из деплоя!!!!"}

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


class Lead(BaseModel):
    name: str
    email: str
    message: str = ""


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/api/lead")
async def create_lead(lead: Lead):
    # тут можно сохранить в БД; пока просто логируем
    print(f"Новая заявка: {lead.name} <{lead.email}>: {lead.message}")
    return {"ok": True, "message": f"Спасибо, {lead.name}! Заявка принята."}
