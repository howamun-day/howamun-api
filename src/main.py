from deta import Deta
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

deta = Deta()

db = deta.Base("whatmoon")


@app.get("/")
async def root():
    return {"data": {"message": "ほわむん♪"}}


@app.put("/v1/increment/{key}")
async def increment_like_counts(key: str, num_increment: int = 1):
    res = db.get(key)
    if not res:
        return {"data": {"message": f"ほわっ…keyが見つからなかったです……: {key}"}}
    else:
        db.update({"likes": db.util.increment(num_increment)}, key)
        res = db.get(key)
        return {
            "data": {
                "message": f"ほわっ…いいねが{num_increment}増えました♪",
                "response": res,
            },
        }


@app.get("/v1/get/{key}")
async def get_like_counts(key: str):
    res = db.get(key)
    if not res:
        return {"data": {"message": f"ほわっ…keyが見つからなかったです……: {key}"}}
    else:
        return {
            "data": {"message": "ほわっ…いいねの数を取得しました♪", "response": res}
        }


@app.post("/v1/create/{key}")
async def create_like_button(key: str, likes: int = 0):
    if db.get(key):
        return {"data": {"message": f"ほわっ…keyがすでに存在しています……: {key}"}}
    else:
        res = db.put({"likes": likes}, key)
        return {
            "data": {
                "message": f"ほわっ…新しいkey: {key} を作成しました♪",
                "response": res,
            }
        }
