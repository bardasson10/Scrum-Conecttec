from flask import render_template
from app import app
from app.api.tickets import make_api_request
import requests


@app.route("/postos", methods=["GET", "POST"])
def postos():
    
    api_url = "https://api.tiflux.com/api/v1/tickets"
    params = {
        "limit": 1,
        "desk_id": 34189,
        "include_entity": "true",
        "is_closed": "true",
    }
    

    response = make_api_request(api_url, params=params)
    print(response)
    return render_template("postos.html")
