from flask import Flask, render_template, request, jsonify

app = Flask(
    __name__,
    template_folder="app/templates",
    static_folder="app/static"
)

# Temporary sample fares in Kenya Shillings.
# These are development values, not confirmed market fares.
FARE_DATA = {
    ("ruiru", "nairobi cbd"): (100, 150),
    ("thika", "nairobi cbd"): (120, 180),
    ("rongai", "nairobi cbd"): (100, 150),
    ("kitengela", "nairobi cbd"): (120, 180)
}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/calculate-fare", methods=["POST"])
def calculate_fare():
    data = request.get_json()

    origin = data.get("origin", "").strip().lower()
    destination = data.get("destination", "").strip().lower()
    travel_time = data.get("travel_time", "offpeak")

    if not origin or not destination:
        return jsonify({"error": "Please enter both locations."}), 400

    route = (origin, destination)

    if route not in FARE_DATA:
        return jsonify({
            "error": "Sorry, this route is not currently supported."
        }), 404

    minimum, maximum = FARE_DATA[route]

    if travel_time == "peak":
        minimum = round(minimum * 1.2)
        maximum = round(maximum * 1.2)
    elif travel_time != "offpeak":
        return jsonify({"error": "Invalid travel time."}), 400

    return jsonify({
        "origin": origin.title(),
        "destination": destination.title(),
        "minimum_fare": minimum,
        "maximum_fare": maximum,
        "currency": "KES",
        "message": "Development estimate only. Actual fares may vary."
    })
if __name__ == "__main__":
    app.run(debug=True)