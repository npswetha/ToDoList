from flask import Flask, request, jsonify
from flask_cors import CORS
from createTask import create_task

app = Flask(__name__)
CORS(app)

app.register_blueprint(create_task)
# @app.route("/dbtest")
# def dbtest():
#     conn = get_conn()
#     cur = conn.cursor()
#     cur.execute("SELECT 1")
#     conn.close()
#     return jsonify({"db": "connected"})

# @app.route("/notes/<int:id>")
# def get(id):
#     note = notes.get(id)
#     if note is None:
#         return jsonify({"error":"Not Found"},404)
#     return jsonify({"id":id,"text":note})


# @app.route("/allnotes")
# def all_notes():
#     if notes is None:
#         return jsonify({"error":"Not Found"},404)
#     return jsonify(list(notes.items()))
    
# @app.route("/putnotes",methods=["POST"])
# def put_notes(): 
#     data = request.get_json()
#     text = data.get("text") if data else None 
#     if text is None:
#         return jsonify({"Text":"required"},400)
#     new_id = max(notes.keys())+1 if notes else 1
#     notes[new_id]=text
#     return jsonify({"success":"Added"})

# @app.route("/delnote/<int:id>")
# def delnote(id):
#     if notes.get(id) is None:
#         return jsonify({"error":"Not Found"},404)
#     del notes[id]
#     return jsonify({"success":"Deleted"})

# @app.route("/updnote/<int:id>",methods=["POST"])
# def updnote(id):
#     if notes.get(id) is None:
#         return jsonify({"error":"Not Found"},404)
#     data = request.get_json()
#     text = data.get("text") if data else None
#     if text is None:
#         return jsonify({"Text":"Required"},400)
#     notes[id] = text
#     return jsonify({"id":id,"text":text,"msg":"Updated"})
        
if __name__ == "__main__":
    app.run(debug=True)