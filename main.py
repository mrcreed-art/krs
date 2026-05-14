from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Football AI SaaS Actived to CK !!"}

@app.get("/predict")
def predict():
    return {
        "home_win": 0.45,
        "draw": 0.28,
        "away_win": 0.27
    }
