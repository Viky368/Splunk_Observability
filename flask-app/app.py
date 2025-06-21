from flask import Flask
import time, logging, random

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("demo-app")

@app.route("/")
def home():
    logger.info("Home endpoint hit")
    return "Hello, World!"

@app.route("/error")
def error():
    logger.error("Simulated error occurred")
    raise Exception("This is a simulated error")

@app.route("/slow")
def slow():
    time.sleep(3)
    logger.info("Slow response served")
    return "This was slow but successful"

@app.route("/random-crash")
def crash():
    if random.choice([True, False]):
        logger.critical("Random crash triggered")
        raise Exception("Random crash!")
    return "You're lucky today"