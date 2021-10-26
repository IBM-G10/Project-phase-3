import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'symptom1':chills, 'symptom2':acidity, 'symptom3':shivering,'symptom4':skin-rash,'symptom5':itching})

print(r.json())