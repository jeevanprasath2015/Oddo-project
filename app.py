from flask import Flask, jsonify, request, render_template
from json_db import read_json, write_json

app = Flask(_name_)

EQUIP = "database/equipment.json"
REQ = "database/maintenance_requests.json"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calendar")
def calendar():
    return render_template("calendar.html")

# Get all requests
@app.route("/api/requests")
def get_requests():
    return jsonify(read_json(REQ))

# Create new request
@app.route("/api/request", methods=["POST"])
def create_request():
    data = request.json
    requests = read_json(REQ)

    equipment = next(e for e in read_json(EQUIP) if e["id"] == data["equipment_id"])

    new_request = {
        "id": len(requests) + 1,
        "subject": data["subject"],
        "equipment_id": equipment["id"],
        "team": equipment["maintenance_team"],  # AUTO-FILL
        "assigned_to": "",
        "type": data["type"],
        "status": "New",
        "scheduled_date": data.get("scheduled_date", ""),
        "duration": 0,
        "is_overdue": False
    }

    requests.append(new_request)
    write_json(REQ, requests)

    return jsonify({"message": "Request created"})

# Update status (Kanban drag)
@app.route("/api/request/<int:id>", methods=["PUT"])
def update_status(id):
    requests = read_json(REQ)
    for r in requests:
        if r["id"] == id:
            r["status"] = request.json["status"]
    write_json(REQ, requests)
    return jsonify({"message": "Updated"})
    
if _name_ == "_main_":
    app.run(debug=True)
