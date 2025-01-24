<<<<<<< HEAD
import requests

url = 'http://127.0.0.1:5000/predict'
data = {
    "ApplicantIncome":100,
    "Credit_History":1.0,
    "Gender":"Male",
    "LoanAmount":120,
    "Married":"No"
}

x = requests.post(url, json = data)
print(x.text)
=======
import requests

url = 'http://127.0.0.1:5000/predict'
data = {
    "ApplicantIncome":100,
    "Credit_History":1.0,
    "Gender":"Male",
    "LoanAmount":120,
    "Married":"No"
}

x = requests.post(url, json = data)
print(x.text)
>>>>>>> fb73bfbee66bb660457e45e5e374b8742aaa1f5e
