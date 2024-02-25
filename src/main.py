from deta import Deta
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["localhost:4200"],
    allow_credentials=True,
    allow_methods=["POST, PUT, GET"],
    allow_headers=["*"],
)

deta = Deta()

db = deta.Base("whatmoon")


@app.get("/")
async def root():
    return {"message": "ほわむん♪"}


@app.put("/v1/pressed/{key}")
async def update_like_counts(key: str):
    res = db.get(key)
    if not res:
        return {"response": f"not found: {key}"}
    else:
        db.update({"likes": db.util.increment()}, key)
        res = await get_like_counts(key)
        return {"response": res}


@app.get("/v1/get/{key}")
async def get_like_counts(key: str):
    res = db.get(key)
    if not res:
        return {"response": f"not found: {key}"}
    else:
        return {"response": res}


@app.post("/v1/create/{key}")
async def create_like_button(key: str, likes: int = 0):
    if db.get(key):
        return {"response": f"already exists: {key}"}
    else:
        res = db.put({"likes": likes}, key)
        return {"response": res}


@app.delete("/v1/delete/{key}")
async def delete_like_button(key: str):
    if not db.get(key):
        return {"response": f"not found: {key}"}
    else:
        db.delete(key)
        return {"response": f"ほわっ… {key} を削除しましたっ！"}
