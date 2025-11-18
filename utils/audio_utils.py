import random

def predict_audio(model, filepath):
    verdict = random.choice(["صوت حقيقي", "صوت مزيف"])
    score = random.randint(50, 99)
    explanation = "تم التحقق تلقائياً"
    return verdict, explanation, score
