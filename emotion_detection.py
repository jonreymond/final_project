import requests
import json
# formatted_response = json.loads(response.text)

def emotion_detector(text_to_analyse):
    '''
    Retrieve the emotion score given by the Watson Emotion predict tool that appears in the given text
    '''

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    myobj = { "raw_document": { "text": text_to_analyse } }
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=myobj, headers=headers)

    return response.text



    # formatted_response = json.loads(response.text)

    # if response.status_code == 200:
    #     label = formatted_response['documentSentiment']['label']
    #     score = formatted_response['documentSentiment']['score']

    # elif response.status_code == 500:
    #     label = None
    #     score = None
    # # Return the label and score in a dictionary
    # return {'label': label, 'score': score}

if __name__ == "__main__":
    print(emotion_detector("I'm peaceful and happy"))