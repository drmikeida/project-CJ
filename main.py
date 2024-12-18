import pyxel
import time


class App:
    def __init__(self):
        # Initialize the Pyxel window (width, height) 
    
        pyxel.init(120, 120)

        pyxel.load("my_resource.pyxres")

        # Set the initial position of the Square (which would be our gingerbread)
        self.x = 60
        self.y = 75
        self.score = 0

        # Set the initial position and velocity of the gumdrop
        self.sprite_x = 80
        self.sprite_y = 60
        self.sprite_dx = 2
        self.sprite_dy = 2

        # Start the game loop
        pyxel.run(self.update, self.draw)

    def update(self):
        

        # Update the square's position based on arrow keys
        if pyxel.btn(pyxel.KEY_UP):
            self.y -= 2
        if pyxel.btn(pyxel.KEY_DOWN):
            self.y += 2
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x -= 2
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += 2

        # Simple interaction: Increase score when square reaches top-left corner
        if abs(self.x - self.sprite_x) <= 4 and abs(self.y - self.sprite_y) <= 4:
            self.score += 1

        # Update the sprite's position
        self.sprite_x += self.sprite_dx
        self.sprite_y += self.sprite_dy

        # Bounce the sprite off the edges of the screen
        if self.sprite_x <= 0 or self.sprite_x >= 160:
            self.sprite_dx *= -1
        if self.sprite_y <= 0 or self.sprite_y >= 120:
            self.sprite_dy *= -1

    def draw(self):
        # Clear the screen with black (color 0)
        pyxel.cls(0)

        pyxel.bltm(0, 0, 0, 0, 0, 256, 256)
        pyxel.bltm(256, 256, 0, 14, 0, 256, 256)
        pyxel.blt(self.x, self.y, 1, 20, 0, 12, 16)


        # Draw a square (color 9)
        pyxel.rect(self.x, self.y, 0, 250, 200)

        # Draw the moving sprite (color 11)
        pyxel.circ(self.sprite_x, self.sprite_y, 5, 11)

        # Display the score
        pyxel.text(5, 5, f"Score: {self.score}", 7)

        # Display a message when score is high
        if self.score >= 25:
            pyxel.bltm(0, 0, 3, 0, 0, 256, 256)
            pyxel.text(40, 40, "You win!", 8)
            
            
           
          
                

# Run the game
App()
