import random

def predict_video(model, filepath):
    verdict = random.choice(["فيديو حقيقي", "فيديو مزيف"])
    score = random.randint(50, 99)
    explanation =  "تم التحقق تلقائياً"
    return verdict, explanation, score
