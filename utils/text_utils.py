from transformers import pipeline

# Load the AI-generated text detection pipeline once (this is efficient)
pipe = pipeline("text-classification", model="roberta-base-openai-detector")

def predict_text(model, input_text):
    # model argument can be ignored; we're using the global pipeline
    result = pipe(input_text)[0]  # Get single result dict

    # result['label'] is "Real" or "AI-Generated"
    label = result['label']
    score = int(result['score'] * 100)

    verdict = "نص بشري" if label == "Real" else "نص مولد بالذكاء الاصطناعي"
    explanation = f"النموذج رجّح أن هذا النص {'بشري' if label == 'Real' else 'مولد آليا'} (ثقة: {score}%)"
    return verdict, explanation, score
