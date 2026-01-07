from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
	return {"message": "Hello, adepterz!"}

@app.post("/user")
def read_root(user_name: str):
	return {
		"message": "Hello, adepterz!",
		"name": f"{user_name}",
	}