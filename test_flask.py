import pytest
from loan_app import app


@pytest.fixture
def client():
	"""
	Fixture that creates an instance of the application's client.

	Returns:
		FlaskClient: The client instance.
	"""
	return app.test_client()

# The `client` fixture creates an instance of the application's client.
# This client instance can be used to send requests to the application.
# It is commonly used in test functions to simulate HTTP requests and
# interact with the application's routes and endpoints.


def test_ping(client):
	"""
	Test function to check the '/ping' endpoint.

	Args:
		client (FlaskClient): The client instance.

	Raises:
		AssertionError: If the response status code is not 200 or the
			response message is not as expected.
	"""
	response = client.get('/ping')
	assert response.status_code == 200, "The status code was not 200"
	assert response.json == {'message': 'Loan Approval Application'}, "The message was not as expected"


# 	# We can have both tests in one function only
# 	test_data={
#     "ApplicantIncome":100,
#     "Credit_History":1.0,
#     "Gender":"Male",
#     "LoanAmount":120,
#     "Married":"No"
# }

	
# 	response = client.post('/predict', json=test_data)

# 	assert response.status_code == 200, "The status code was not 200"
# 	assert response.json == {"loan_approval_status": "Approved"}, "The message was not as expected"


def test_predict(client):

	test_data={
    "ApplicantIncome":100,
    "Credit_History":1.0,
    "Gender":"Male",
    "LoanAmount":120,
    "Married":"No"
}

	
	response = client.post('/predict', json=test_data)

	assert response.status_code == 200, "The status code was not 200"
	assert response.json == {"loan_approval_status": "Approved"}, "The message was not as expected"


#import random

#def test_dynamic_predict(client):
#	genders = ["Male", "Female"]
#	marital_statuses = ["Married", "Unmarried"]
#	credit_histories = [0.0, 1.0]
#	applicant_incomes = [50000, 100000, 150000]
#	loan_amounts = [500000, 1000000, 2000000]

#	for _ in range(10):  # Run the test 10 times with different random parameters
#		test_data = {
#			'Gender': random.choice(genders),
#			'Married': random.choice(marital_statuses),
#			'Credit_History': random.choice(credit_histories),
#			'ApplicantIncome': random.choice(applicant_incomes),
#			'LoanAmount': random.choice(loan_amounts)
#		}

#		response = client.post('/predict', json=test_data)

#		assert response.status_code == 200, "The status code was not 200"
#		assert "loan_approval_status" in response.json, "The response did not contain 'loan_approval_status'"