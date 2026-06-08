import random

# Ask for language
lang = input('Choose language / เลือกภาษา (English/Thai): ').strip().lower()

# English messages
if lang == 'english':
  print('You have 10 chances to guess the number. Start when you are ready')
  low = int(input('Enter the lowest number: '))
  high = int(input('Enter the highest number: '))
  print(f'You have 10 chances to guess the number between {low} and {high}. Start when you are ready')

# Thai messages
elif lang == 'thai':
  print('คุณมี 10 ครั้งในการทายตัวเลข เริ่มได้เมื่อพร้อม')
  low = int(input('กรอกตัวเลขต่ำสุด: '))
  high = int(input('กรอกตัวเลขสูงสุด: '))
  print(f'คุณมี 10 ครั้งในการทายตัวเลขระหว่าง {low} ถึง {high} เริ่มได้เมื่อพร้อม')

# Default to English if unknown input
else:
  print('Language not recognized. Defaulting to English.')
  low = int(input('Enter the lowest number: '))
  high = int(input('Enter the highest number: '))
  print(f'You have 10 chances to guess the number between {low} and {high}. Start when you are ready')

num = random.randint(low, high)
ch = 10
gc = 0

while gc < ch:
  gc += 1

  if lang == 'thai':
    guess = int(input('กรอกตัวเลขที่คุณทาย: '))
  else:
    guess = int(input('Enter your guess: '))

  if guess == num:
    if lang == 'thai':
      print(f'ถูกต้อง, ตัวเลขคือ {num} คุณทายถูกใน {gc} ครั้ง')
    else:
      print(f'Correct, the number is {num}. You guessed it in {gc} attempts')
    break

  elif gc >= ch:
    if lang == 'thai':
      print(f'เสียใจด้วย ตัวเลขคือ {num} โชคดีในครั้งหน้า')
    else:
      print(f'Sorry, the number was {num}. Better luck next time')

  elif guess > num:
    print('สูงเกินไป' if lang == 'thai' else 'Too high')

  elif guess < num:
    print('ต่ำเกินไป' if lang == 'thai' else 'Too low')