from flask import Blueprint, request, jsonify
from db import get_conn

create_task = Blueprint("create_task",__name__)

@create_task.route("/addtodo",methods=["POST"])
def addtodo():
    device_id = request.headers.get("X-Device-Id","test-device")
    if not device_id:
        return jsonify({"error":"DeviceId is Required"}),400
    
    data = request.get_json()
    task= data.get("task") if data else None
    if task is None:
        return jsonify({"error":"Task is required"}),400
    conn = get_conn()
    try:
         cur = conn.cursor()
         cur.execute(
            "Insert into user_todo(task,device_id) values (%s,%s) returning id",(task,device_id)
         )
         new_id = cur.fetchone()[0]
         conn.commit()
         return jsonify({"id:":new_id,"task":task,"status":False}),201
    except exeception as e:
         conn.rollback()
         print("DB Error:",e)
         return jsonify({"error":"DB error"}),500
    finally:
        conn.close()