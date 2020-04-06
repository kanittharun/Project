import paho.mqtt.subscribe as subscribe
import threading
import json
from flask import render_template, request, flash, redirect, url_for, jsonify, abort
from app import app, db
from app.models import FallEvent

CLIENT_ID = 'a306c380-9f11-4d10-b514-a34201a8db27'
NETPIE_TOKEN = 'Q7Twq7qFerR33BNURwtqKJ1bE8XFihPb'

@app.before_first_request
def activate_job():
    def run_job():
        while True:
            msg = subscribe.simple('@msg/fallevent/#', hostname='mqtt.netpie.io', port=1883, client_id=CLIENT_ID, auth={'username':NETPIE_TOKEN, 'password':None}, keepalive=10)
            if msg.topic == '@msg/fallevent/John':
                data_str = msg.payload.decode("utf-8")
                data = FallEvent(John=data_str)
                db.session.add(data)
                db.session.commit()
            elif msg.topic == '@msg/fallevent/Mandy':
                data_str = msg.payload.decode("utf-8")
                data = FallEvent(Mandy=data_str)
                db.session.add(data)
                db.session.commit()
            else:  
                data_str = msg.payload.decode("utf-8")
                data = FallEvent(Chris=data_str)
                db.session.add(data)
                db.session.commit()

    thread = threading.Thread(target=run_job)
    thread.start()