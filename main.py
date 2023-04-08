from fastapi import FastAPI
from pydantic import BaseModel


class SearchParams(BaseModel):
    text: str


app = FastAPI()


@app.post("/search")
async def root(params: SearchParams):

    productTitle = "خودکار آبی رنگ ارزان قیمتی می خواهم"

    if (len(params.text) > 0 and params.text in productTitle):

        return {
            "status": "OK",
            "message": "لینک محصولات مربوطه در دسترس شماست"
        }

    return {
        "status": "Not OK",
        "message": "محصولی وجود ندارد"
    }
