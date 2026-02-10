from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return """
    <body style='background-color: #2c3e50; color: white; font-family: sans-serif; text-align: center; padding-top: 50px;'>
        <h1>🚀 Mehmet Bayram DevOps Projesi v2</h1>
        <p>GitHub Actions ile otomatik build edildi.</p>
        <p>Docker ile GHCR üzerinden çekildi ve çalıştırıldı.</p>
        <div style='background: #e74c3c; padding: 10px; display: inline-block; border-radius: 5px;'>
            <strong>Durum: Konteynır Canlı!</strong>
        </div>
    </body>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
