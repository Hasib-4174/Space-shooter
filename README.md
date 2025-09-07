# 🚀 Space Shooter

A simple **2D space shooting game** built with **[pygame-ce](https://github.com/pygame-community/pygame-ce)**.  
Control your spaceship using **WASD** keys and navigate through the starfield while dodging meteors and firing lasers.

---

## 📂 Project Structure

```
Space-Shooter/
├── audio
│   ├── damage.ogg
│   ├── explosion.wav
│   ├── game_music.wav
│   └── laser.wav
├── images
│   ├── explosion
│   │   ├── *.png
│   │   ├── ..
│   ├── laser.png
│   ├── meteor.png
│   ├── Oxanium-Bold.ttf
│   ├── player.png
│   └── star.png
├── main.py
└── README.md
```

---

## 🎮 Features

- Player spaceship movement using **WASD**.
- Randomly generated **stars** as background.
- Static **meteor** and **laser** sprites.
- **Explosion sprite sheet** for future animation.
- Audio files included (laser, damage, explosion, music).
- Smooth movement with `pygame.math.Vector2`.

> ⚠️ Currently, the player can move **outside the window border**.  
> No boundary collision is implemented yet.

---

## 🛠️ Installation & Setup

Follow these steps to set up and run the project:

### 1. Clone the repository

```bash
git clone https://github.com/Hasib-4174/Space-shooter.git
cd space-shooter
```

### 2. Create and activate a virtual environment

```bash
# Create virtual environment
python -m venv pygame_venv

# Activate it
# On Linux/macOS:
source pygame_venv/bin/activate
# On Windows:
pygame_venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install pygame-ce
```

### 4. Run the game

```bash
python main.py
```

### 5. Deactivate environment (when done)

```bash
deactivate
```

---

## 🎮 Controls

| Key | Action |
|-----|---------|
| **W** | Move Up |
| **A** | Move Left |
| **S** | Move Down |
| **D** | Move Right |

---

## 🖼️ Preview
No preview!!
<!-->> *(Add a screenshot or GIF of the gameplay here)*-->

---

## 🚧 Future Improvements

- Add **boundary collision** (prevent player from leaving the screen).  
- Implement **shooting mechanics** with laser projectiles.  
- Add **enemy ships** and AI movement.  
- Animate **explosions** using the sprite sheet.  
- Play **background music** and sound effects.

---

## 📝 Notes

This game was created while following a **Pygame tutorial** as part of my learning journey.  
I have customized and experimented with different features (like **WASD movement**) to understand how game loops, event handling, and sprite rendering work in **pygame-ce**.  

[Original Tutorial](https://www.youtube.com/watch?v=8OMghdHP-zs)

This project is both a **practice exercise** and a **foundation** for building more advanced games in the future.
