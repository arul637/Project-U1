import joblib
import numpy as np
import getPhishFeatures

file = open('model/model.joblib', 'rb')
model = joblib.load(file)
file.close()


def phishPrediction(url):
    features = getPhishFeatures.Features(f'{url}').get_features()
    data = np.array([features]).reshape(1, 29)
    print(data)

    y_pred = model.predict(data)[0]
    y_phishing = model.predict_proba(data)[0, 0]
    y_non_phishing = model.predict_proba(data)[0, 1]

    print("y predict", y_pred)
    print(f"phishing prediction {round(y_phishing*100, 2)}")
    print(f"non phishing prediction {round(y_non_phishing*100, 2)}")

    return y_pred, round(y_phishing*100, 2), round(y_non_phishing*100, 2)

# print("\nyoutube: ", phishPrediction("https://youtube.com/"))
# print("\ngoogle: ", phishPrediction("https://google.com/"))
# print("\nyahoo: ", phishPrediction("https://yahoo.com/"))
# print("\nopenai: ", phishPrediction("https://openai.com/"))
# print("\nyou: ", phishPrediction("https://you.com/"))
# print("\nx: ", phishPrediction("http://apholdzlogin.gitbook.io/"))
# print("\ntryhackem: ", phishPrediction("https://tryhackme.com/"))

