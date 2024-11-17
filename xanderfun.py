from flask import Flask, render_template_string

app = Flask(__name__)

# Define the home route
@app.route('/')
def home():
    return render_template_string(home_page())

# Example activity 1: Random Joke Generator
@app.route('/activity1')
def activity1():
    return render_template_string(activity1_page())

# Example activity 2: Color Changer
@app.route('/activity2')
def activity2():
    return render_template_string(activity2_page())

# Home page with links to activities
def home_page():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Fun Website by Xander Gonder</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                padding: 20px;
                background-color: #f0f0f0;
            }
            h1 {
                color: #333;
            }
            h2 {
                color: #555;
                margin-top: 0;
            }
            ul {
                list-style-type: none;
                padding: 0;
            }
            li {
                margin: 10px;
            }
            a {
                text-decoration: none;
                color: #007BFF;
                font-size: 18px;
            }
            a:hover {
                text-decoration: underline;
            }
            .donate-button {
                display: inline-block;
                padding: 10px 20px;
                margin-top: 20px;
                background-color: #ffdd57;
                color: #333;
                font-size: 16px;
                border: none;
                text-decoration: none;
                cursor: pointer;
                border-radius: 5px;
            }
            .donate-button:hover {
                background-color: #ffc107;
            }
        </style>
    </head>
    <body>
        <h1>Fun Website</h1>
        <h2>A small website made by Xander Gonder where I post my projects.</h2>
        <p>Choose an activity:</p>
        <ul>
            <li><a href="/activity1">Random Joke Generator</a></li>
            <li><a href="/activity2">Color Changer</a></li>
        </ul>
        <a class="donate-button" href="https://www.buymeacoffee.com/xandergonder" target="_blank">Buy me a coffee!</a>
    </body>
    </html>
    """

# Random Joke Generator Activity
def activity1_page():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Random Joke Generator</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                padding: 20px;
                background-color: #f0f0f0;
            }
            button {
                padding: 10px 20px;
                font-size: 16px;
                background-color: #007BFF;
                color: white;
                border: none;
                cursor: pointer;
            }
            button:hover {
                background-color: #0056b3;
            }
            #joke {
                font-size: 18px;
                margin-top: 20px;
            }
        </style>
    </head>
    <body>
        <h1>Random Joke Generator</h1>
        <button onclick="getJoke()">Get Joke</button>
        <p id="joke">Click the button to generate a random joke!</p>
        <br><br>
        <a href="/">Back to Home</a>

        <script>
            function getJoke() {
                const jokes = [
                    "Why don't skeletons fight each other? They don't have the guts.",
                    "Why don’t scientists trust atoms? Because they make up everything!",
                    "What do you call fake spaghetti? An impasta!"
                ];
                const randomJoke = jokes[Math.floor(Math.random() * jokes.length)];
                document.getElementById('joke').innerText = randomJoke;
            }
        </script>
    </body>
    </html>
    """

# Color Changer Activity
def activity2_page():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Color Changer</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                padding: 20px;
                background-color: #f0f0f0;
            }
            button {
                padding: 10px 20px;
                font-size: 16px;
                background-color: #28a745;
                color: white;
                border: none;
                cursor: pointer;
            }
            button:hover {
                background-color: #218838;
            }
            a {
                text-decoration: none;
                color: #007BFF;
                font-size: 18px;
            }
        </style>
    </head>
    <body>
        <h1>Color Changer</h1>
        <p>Click the button to change the background color:</p>
        <button onclick="changeColor()">Change Color</button>
        <br><br>
        <a href="/">Back to Home</a>

        <script>
            function changeColor() {
                const colors = ["#ff5733", "#33ff57", "#3357ff", "#f0f033", "#ff33f5"];
                document.body.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
            }
        </script>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
