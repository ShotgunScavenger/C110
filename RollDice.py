import random

option = str(input('Press y to roll again and n to cancel:'))

if (option == 'y'):
    number = random.randint(1,6)
    if (number == 1):
      print('[-----]')
      print('[     ]')
      print('[  0  ]')
      print('[     ]')
      print('[-----]')
    elif (number == 2):
      print('[-----]')
      print('[    0]')
      print('[     ]')
      print('[0    ]')
      print('[-----]')
    elif (number == 3):
      print('[-----]')
      print('[  0  ]')
      print('[     ]')
      print('[0   0]')
      print('[-----]')
    elif (number == 4):
      print('[-----]')
      print('[0   0]')
      print('[     ]')
      print('[0   0]')
      print('[-----]')
    elif (number == 5):
      print('[-----]')
      print('[0   0]')
      print('[  0  ]')
      print('[0   0]')
      print('[-----]')

elif (option == 'n'):
  print('You have cancelled the program')

else:
  print('Invalid input. Cancelling program')