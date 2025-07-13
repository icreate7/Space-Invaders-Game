# 🛸 Space Invaders Game

A retro-style **Space Invaders** game built using Python's `turtle` module.

## 🎮 Gameplay

- Control the paddle using `←` and `→` arrow keys.
- Press `Spacebar` to shoot.
- Destroy all invading aliens before they reach your base.
- Avoid alien bullets.
- Barricades protect you — but they get damaged over time!

---

## 🧠 Features

- Alien army that moves left, right, and descends over time
- Bullet collision with aliens, barricades, and player
- Player and alien bullet mechanics
- Health-based barricade system
- Game Over message when player is hit or aliens reach the bottom

---

## 🛠️ Requirements

- Python 3.x  
- No external libraries required (uses built-in `turtle`, `random`, and `time`)

---

## ▶️ How to Run

1. Clone the repo:

bash:
git clone https://github.com/your-username/space-invaders.git
cd space-invaders
Run the game:

bash:
Copy
Edit
python main.py

📁 File Structure
graphql
Copy
Edit
space-invaders/
│
├── main.py             # Game loop and controls
├── bullet.py           # Bullet behavior
├── barricade.py        # Barricade class with health and damage
├── paddle.py           # Player paddle
├── alien.py            # Alien and AlienGroup logic
├── text.py             # Display Game Over message
└── README.md           # This file
📸 Screenshots
(Optional: You can add your own screenshots here)

🧠 Inspiration
This project is inspired by the classic Space Invaders arcade game from the 1970s, rebuilt in Python for learning and fun.

📝 License
This project is open-source and free to use for learning purposes.

Let me know if you'd like me to add badges, emojis, or GIFs — or help you upload screenshots!
