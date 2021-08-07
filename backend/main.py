from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from products import allProducts
from models import ItemID
from tax_calculator import create_receipt


app = FastAPI()


origins = [
    "http://localhost",
    "https://localhost:5000",
    "http://localhost:8080",
    "http://localhost:8081",
    "http://localhost:8082",
]


# middleware for cross origin resource sharing
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# API returning all items
@app.get("/getAllProducts")
async def all_items():
    # print(allProducts)
    return allProducts


# API to create receipt
@app.post("/calculateTax")
async def tax_calculation(ids : ItemID):
    # calling create receipt function
    result = create_receipt(ids)
    return result


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)