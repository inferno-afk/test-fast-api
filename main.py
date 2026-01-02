from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/')
def home():
    return {"Hello":"This is home page"}

@app.get('/health')
def health_check():
    return {"status":"OK"}

if __name__ == "__main__":
    uvicorn.run(host='0.0.0.0', port=port)