from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Possible choices
choices = ["👊🏻", "🖐🏻", "✌🏻"]

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a Tie!"
    elif (user_choice == "👊🏻" and computer_choice == "✌🏻") or \
         (user_choice == "🖐🏻" and computer_choice == "👊🏻") or \
         (user_choice == "✌🏻" and computer_choice == "🖐🏻"):
        return "You Win! 🎉"
    else:
        return "Computer Wins! 🤖"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game')
def game():
    avatar = request.args.get('avatar', '👤')  # Default avatar
    return render_template('game.html', avatar=avatar)

@app.route('/play', methods=['POST'])
def play():
    data = request.get_json()
    user_choice = data.get('user_choice')
    computer_choice = random.choice(choices)
    result = determine_winner(user_choice, computer_choice)
    return jsonify({"computer_choice": computer_choice, "result": result, "play_again": True})

if __name__ == '__main__':
    app.run(debug=True)
