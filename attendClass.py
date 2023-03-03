class1 = input('Is there class today?')
if class1 == 'y': 
  wake1 = input('Did you wake up on time?')
  if wake1 == 'y':
    getWeather = input("What is the temperature outside?: ")
    weather1 = input('Is it nice out?')
    if weather1 == 'y':
      trans1 = input('Do you have transportation?')
      if trans1 == 'y':
        print('GO TO CLASS!')
      if trans1 == 'n':
        int2 = input('Do you have internet access?')
        if int2 == 'y':
          print('Attend the class live stream')
        if int2 == 'n':
          print('Go back to sleep')  
    if weather1 == 'n':
      int3 = input('Do you have internet access?')
      if int3 == 'y':
        print('Attend the class live stream')
      if int3 == 'n':
        print('Go back to sleep')
  if wake1 == 'n':
    int1 = input('Do you have internet access?')
    if int1 == 'y':
      print('Attend the Class live stream')
    if int1 == 'n':
      print('Go back to sleep') 
if class1 == 'n':
  print('Go back to sleep')

