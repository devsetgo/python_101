# Python 101

## Install
- Python - [download](https://www.python.org/downloads/)
- VS Code - [download](https://code.visualstudio.com/)
    - install [python plugin](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
    - go to settings and set autosave
    - set the CMD prompt for windows users (unless you want to use powershell)
        - see setup_environment folder for JSON settngs


### Learning Resources
- W3 Schools
- Real Python
- Python Reference Documents
- Recommended books and sites
    - Beginner:
        - [Sam's Teach Yourself Python in 24 Hours](https://amzn.to/2EHW56F)
        - [Python Crash Course](https://amzn.to/2UhE4Bi)
        - [Python Reference Documents](https://wiki.python.org/moin/BeginnersGuide)
        - [W3 Schools](https://www.w3schools.com/python/)(
        - [Full Stack Python](https://www.fullstackpython.com/table-of-contents.html))
    - Next Steps:
        - [Automate the Boring Stuff with Python](https://amzn.to/2NDwPBf)
        - [Modern Python Standard Library Cookbook](https://amzn.to/2UhFYC6)
        - [Python 3 Object-Oriented Programming](https://amzn.to/2Tb4yZ0)
        - [The Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
    - Pytest
        - pytest
## TODO LIST
- [ ] Write Test Example
- [ ] Write Flask Example
- [ ] Write Flask RESTPlus expample

## Basic Python
### Week 1
- Hello World
- Basic Math
- Variables
- Strings
    - Print(“Hello all {} of you.”.format(5)
    - Print(f(“Hello all {aVar} of you.”)
        - Python 3.6 or higher

### Week 2
- Functions
    - For Loop
        - Count
    - Append a dictionary
    - Pass variable to Function
    - Simple IF, ELIF, Else statement

### Week 3
- Import statement
- Read a CSV
- Write to a CSV

### Week 4
- What is an API?
  - GET (Read)
    - POST (create), PUT (update), DELETE (delete)
    - More detailed information [here](https://www.tutorialspoint.com/http/http_methods.htm)
- JSON Data - JavaScript Object Notation
- Windows:
    - pip install virtualenv
        - virtualenv env
        - env\scripts\activate
- Linux:
    - pip3 install virtualenv
        - virtualenv env
        - source env/bin/activate

- Install Requirements
    - pip/pip3 install -r requirements.txt

- Using Python [Requests](http://docs.python-requests.org) to fetch data from an api
- Print result JSON value
- For loop over JSON
