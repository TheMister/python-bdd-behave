# python-bdd-behave

## BDD UI test framework in python

This framework is written in Python and follows Behavior Driven Development. 

Inside the features file there is a feature named 101-AddNewMovie.feature
Within this feature, there are 4 scenarios. The first one covers multiple field validations and performs positive and negative tests.
The step definitions have not been scripted out completely since more time and information would be needed. 

Some improvements that can be made to this framework is a helper class for browser selection and start-up/teardown functions.

#### Besides testing the UI, we should also perform Integration/API and Unit Tests to ensure that the system is working properly.
- API tests: Validate that Videos can be uploaded successfully
- Unit tests: Validate that fields are taking the correct types of data
