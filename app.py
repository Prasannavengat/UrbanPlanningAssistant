from flask import Flask, request, jsonify
from rag_engine import get_rag_response
from agentic_model import simulate_environment
from report_generator import generate_pdf

app = Flask(__name__)

@app.route('/query_zoning', methods=['POST'])
def query_zoning():
    question = request.json.get('question')
    answer = get_rag_response(question)
    return jsonify({'response': answer})

@app.route('/simulate_plan', methods=['POST'])
def simulate_plan():
    plan = request.json.get('plan')
    result = simulate_environment(plan)
    return jsonify({'simulation': result})

@app.route('/generate_report', methods=['POST'])
def generate_report():
    data = request.json
    pdf_path = generate_pdf(data)
    return jsonify({'report_url': pdf_path})

if __name__ == '__main__':
    app.run(debug=True)