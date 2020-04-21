from fastai.vision.learner import load_learner
from fastai.vision.image import open_image

def predict(filepath):

    learn = load_learner("./ml_model/")
    img = open_image(filepath)
    prediction = learn.predict(img)
    category = str(prediction[0])
    tensor_probs = prediction[2]
    pred_probs = {
    "cardboard": round(float(tensor_probs[0]),2),
    "glass": round(float(tensor_probs[1]),2),
    "metal": round(float(tensor_probs[2]),2),
    "paper": round(float(tensor_probs[3]),2),
    "plastic": round(float(tensor_probs[4]),2),
    "trash": round(float(tensor_probs[5]),2)
    }
    ans = {
    "category": category,
    "pred_probs": pred_probs
    }

    return ans
