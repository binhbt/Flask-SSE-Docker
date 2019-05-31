from flask import Flask
from redis import Redis
from flask_sse import sse

app = Flask(__name__)
redis = Redis(host='redis', port=6379)
app.config["REDIS_URL"] = "redis://redis:6379"

@app.route('/')
def hello():
    redis.incr('hits')
    return 'Hello World! I have been seen %s times.' % redis.get('hits')

app.register_blueprint(sse, url_prefix='/stream')

@app.route('/send')
def send_message():
    sse.publish({"message": "Hello!"}, type='greeting')
    return "Message sent!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
