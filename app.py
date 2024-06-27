#!/usr/bin/env python3
import os
import requests
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://uahr1t8mhbh2ou:p37de180475ed61ab5fa6d80a4d446a1c7135e89607020eae8dc5f7d4e34caf5b@cd1goc44htrmfn.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/d5ukmvbbr0hl1d'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Forecasts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(100), nullable=False)
    day = db.Column(db.String(50), nullable=False)
    day_condition = db.Column(db.String(100))
    day_condition_icon = db.Column(db.String(100))
    h1_avg_temp = db.Column(db.Float)
    h1_wind_speed = db.Column(db.Float)
    h1_wind_direction = db.Column(db.String(5), nullable=False)
    h1_swell_ht_ft = db.Column(db.Float)
    h1_avg_temp = db.Column(db.Float)
    h1_wind_speed = db.Column(db.Float)
    h1_wind_direction = db.Column(db.String(5), nullable=False)
    h1_swell_ht_ft = db.Column(db.Float)
    h2_avg_temp = db.Column(db.Float)
    h2_wind_speed = db.Column(db.Float)
    h2_wind_direction = db.Column(db.String(5), nullable=False)
    h2_swell_ht_ft = db.Column(db.Float)
    h3_avg_temp = db.Column(db.Float)
    h3_wind_speed = db.Column(db.Float)
    h3_wind_direction = db.Column(db.String(5), nullable=False)
    h3_swell_ht_ft = db.Column(db.Float)
    h4_avg_temp = db.Column(db.Float)
    h4_wind_speed = db.Column(db.Float)
    h4_wind_direction = db.Column(db.String(5), nullable=False)
    h4_swell_ht_ft = db.Column(db.Float)
    h5_avg_temp = db.Column(db.Float)
    h5_wind_speed = db.Column(db.Float)
    h5_wind_direction = db.Column(db.String(5), nullable=False)
    h5_swell_ht_ft = db.Column(db.Float)
    h6_avg_temp = db.Column(db.Float)
    h6_wind_speed = db.Column(db.Float)
    h6_wind_direction = db.Column(db.String(5), nullable=False)
    h6_swell_ht_ft = db.Column(db.Float)
    h7_avg_temp = db.Column(db.Float)
    h7_wind_speed = db.Column(db.Float)
    h7_wind_direction = db.Column(db.String(5), nullable=False)
    h7_swell_ht_ft = db.Column(db.Float)
    h8_avg_temp = db.Column(db.Float)
    h8_wind_speed = db.Column(db.Float)
    h8_wind_direction = db.Column(db.String(5), nullable=False)
    h8_swell_ht_ft = db.Column(db.Float)
    h9_avg_temp = db.Column(db.Float)
    h9_wind_speed = db.Column(db.Float)
    h9_wind_direction = db.Column(db.String(5), nullable=False)
    h9_swell_ht_ft = db.Column(db.Float)
    h10_avg_temp = db.Column(db.Float)
    h10_wind_speed = db.Column(db.Float)
    h10_wind_direction = db.Column(db.String(5), nullable=False)
    h10_swell_ht_ft = db.Column(db.Float)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())

    def __repr__(self):
        return f'<Forecasts {self.location}>'


with app.app_context():
    db.create_all()

def calculateCondition(length, wind, waves):
   print("calculating condition for", str(length), str(wind), str(waves))
   condition = 'good'
   if wind < 5:
    print("wind < 5")
    condition = 'too-calm'  
    return condition
   if wind > 20 or waves/length > .05:
    print("wind too high or wavess over 5 percent")
    condition = 'rough'
    return condition
   if wind/length > .5:
    print("wind too little wind")
    condition = 'too-calm'
   
   return condition


@app.route("/get_forecast")
def forecaster():
 with app.app_context():
    location = "New York"
    length = 30
    forecasts = Forecasts.query.filter_by(location=location).all()
    print(forecasts)
    print("record count ",str(len(forecasts)))
    forecastCount = len(forecasts)
    outputObject = []
    dayObject = {}
    for x in range(forecastCount):
      length = 20
      print (x)
      fieldName = "h"+str(x+1)+"_swell_ht_ft"
      del dayObject
      dayObject = {}
      print(forecasts[x].day)
      dayObject['day']=forecasts[x].day
      dayObject['sailing_condition_7']=calculateCondition(length,forecasts[x].h1_wind_speed,forecasts[x].h1_swell_ht_ft)
      dayObject['sailing_condition_8']=calculateCondition(length,forecasts[x].h2_wind_speed,forecasts[x].h2_swell_ht_ft)
      dayObject['sailing_condition_9']=calculateCondition(length,forecasts[x].h3_wind_speed,forecasts[x].h3_swell_ht_ft)
      dayObject['sailing_condition_10']=calculateCondition(length,forecasts[x].h4_wind_speed,forecasts[x].h4_swell_ht_ft)
      dayObject['sailing_condition_11']=calculateCondition(length,forecasts[x].h5_wind_speed,forecasts[x].h5_swell_ht_ft)
      dayObject['sailing_condition_12']=calculateCondition(length,forecasts[x].h6_wind_speed,forecasts[x].h6_swell_ht_ft)
      dayObject['sailing_condition_13']=calculateCondition(length,forecasts[x].h7_wind_speed,forecasts[x].h7_swell_ht_ft)
      dayObject['sailing_condition_14']=calculateCondition(length,forecasts[x].h8_wind_speed,forecasts[x].h8_swell_ht_ft)
      dayObject['sailing_condition_15']=calculateCondition(length,forecasts[x].h9_wind_speed,forecasts[x].h9_swell_ht_ft)
      dayObject['sailing_condition_16']=calculateCondition(length,forecasts[x].h10_wind_speed,forecasts[x].h10_swell_ht_ft)
      dayObject['temp_7']=forecasts[x].h1_avg_temp
      dayObject['temp_8']=forecasts[x].h2_avg_temp
      dayObject['temp_9']=forecasts[x].h3_avg_temp
      dayObject['temp_10']=forecasts[x].h4_avg_temp
      dayObject['temp_11']=forecasts[x].h5_avg_temp
      dayObject['temp_12']=forecasts[x].h6_avg_temp
      dayObject['temp_13']=forecasts[x].h7_avg_temp
      dayObject['temp_14']=forecasts[x].h8_avg_temp
      dayObject['temp_15']=forecasts[x].h9_avg_temp
      dayObject['temp_16']=forecasts[x].h10_avg_temp
      outputObject.append(dayObject)
    fullOutput = {}
    fullOutput['location'] = location
    fullOutput['length'] = length
    fullOutput['forecasts'] = outputObject
 return fullOutput  

@app.route("/")
def main():

    return '''
     <h1> Data Analyzer </h1>
     '''


@app.route("/show_me")
def dbCall():
    forecasts = Forecasts.query.filter_by(location='Houston').all()
    return render_template("svs.html", forecasts=forecasts) 
    return "Data pulled from DB for record ID:"+str(get_forecast.id)+"<br> port name:"+str(get_forecast.location)\
    #+"<br> weather condition: "+get_forecast.condition \
    #+"<br> average temp F: "+str(get_forecast.avg_temp)\
    #+"<br> wind speed: "+str(get_forecast.wind_speed) \
    #+"<br> wind direction: "+get_forecast.wind_direction \
    #+"<br> swell height ft: "+str(get_forecast.swell_ht_ft)
