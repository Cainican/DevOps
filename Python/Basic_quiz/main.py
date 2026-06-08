import random

# Quiz
def quiz():
  print('\nWelcome to my quiz\n')
  print('Answer the following questions:')

  q_a = [
    ('1. What species of bears is the biggest? ', 'Polar bear'),
    ('2. What is the biggest animal on Earth? ', 'Blue whale'),
    ('3. What is the biggest island in the world? ', 'Greenland'),
    ('4. How many settlements are there in Greenland? ', '54'),
    ('5. What is the capital of Greenland? ', 'Nuuk')
  ]

  random.shuffle(q_a)

  score = 0

  for question, answer in q_a:
    user_answer = input(question).strip().lower()
    correct_answer = answer.strip().lower()
    if user_answer == correct_answer:
      print('Correct\n')
      score += 1
    else:
      print(f'Incorrect. The correct answer is: "{answer}"\n')

  percentage = (score / len(q_a)) * 100
  print('Quiz completed\n')
  print(f'You got {score}/{len(q_a)} questions right ({percentage:.1f}%)')

  if percentage == 100:
    print('Perfect score. You are a trivia master')
  elif percentage >= 60:
    print('Great job. You really know your stuff')
  else:
    print('Keep learning - you will get there')

  reply = input('\nWould you like to play again? (y/n): ').strip().lower()
  if reply in ['yes', 'y']:
    quiz()
  else:
    print('\nThanks for playing')

quiz()