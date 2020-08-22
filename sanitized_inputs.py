from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/v1/sanitized/input/', methods=['POST'])
def json_sanitize():
    req_data = request.get_json()
    pay_input = req_data["payload"]
    bad_chars = {"\0", "\'", "\"", "\b", "\n", "\r",
                "\\", "%", "_", " ", "^", ""}
    
    for ch in pay_input:
        if ch in bad_chars:    
            return jsonify({"result":"unsanitized"})
    
    return jsonify({"result":"sanitized"})

if __name__ == "__main__":
    app.run(debug=True)
