# Thomas' Projects

[HOME](index.html)

[PROJECT DIRECTORY](index2.html)

## Asteroids

![asteroids pic](static/images/asteroids/asteroids_gif.gif)

> I know what your thinking.. *That game is simple and has been made many times over!* While that is true I used this project to experiment with the *Pygame* moduel and learned many things along the way. 

## The Code

## *Before graphics and controller*

![bwasteroids](static/images/asteroids/bwasteroids_gif.gif)

* This is the [REPO](https://github.com/BruzaTom/asteroids-) before graphics and controller inputs.

![asteroids dir pic](static/images/asteroids/asteroids_dir.png)

> Here is a look at the root directory.

## requirements.txt

![reqirements](static/images/asteroids/requirements.png)

> Short and sweet! The only requirements for the game are *pygame2.6.0*, with that the game will run great!

## constants.py

![constants](static/images/asteroids/constants.png)

> If you have developed games before you probly understand the importance of constant variables. If not, the constant variables provide controle to testing the feel of the game and how it behaves. Rather than searching for every instance of player speed in the game, I can simply modify one variable.

## circleshape.py

![circlshape](static/images/asteroids/circleshape2.png)

> The foundation of every object in the game is a circleshape. Acting as a hit box, north star for positioning, and in some cases the actual graphic.

## player.py

![player](static/images/asteroids/player2.png)

> Here is the star of the show, the player! This class handles player positioning, inputs to control player, and a method to create shot objects. speaking of shots..

![shots](static/images/asteroids/shots_gif.gif)

## shot.py

![shots](static/images/asteroids/shot2.png)

> Pretty standard stuff here an object drawn traveling away from the path it was spawnd.(from players position) Lets get into these containers..

## main.py

![cheering](static/images/asteroids/cheering.gif)

![main](static/images/asteroids/main.png)