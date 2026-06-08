import random
import string
import math

try:
  import pyperclip
  clipboard_available = True
except ImportError:
  clipboard_available = False

print('\nThis is a password generator')

while True:
  # Randomized all combinations
  magic = input('\nUse magic mode (random everything)? (y/n): ').lower() == 'y'

  if magic:
    nr_letters = random.randint(4, 8)
    nr_numbers = random.randint(2, 4)
    nr_symbols = random.randint(2, 4)
    use_upper = use_lower = True
  else:
    def get_value_count(prompt, min_value):
      while True:
        try:
          value = int(input(prompt))
          if value < min_value:
            print(f'\nPlease enter at least {min_value}')
          else:
            return value
        except ValueError:
          print('Please enter a valid number')
    nr_letters = get_value_count('\nHow many letters do you want in your password: ', 2)
    nr_numbers = get_value_count('How many numbers do you want in your password: ', 2)
    nr_symbols = get_value_count('How many symbols do you want in your password: ', 2)

    while True:
      use_upper = input('\nInclude uppercase letters? (y/n): ').lower() == 'y'
      use_lower = input('Include lowercase letters? (y/n): ').lower() == 'y'
      if use_upper or use_lower:
        break
      print('\nYou must include at least uppercase or lowercase letters')

  # Build character set
  letters = ''
  if use_upper:
    letters += string.ascii_uppercase
  if use_lower:
    letters += string.ascii_lowercase

  numbers = string.digits
  symbols = '!@$^&*-+='

  # Generate password
  password_list = (
    random.choices(letters, k=nr_letters) +
    random.choices(numbers, k=nr_numbers) +
    random.choices(symbols, k=nr_symbols)
  )
  random.shuffle(password_list)
  pwd = ''.join(password_list)
  print(f'\nYour password is: {pwd}')

  # Estimate entropy
  charset_size = len(set(letters + numbers + symbols))
  entropy = round(len(pwd) * math.log2(charset_size), 2)
  print(f'\nEstimated password entropy: {entropy} bits')

  # Asses password strength
  if entropy < 40:
    strength = 'Weak'
  elif entropy < 60:
    strength = 'Moderate'
  else:
    strength = 'Strong'
  print(f'Password strength: {strength}')

  # Copy to clipboard
  if clipboard_available:
    try:
      pyperclip.copy(pwd)
      print('\nPassword copied successfully')
    except pyperclip.PyperclipException:
      print('Could not copy. Please copy manually')
  else:
    print('Clipboard support not available')

  # Save to file
  save = input('\nSave password to file? (y/n): ').lower()
  if save == 'y':
    with open('my_password.txt', 'w') as file:
      file.write(pwd)
    print('Password saved to "my_password.txt"')

  # Generate a new password
  again = input('\nGenerate another password? (y/n): ').lower()
  if again != 'y':
    print('Goodbye')
    break