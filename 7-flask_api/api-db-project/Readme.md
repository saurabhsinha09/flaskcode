# Flask API

Exposing Api's to fetch data from Database.

* API has Get, Post, Put and Delete
* Two url - 
    * user
    * users

## API Request

1. GET http://127.0.0.1:5000/user?name=Saurabh
2. POST http://127.0.0.1:5000/user?name=Saurabh&gender=M
3. PUT http://127.0.0.1:5000/user?name=Sanya&gender=F
4. DELETE http://127.0.0.1:5000/user?name=Saurabh

JWT token is required for users.  
PostMan tool  
POST http://127.0.0.1:5000/auth  
Header  
Content-Type : application/json  
Body  
{  
    "username":"Sammy",  
    "password":"mypassword"  
}  

GET http://127.0.0.1:5000/users  
Authorization : JWT [Token]  