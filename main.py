from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/send-daily-news", methods=["POST"])
def send_daily_news():
    data = request.get_json()
    print("Received request:", data)

    recipient = data.get("recipient_email")
    summary_length = data.get("summary_length")
    send_time = data.get("send_time")
    source = data.get("source")

    return jsonify({
        "message": f"News email scheduled for {recipient} at {send_time}. Summary will take {summary_length} min to read from {source}."
    }), 200

if __name__ == "__main__":
    app.run()
