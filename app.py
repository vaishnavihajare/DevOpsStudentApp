
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
      <head><title>Student DevOps App</title></head>
      <body style="font-family:Arial;text-align:center;margin-top:80px;">
        <h1>Student Information Application</h1>
        <h2>DevOps Lifecycle Assignment</h2>
        <p>Application built using Python and Flask.</p>
        <p>Git, GitHub, Docker and Jenkins integration.</p>
        <p>Status: Application is running successfully!</p>
      </body>
    </html>
    """

@app.route("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
