### _Welcome to my repository!_
## 🎸 Stack:
- Language: Python🐍 version 3.10✅.
- Development approach: Flask🔨 version 3.0.3🔥.
## ⚙ Installation and usage:
### IDE
#### 1. Go to IDE and run in terminal:
    git clone https://github.com/Nerogen/Mogy-Tolko-Full-Stack.git
#### 2. Then run in terminal next line:
    pip install -r requirements.txt
#### 3. Finally, in project dir
    python app.py

### 🐳 Docker
#### 1. Go to IDE and run in terminal:
    git clone https://github.com/Nerogen/Mogy-Tolko-Full-Stack.git
#### 2. Then run in terminal next lines:
    docker build -t flask-app .
    docker run -d -p "5000:5000" flask-app

## 🌐 About site
### Description
This is flask app for clients and dealers, this app have login/register form and logic for adding clients and changing order status.
### Sql design
#### Clients Table

| Account Number | Last Name | First Name | Middle Name | Date of Birth | INN       | Responsible Person | Status         |
|----------------|-----------|------------|-------------|---------------|-----------|---------------------|----------------|
| 1              | Ivanov    | Ivan       | Ivanovich    | 1990-01-01    | 12345678  | Petrov Petr Petrovich | Not in progress |
| 2              | Petrov    | Petr       | Petrovich    | 1985-05-15    | 98765432  | Ivanov Ivan Ivanovich | In progress    |
| 3              | Sidorov   | Sidor      | Sidorovich   | 1978-12-30    | 56781234  | Nikolaev Nikolay Nikolaevich | Deal closed   |

#### Users Table

| Full Name                    | Username | Password |
|------------------------------|----------|----------|
| Ivanov Ivan Ivanovich        | ivan123  | password1|
| Petrov Petr Petrovich        | petr456  | password2|
| Nikolaev Nikolay Nikolaevich | nick789  | password3|


### Login form
![image](https://github.com/Nerogen/MLKA/assets/72101790/4c9bceea-d6f3-4a1a-a567-88216b94d902)
### Register form
![image](https://github.com/Nerogen/MLKA/assets/72101790/606938e8-c02c-4175-a8b9-652c9d27cbe0)
## Clients page
![image](https://github.com/Nerogen/MLKA/assets/72101790/9ddcd485-4942-48a9-8a98-96bff33a0c69)
## Status change
![image](https://github.com/Nerogen/MLKA/assets/72101790/2915507a-c7d0-47a3-b786-713dc743d177)
## Add client
![image](https://github.com/Nerogen/MLKA/assets/72101790/760412fa-c653-4072-996c-3b1d8fd158eb)