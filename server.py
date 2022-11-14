"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page.""" #<----doesnt get interpreted
  #<title> is for the tab name
    
    
    return """
    <!doctype html>
    <html>
      <head>
        <title>Home Page</title>
        <h1>Hi! This is the home page.</h1>
      </head>
      <body>
        <a href="http://localhost:5000/hello">Hello</a>
      </body>
    </html>
    """ 
    #^^^returning a string in triple qoutes is diff and shows up
    #^^^line 31 is a link for our local server, not avail on internet...this is a developmental server just fo us...practice
    #^^^on E's personal machine, the server would be diff 
#^^^OUTPUT

@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          <input type="submit" value="Submit">
        </form>
        
        <form>
        <label for "compliment-select">Choose a compliment:</label>

        <select name="comp">
          <option value="awesome">awesome</option>
          <option value="terrific">terrific</option>
          <option value="fantastic">fantastic</option>
          <option value="neato">neato</option>
        </select>
        
        </form>

      </body>
    </html>
    """
#^^^the first form is a TEXT INPUT form w/o the id-selector 
#^^^the second form is a  DROPDOWN MENU form w/o id-selector


# <form>
#   <label for="lang-select">Choose your main programming language:</label>

#   <select name="lang" id="lang-select">
#     <option value="python">Python</option>
#     <option value="javascript">JavaScript</option>
#     <option value="ruby">Ruby</option>
#   </select>
# </form>


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    #compliment = choice(AWESOMENESS)

    compliment = request.args.get("comp")

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
