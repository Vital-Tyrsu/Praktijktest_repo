from flask import Flask
from flask import render_template
import datetime

microweb_app = Flask(__name__)

@microweb_app.route("/") # Toont de route om de locatie van de file te vinden
def main():
    return render_template("index.html")


if __name__ == "__main__":
    microweb_app.run(host="0.0.0.0", port=5555)
