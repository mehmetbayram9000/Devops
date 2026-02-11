from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string('''
        <style>
            body { text-align: center; background: #f0f0f0; font-family: sans-serif; overflow: hidden; }
            #btn { padding: 20px 40px; font-size: 24px; cursor: pointer; background: #e74c3c; color: white; border: none; border-radius: 10px; margin-top: 50px; }
            .balloon { position: absolute; bottom: -100px; width: 50px; height: 70px; background: red; border-radius: 50%; animation: fly 3s linear; }
            @keyframes fly { to { transform: translateY(-110vh); } }
        </style>
        <h1>ERDOĞAN KAYA ÖZEL OYUNU</h1>
        <button id="btn" onclick="patlat()">BURAYA BAS!</button>
        <h2 id="msg" style="display:none; color: #2c3e50; margin-top: 30px;">ERDOĞAN KAYA ADAMDIR!</h2>

        <script>
            function patlat() {
                document.getElementById('msg').style.display = 'block';
                for(let i=0; i<20; i++) {
                    let b = document.createElement('div');
                    b.className = 'balloon';
                    b.style.left = Math.random() * 100 + 'vw';
                    b.style.backgroundColor = 'hsl(' + (Math.random() * 360) + ', 70%, 50%)';
                    document.body.appendChild(b);
                }
            }
        </script>
    ''')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
