# Building project locally
Install VirtualEnvironment (one time)

    >python -m pip install virtualenv

Create virtual environment

    >virtualenv virtual_project

1. This will create a virtual environment project folder and install python there.
2. This step can be skipped if you already have the folder locally.

Open virtual environment (Windows)

To activate the Virtual machine,put in the project directory then use: 

    .\venv\Scripts\activate

To deactivate the Virtual machine run: 

    deactivate

1. This will activate the virtual environment.  Yous should see `(venv)` to the left of the terminal prompt.
2. This step will be needed each time.

Install requirements
    
    >python -m pip install -r requirements.txt

# Building Docker image
At the root of the project run

    >docker image build -t YOUR_NAME .

This will create a docker image using the `Dockerfile` with the image name `YOUR_NAME`

Run container(on your local machine with port 5000)

    >docker run -p 5000:5000 YOUR_NAME

# Building the application locally
At the root of the project run

    >app.py

This will run the application in your machine and not in a container.

# 5 Solid Practices:
1. Single Responsibility Principle (SRP): Each controller in the controllers.py module has a single responsibility. For example, TweetController is responsible for handling tweet-related operations, ThreadController for handling thread-related operations, etc. Each controller focuses on a specific area of functionality, making the code easier to understand, maintain, and test.


2. Open-Closed Principle (OCP): The code follows the OCP by using Flask's routing mechanism. The routes in the app.py module can be easily extended to handle additional functionalities by adding new routes and corresponding functions without modifying the existing code. This allows for the application to be open for extension but closed for modification.


3. Liskov Substitution Principle (LSP): The code adheres to the LSP by utilizing polymorphism. The controllers implement consistent interfaces, allowing them to be substituted. For example, the create_tweet() function can handle any type of controller as long as it follows the expected interface, allowing the same function to create tweets, threads, or replies.


4. Interface Segregation Principle (ISP): The controllers in the controllers.py module expose specific methods related to their respective functionalities. Each controller has a concise and focused interface that provides only the necessary methods for its purpose. This promotes separation of concerns and avoids clients depending on unnecessary or unrelated methods.


5. Dependency Inversion Principle (DIP): The code follows the DIP by utilizing dependency injection. The controllers are instantiated and injected into the routes through the tweet_controller, thread_controller, user_controller, and event_controller objects. This allows for loose coupling and enables easy substitution of implementations if needed.

# 3 Design Patterns
1. Repository Pattern:

The controllers (TweetController, ThreadController, UserController, EventController) can be seen as implementing the Repository pattern. They act as intermediaries between the application logic and the underlying database. The controllers encapsulate the database operations, such as creating, retrieving, updating, and deleting records. This separation of concerns promotes better organization and maintainability, allowing the controllers to handle database-related tasks while the models focus on defining the data structures and relationships.


2. Object-Relational Mapping (ORM) Pattern: 

The ORM pattern is implemented using SQLAlchemy, which provides a high-level interface for mapping models to relational database tables. Each class (User, Tweet, Thread, Event) represents a table in the database, and the attributes of the class correspond to the columns in the table. SQLAlchemy handles the mapping between the objects and the database records, allowing developers to interact with the database using object-oriented paradigms rather than writing raw SQL queries.


3. Model-View-Controller (MVC) Pattern:

The app.py module acts as the controller, defining the routes and handling HTTP requests. It is responsible for invoking the appropriate methods from the controllers to interact with the models and retrieve data. The controllers handle the business logic and data operations, while the models define the data structures and relationships.

The View component, in this case, is represented by the templates (e.g., dashboard.html, login.html) located in the templates/ directory. The controller (app.py) renders these templates by utilizing the render_template function provided by Flask. The rendered templates are then returned as responses to the client's HTTP requests.
