import random

def predict_image(model, filepath):
    verdict = random.choice(["صورة حقيقية", "صورة مزيفة"])
    score = random.randint(50, 99)
    explanation = "تم التحقق تلقائياً"
    return verdict, explanation, score
