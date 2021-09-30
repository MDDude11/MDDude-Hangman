  #MANAANSH CODE
import pygame, sys, random, time
from pygame import display, event, font
 
pygame.init()
screen = display.set_mode((800, 550))
display.set_caption("Hangman!")

def display_message(message):
  screen.fill(notyellow)
  text = error_ho_gaya5.render(message, True, sadd)
  screen.blit(text, (230, 200))
  display.flip()
  # 3000 is in seconds
  time.sleep(3000)
  

sadd = (28, 255, 3)

sus = (67, 17, 247)

notyellow = (212, 49, 49)

blue = (20,61,89)

green = (147, 245, 66)

cyen = (52, 235, 216)
# font  = module name 
# Font = method inside your font ModuleNotFoundError
# (font name , font size)

words = ["minecraft", "iphone", "youtube", "error", "glitch", "computer", "system"]
numerical = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]


error_ho_gaya = font.Font("font1.ttf", 70)
error_ho_gaya2 = font.Font("font2.ttf", 40)
error_ho_gaya3 = font.Font("Roboto.ttf", 20)
error_ho_gaya4 = font.Font("yeye.ttf", 20)
error_ho_gaya5 = font.Font("yeye.ttf", 50)
error_chala_gaya = font.Font("bebas.otf", 40)
word = random.choice(words)
print(word)
guessed = []
# char varibale -> will save every key that we press on keyboard
char = ""
hangman_tries = 5
#yes sir!

while True:
  allevents = event.get()
  for myevent in allevents:
    if myevent.type == pygame.QUIT:
      sys.exit()
    if myevent.type == pygame.KEYDOWN:
      char = myevent.unicode
      print(char)
      if char in word:
        guessed.append(char)
        print(guessed)
      if char not in word:
        hangman_tries=hangman_tries-1
        print("Number of tries remaining:" , hangman_tries,"th" , "letter is not", char)
      

  screen.fill(notyellow)
  # step2 WRITING FONT
  # fontvarible.render("WHAT YOU WANT TO WRITE ,"T/F" , color )
  # True = shown on screen , False = Hidden
  text = error_ho_gaya.render("HANGMAN", True,blue)
  text2 = error_ho_gaya2.render("Guess the word", True,green)
  text3 = error_ho_gaya3.render("Made by Manaansh", True,green)
  text4 = error_chala_gaya.render("Make sure that your caps lock is off!!!", True,sadd)
  # STEP3  SHOW ON SCREEN 
  # blut function will help to show on screen
  #  200= x-coordinate 
  # 150 = y-cordinate
  screen.blit(text, (200, 20))
  screen.blit(text2, ((280,125)))
  screen.blit(text3, (600, 400))
  screen.blit(text4, (120, 300))
  display_word = ""
  # for loop will decide how many blank are there depending on word letters
  for ch in word:
    if ch in guessed:
      display_word = display_word + ch + " "
    else:
      display_word = display_word + " __ "
  text = error_ho_gaya5.render(display_word, True, blue)
  screen.blit(text, (150, 200))
  won=True
  for ch in word:
    if ch not in guessed:
      won = False
      break
  if won == True:
    display_message("You won!!!!")
    break
  if hangman_tries == 0:
    display_message("Try again, bruh")
    break


  
  tries = "Tries : " + str(hangman_tries)
  tries_text = error_ho_gaya4.render(tries, True, sus)
  screen.blit(tries_text, (50, 50))

  display.flip()

#This is a comment
#No one knows how to use it except ME!
#lol

# मैं अपरिहार्य हूँ 

# we say lol in Hindi as: ज़ोर-ज़ोर से हँसना