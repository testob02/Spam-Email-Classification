from pydantic import BaseModel 
import joblib
import json

__model = None
__labels = None

class InputSchema(BaseModel):
    email: str

def load_artifacts():
    global __model
    global __labels

    __model = joblib.load('./artifacts/model.joblib')

    with open('./artifacts/labels.json','r') as f:
        __labels = json.load(f)

def predict(request):
    pred = __model.predict([request.email])
    return {'data': __labels[str(pred[0])]}
