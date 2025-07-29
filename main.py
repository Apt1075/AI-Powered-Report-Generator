from fastapi import FastAPI, Query
from pydantic import BaseModel
from app.model import text_to_query
from app.mongo import get_report

app = FastAPI()

class RequestModel(BaseModel):
    query: str

@app.post("/generate-report/")
def generate_report(req: RequestModel):
    mongo_query = text_to_query(req.query)
    print(mongo_query)
    results = get_report(mongo_query)
    print(results)
    return {"query": mongo_query, "results": results}
