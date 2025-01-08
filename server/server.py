from fastapi import FastAPI
import utils

app = FastAPI()

utils.load_artifacts()

@app.post('/get_prediction')
def predict(request: utils.InputSchema):
    return utils.predict(request)