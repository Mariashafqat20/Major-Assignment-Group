from flask import Blueprint, jsonify
from gul_andam_backend import InventoryDB

DB_PATH = "inventory.db"
report_api = Blueprint("report_api", __name__)

@report_api.route("/summary", methods=["GET"])
def summary():
    db = InventoryDB(DB_PATH)
    rows = db.fetch_all()
    db.close()

    if not rows:
        return jsonify({
            "total_items": 0,
            "total_value": 0.0,
            "most_expensive": None
        }), 200

    total_items = len(rows)
    total_value = sum(r[3] * r[4] for r in rows)  # quantity * price
    most_expensive = max(rows, key=lambda x: x[4])
    return jsonify({
        "total_items": total_items,
        "total_value": total_value,
        "most_expensive": {
            "id": most_expensive[0],
            "name": most_expensive[1],
            "price": most_expensive[4]
        }
    }), 200
