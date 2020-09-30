# Userregister

Build an API for login and registration.
Requirements:
1. First the email will be sent through the API
2. If it is a registered email id, then the response should be
{
 user_id:
 login_type: signin
}
3. The userId and password will be sent to the same API
 If the credentials are correct, them the response should be
{
 message: " login successful "
}
 Else the response should be
{
message: "failed"
}
4. In the step 1, if the email id is not registered, then the response should be
{
 user_id: "not registered"
 login_type: "signup"
}
5. To register new user, the following details will be sent though the API
 Email address, Password, First Name, Last Name
A new user should be registered with these details.
Note:
1. All the above functionalities should be done on the same API URL.
2. The passwords should be hashed before saving.
3. The APIs will be tested using postman, no need to make templates and
UI.
4. We will be testing your APIs on your local host itself do not host them.
5. The django admin should have access to User Details. (Password to be
hashed.)


Task 2: User profile APIs
Requirements:
The user modal should have a column called Favourite which stores the
favourit categories of the user, the favourites will be strings, Ex: cars,
traveling, technology, etc
You are required to build 3 different apis:
1. User Details API:
 user_id will be sent.
 Should give email, first name, last name and favorites of user.
2. Add Favourites:
 user_id and a favourite category name will be sent.
 Should add the category to the list of favourites.
3. Remove Favourites:
 user_id and a favourit category name will be sent
 Should remove the category from the list of favourites
