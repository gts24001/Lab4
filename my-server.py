# my-server.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return "You called\n"

# curl -d "text=Hello!&param2=value2" -X POST http://localhost:5000/echo
@app.route("/echo", methods=['POST'])
def echo():
    return "You said: " + request.form['text']


def trial_division(n):
    factors = []
    # Handle invalid input
    if n <= 1:
        return [n]
    # Handle 2 separately
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    # Check odd numbers up to sqrt(n)
    p = 3
    while p * p <= n:
        while n % p == 0:
            factors.append(p)
            n //= p
        p += 2
    if n > 1:
        factors.append(n)
    return factors


# curl "http://localhost:5000/factors?inINT=12"
@app.route("/factors", methods=['GET'])
def get_factors():
    try:
        inINT = int(request.args.get('inINT'))
        factors = trial_division(inINT)

        # Prime check: if only one factor and equals the number itself
        if len(factors) == 1 and factors[0] == inINT:
            return jsonify([inINT])

        # Otherwise return all factors (including 1 for completeness)
        return jsonify([1] + factors)
    except (TypeError, ValueError):
        return jsonify({'error': 'Please provide a valid integer using ?inINT=<number>'}), 400


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

