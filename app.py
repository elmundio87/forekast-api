from flask import Flask, jsonify, make_response
import internet_calendar

app = Flask(__name__)

@app.route("/")
@app.route("/events")
def hello_from_root():
    return jsonify(internet_calendar.Forekast().events)

@app.route("/today")
def today():
    return jsonify(internet_calendar.Forekast().today())

@app.route("/trending")
def trending():
    return jsonify(internet_calendar.Forekast().trending())

@app.route("/just_added")
def just_added():
    return jsonify(internet_calendar.Forekast().just_added())

@app.route("/yesterday")
def yesterday():
    return jsonify(internet_calendar.Forekast().yesterday())

@app.route("/tomorrow")
def tomorrow():
    return jsonify(internet_calendar.Forekast().tomorrow())

@app.route("/sports_events")
def sports_events():
    return jsonify(internet_calendar.Forekast().sports_events())

@app.route("/tv_events")
def tv_events():
    return jsonify(internet_calendar.Forekast().tv_events())

@app.route("/music_events")
def music_events():
    return jsonify(internet_calendar.Forekast().music_events())

@app.route("/gaming_events")
def gaming_events():
    return jsonify(internet_calendar.Forekast().gaming_events())

@app.route("/holidays")
def holidays():
    return jsonify(internet_calendar.Forekast().holidays())

@app.route("/space_events")
def space_events():
    return jsonify(internet_calendar.Forekast().space_events())

@app.route("/art_events")
def art_events():
    return jsonify(internet_calendar.Forekast().art_events())

@app.route("/other_events")
def other_events():
    return jsonify(internet_calendar.Forekast().other_events())

@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)
