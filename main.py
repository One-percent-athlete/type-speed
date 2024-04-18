import tkinter as tk
import time
import random

sentenses = [
"The aroma of freshly brewed coffee filled the air, a delightful invitation to awaken the senses. Sunlight streamed through the window, painting warm stripes across the wooden table. A gentle breeze rustled the leaves outside, carrying the sweet melody of birdsong.",
"The bustling city center throbbed with activity. Cars honked, pedestrians hurried by, and shops displayed a dazzling array of goods in their windows. A street performer's lively music added a touch of whimsy to the urban symphony. Despite the chaos, there was an undeniable energy that pulsed through the heart of the metropolis.",
"The vast expanse of the desert stretched before her, a sea of golden sand dunes rippling under the relentless sun. The silence was profound, broken only by the occasional sigh of the wind. A lone hawk circled overhead, a solitary predator in this unforgiving landscape.  A sense of awe and wonder filled her as she contemplated the raw beauty and power of nature.",
"The library was a haven of tranquility, a sanctuary from the outside world. Rows upon rows of books lined the walls, their spines offering a kaleidoscope of colors and titles. The scent of old paper mingled with the faint aroma of lavender, creating a calming atmosphere. A comfortable armchair beckoned, promising an afternoon of peaceful exploration amongst the written word.",
"The rain pattered rhythmically against the windowpane, a soothing lullaby for a weary soul. Curling up beneath a cozy blanket, she sipped a steaming cup of tea, the warmth radiating through her body. The gentle pitter-patter of the rain outside created a sense of comfort and seclusion, a perfect refuge for quiet introspection.",
"The stage lights bathed the performers in a brilliant glow, casting dramatic shadows across the stage. The orchestra swelled with a crescendo, their music building towards a thrilling climax. The audience held their breath, captivated by the artistry unfolding before them. The energy in the theater was electric, a shared experience that transcended language and culture.",
"The aroma of spices filled the kitchen as she prepared her grandmother's secret recipe. The rhythmic chopping of vegetables, the sizzle of ingredients in the pan, and the gentle bubbling of a pot on the stove combined to create a symphony of sound. The anticipation of sharing this culinary masterpiece with loved ones added a touch of warmth to the air.",
"The towering mountain peak pierced the clouds, a majestic sentinel guarding the valley below. A winding trail snaked its way up the side, a challenge for the adventurous spirit. The view from the summit promised to be breathtaking, a reward for those willing to test their limits. A sense of determination filled her as she embarked on her ascent.",
"The rhythmic clatter of the train wheels echoed through the countryside. Lush green fields and rolling hills unfolded outside the window, a scenic tapestry painted by nature. The gentle rocking of the train lulled her into a state of relaxation, a temporary escape from the daily grind. The journey itself became a destination, a chance to disconnect and reconnect with the beauty of the world.",
"The crackling fireplace cast a warm glow on the room, its flames dancing in a hypnotic rhythm. A mug of hot cocoa warmed her hands, its comforting warmth radiating through her fingers. A good book lay open on her lap, its pages promising an engrossing adventure. The world outside seemed to fade away as she immersed herself in the story, a peaceful haven from the chill of the winter night."
]

sentense_num = random.randint(0,10)

class TypingTest:
  def __init__(self, master):
    self.master = master
    master.title("Typing Speed Test")

    # Text box for user input
    self.user_input = tk.Entry(master, width=75)
    self.user_input.pack(pady=10)
    self.user_input.bind("<Return>", self.start_test)  # Start test on Enter press

    # Display area for the test text
    self.test_text = tk.Label(master, text="Click 'Start Test' to begin", font=("Arial", 12))
    self.test_text.pack(pady=10)

    # Button to start the test
    self.start_button = tk.Button(master, text="Start Test", command=self.start_test)
    self.start_button.pack()

    # Results label (initially hidden)
    self.results = tk.Label(master, text="", font=("Arial", 12))
    self.results.pack()

    # Variables for storing test data
    self.test_start = None
    self.words = None

  def start_test(self, event=None):
    # Disable start button and clear previous results
    self.start_button.config(state="disabled")
    self.results.config(text="")

    # Get the test text (replace with your own or load from a file)
    self.test_text.config(text=sentenses[0], width=75, wraplength=200)

    # Record test start time
    self.test_start = time.time()

    # Reset focus to user input area
    self.user_input.focus_set()

    # Bind function to detect when user finishes typing
    self.user_input.bind("<KeyRelease-Return>", self.end_test)

  def end_test(self, event=None):
    # Calculate elapsed time
    elapsed_time = time.time() - self.test_start

    # Get user input and split into words
    user_text = self.user_input.get().strip()
    self.words = len(user_text.split())

    # Calculate words per minute (WPM)
    wpm = int((self.words / elapsed_time) * 60)

    # Display results
    self.results.config(text=f"WPM: {wpm}")

    # Enable start button again for another test
    self.start_button.config(state="normal")

# Create the main window
root = tk.Tk()

# Create the application instance
app = TypingTest(root)

# Run the main loop
root.mainloop()