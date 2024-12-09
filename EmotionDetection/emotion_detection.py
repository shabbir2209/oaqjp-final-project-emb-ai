import requests
import json

def emotion_detector(text_to_analyse):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    body = {
        "raw_document":{
            "text":text_to_analyse
        }
    }
    response = requests.post(url, json=body, headers=headers)
    json_data = response.json()
    anger_score = json_data['emotionPredictions'][0]['emotion']['anger']
    disgust = json_data['emotionPredictions'][0]['emotion']['disgust']
    fear = json_data['emotionPredictions'][0]['emotion']['fear']
    joy = json_data['emotionPredictions'][0]['emotion']['joy']
    sadness = json_data['emotionPredictions'][0]['emotion']['sadness']

    emotions = {
    "anger": anger_score,
    "disgust": disgust,
    "fear": fear,
    "joy": joy,
    "sadness": sadness
    }

    dominant_emotion = max(emotions, key=emotions.get)
    emotions["dominant_emotion"] = dominant_emotion

    return emotions
