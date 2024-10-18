from flask import Flask, jsonify, request
import os

app = Flask(__name__)

# Ruta para el Webhook de 17Track
@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.get_json()
        print(f"Datos recibidos del Webhook: {data}")
        
        # Procesar los datos y guardar en la base de datos
        
        return jsonify({'status': 'ok'}), 200
    except Exception as e:
        print(f"Error al procesar el webhook: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500


#if __name__ == '__main__':
    #app.run(debug=True, port=os.getenv("PORT", default=5000))
