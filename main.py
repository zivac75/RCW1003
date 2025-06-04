from fastapi import FastAPI , HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.get("/")
async def welcome():
    try:
        return{"message" : "TNAKT"}
    except Exception as e:
        print(f'Exception : {e}')
        raise HTTPException(status_code = 500 , detail = str(e))
    
@app.get("/")
async def Bienvenue():
    try:
        return{"message" : "TNAKT x2"}
    except Exception as e:
        print(f'Exception : {e}')
        raise HTTPException(status_code = 500 , detail = str(e))