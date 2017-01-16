# Rappi - Test Project:
Project used to test backend skills.

Coding Challenge based in a hackerrank challenge.
[Cube Summation](https://www.hackerrank.com/challenges/cube-summation)

**Test the project:**

After configure and run the project correctly.

Go to this url [http://localhost:8080/](http://localhost:8080/)

Use this code as input (Please insert line by line in the input box, not all at the same time):

    2
    4 5
    UPDATE 2 2 2 4
    QUERY 1 1 1 3 3 3
    UPDATE 1 1 1 23
    QUERY 2 2 2 4 4 4
    QUERY 1 1 1 3 3 3
    2 4
    UPDATE 2 2 2 1
    QUERY 1 1 1 1 1 1
    QUERY 1 1 1 2 2 2
    QUERY 2 2 2 2 2 2

And the expected output is the following:
    
    4
    4
    27
    0
    1
    1

**Technologies:**  
   React/Redux, Django/Django Rest Framework, Docker, Webpack, npm.


## Without Docker

### BACKEND
#### Configuration:

1. Fork the project on GitLab and clone it to your local respository:

        git clone https://eliosf27@bitbucket.org/eliosf27/backendrappi.git && cd backendrappi

2. Config python enviroment:

Choose only one option to work with python enviroment
    
a)  Install dependecies:
        
        sudo apt install python-pip
        sudo pip install virtualenv

b) Config Virtualenv (Optional):

        virtualenv -p python3 backendrappi_env
        source backendrappi_env/bin/activate

c) Install the requirements:

         pip install -r requirements.txt

d) Run development server:

        python backend/manage.py runserver

### FRONTEND
#### Configuration

1. Install the dependencies:

        cd frontend ; npm install

2. Run the development server

        npm start

3. Open the following URL:   
   
        [http://localhost:8080/](http://localhost:8080/)

### Tasks
* Run tests:

        cd backend ; python manage.py test

* Run PEP8 validations:

        flake8

* Verify if the imports are correctly sorted

        isort -c -rc -df

Note: We can run all the tests and the validations with a single command:
        
        chmod +x test-all.sh
        ./test-all.sh

## With Docker
0. Install and configure Docker

    * Install docker. [Docker](https://www.docker.com)

    * Install docker-compose. [Compose](https://docs.docker.com/compose/install/)

## Instructions:
1. Clone the repo:  
   
   `git clone https://eliosf27@bitbucket.org/eliosf27/backendrappi.git`

2. Build the docker image:  
   
   `cd backendrappi/ && docker-compose build`

3. Install the dependencies:  
   
   `docker-compose run --rm node npm install`  

4. Starts the containers in the background and leaves them running.:  
   
   `docker-compose up -d`  

5. Open the following URL:   
   
   [http://localhost:8080/](http://localhost:8080/)

6. Run backend tests:
   
   `docker-compose exec django bash test-all.sh` 
   

