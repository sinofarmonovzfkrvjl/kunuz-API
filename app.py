from fastapi import FastAPI
from kunuz import KunUzNews

app = FastAPI(
    title="KunUz API",
    description="bu kunuz 3 taraf API (kunuzning o'zini rasmiy API yo'q)",
    summary="savol va takluflar uchun https://t.me/sinofarmonov",
    version="1.0.0",
    docs_url='/',
    redoc_url='/docs'
)

@app.get("/news/songi-yangiliklar", tags=['News'])
async def songi_yangiliklar():
    news = KunUzNews().songi_yangiliklar()
    return news

@app.get("/news/yangilik", tags=['News'])
async def yangilik():
    return KunUzNews().yangilik()

@app.get("/news/uzbekiston-yangiliklar", tags=['News'])
async def uzbekiston_yangiliklar():
    news = KunUzNews().yangiliklar()
    data = []
    for i in range(len(news['titles'])):
        data.append({'title': news['titles'][i], 'description': news['descs'][i]})
    return data

@app.get("/news/jahon-yangiliklari", tags=['News'])
async def jahon_yangiliklari():
    news = KunUzNews().jahon_yangiliklari()
    data = []
    for i in range(len(news['titles'])):
        data.append({'title': news['titles'][i], 'description': news['descs'][i]})
    return data
