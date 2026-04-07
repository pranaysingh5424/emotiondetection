import requests
import certifi

def emotion_detector(text_to_analyse):
    if not text_to_analyse.strip():
        return None
        
    url = "https://api.au-syd.natural-language-understanding.watson.cloud.ibm.com/instances/d13164d0-232e-4d51-b2b6-a3dd9c4cf6ae/v1/analyze"
    
    headers = {
        "Content-Type": "application/json"
    }

    params = {
        "version": "2021-08-01"
    }

    data = {
        "text": text_to_analyse,
        "features": {
            "emotion": {}
        }
    }

    response = requests.post(url, json=data, headers=headers, params=params, auth=("apikey", "a2XlI3FgVZb_7s51IgZ0-PdNT0hjxUw6zwg25a7PfJ60"), verify=False)

    if response.status_code != 200:
        return None
        
    if response.status_code == 400:
        return None

    result = response.json()

    emotions = result['emotion']['document']['emotion']

    dominant_emotion = max(emotions, key=emotions.get)

    return {
        "anger": emotions['anger'],
        "disgust": emotions['disgust'],
        "disgust": emotions['disgust'],
        "disgust": emotions['disgust'],
        "disgust": emotions['disgust'],
        "fear": emotions['fear'],
        "joy": emotions['joy'],
        "sadness": emotions['sadness'],
        "dominant_emotion": dominant_emotion
    }