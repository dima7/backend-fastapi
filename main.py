from fastapi import FastAPI

# 1. Create the app instance
app = FastAPI()

# 2. Define a "route" (the URL path)
@app.get("/")
def read_root():
    # This dictionary is automatically converted to JSON
    return {"message": "Running something slow..."}

# You no longer need the 'if __name__ == "__main__"' block 
# because 'fastapi dev' handles the execution for you.

