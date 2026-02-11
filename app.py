from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <body style='background-color: #1a1a1a; color: #00ff00; font-family: monospace; text-align: center; padding: 50px;'>
        <h1>🚀 MEMO HOSGELDİN 🚀</h1>
        <hr style='border: 1px solid #333;'>
        <p style='font-size: 20px;'>Sistem Durumu: <b>KONTEYNIR CANLI</b></p>
        <p>GitHub Actions -> GHCR -> Docker VM</p>
        <div style='border: 2px solid #00ff00; display: inline-block; padding: 20px;'>
            CI/CD Boru Hattı Başarıyla Kuruldu!
        </div>
    </body>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
