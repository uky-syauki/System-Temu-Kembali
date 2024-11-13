from flask import render_template

from app import app, stk, socketio, send

@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('message')
def handle_message(msg):
    hasil = stk.rekomendasi_produk(msg, stk.produk, stk.daftar_produk)
    print(f"Rekomendasi untuk {msg} adalah {hasil}") 
    print('Message received:', msg)
    # Mengirim pesan balasan dari server ke klien
    response = f"ChatBot: {' '.join(hasil)}"
    send(response, broadcast=True)