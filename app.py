from flask import Flask, render_template
import pymongo

app = Flask(__name__)

# setup mongo connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# connect to mongo db and collection
db = client.costa_rica_db
collection = db.surf_summary


@app.route("/")
def index():
    # write a statement that finds all the items in the db and sets it to a variable
    city_weather = list(db.collection.find())
    print(city_weather)

    # render an index.html template and pass it the data you retrieved from the database
    return render_template("index.html", city_weather = city_weather)


if __name__ == "__main__":
    app.run(debug=True)
