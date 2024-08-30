# Sprint The Game remake Tutorial

Le but de ce tutoriel est de vous apprendre à créer un jeu vidéo en 2D en utilisant la library *Pyxel* en Python. Il s'agit d'un remake d'un jeu que j'ai eu l'occasion de faire en équipe.
Voici le jeu original: [Sprint The Game](https://github.com/Hennzau/Sprint-The-Game-Origin)

# Tutoriel 1: Installation et setup du projet

Nous allons utiliser un outil très simple de gestion de projet python appelé *uv*. Pour l'installer, il suffit de taper la commande suivante dans votre terminal:

Pour linux et mac:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Pour windows:
```bash
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Cela permettra de créer un projet très rapidement avec la bonne version de python.

Pour créer un projet, il suffit de taper la commande suivante dans votre terminal:
```bash
mkdir -p ~/Documents/sprint-the-game
cd ~/Documents/sprint-the-game
uv venv --python 3.12
uv pip install "pyxel==2.2.0"
```

Et voilà vous embarez directement un projet qui fonctionnera. Pour vous le prouvez, créons un premier fichier

```python
# ~/Documents/sprint-the-game/main.py

def main():
    print("Hello World!")

if __name__ == "__main__":
    main()
```

Pour lancer le projet, il suffit de taper la commande suivante dans votre terminal:
```bash
uv run main.py
```

Alternativement vous pouvez activer votre environnement Python avec la commande que `uv` vous a donné et lancer le script avec `python main.py`.

```bash
source .venv/bin/activate # pour linux et MacOS
.venv\Scripts\activate # pour windows
```
