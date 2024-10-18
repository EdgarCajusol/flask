from flask import Flask, jsonify, request
import os

app = Flask(__name__)

# Ruta para el Webhook de 17Track
@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.get_json()
        print(f"Datos recibidos del Webhook: {data}")

        if not data:
            return jsonify({'error': 'No data provided'}), 400

        # Ejemplo de procesamiento: almacenar el estado en la base de datos
        tracking_number = data.get('tracking_number')  # Asegúrate de que este campo exista
        status = data.get('status')

        # Aquí conectarías a tu base de datos y guardarías la información
        # self.cursor.execute("INSERT INTO envios (tracking_number, status) VALUES (%s, %s)", (tracking_number, status))
        # self.conn.commit()

        return jsonify({'status': 'ok'}), 200
    except Exception as e:
        print(f"Error al procesar el webhook: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500


#if __name__ == '__main__':
    #app.run(debug=True, port=os.getenv("PORT", default=5000))
