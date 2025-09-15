#3주차 if else
print('''
             z$
             z$$F
            d$$$
           $$$$$
          J$$$$$
          $$$$$$
         .$$$$$$
         $$$$$$$b
        $$$$$$$$$c
       J$$$$$$$$$$$c
       $$$$ "$$$$$$$$$.
      $$$$P    "*$$$$$"                     .ze$$$$$bc
     .$$$$F                              z$$$$$$$$$$$$$b
     $$$$$                           .e$$$$$$$$$$$$$$$$$$.
     $$$$$                         z$$$$$$$$$$$$$$$$""$$$$
    4$$$$$F                     .$$$$$$$$$$$$$$$$$$$  $$$$r
    $$$$$$$                   z$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    $$$$$$$c                e$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    '$$$$$$$c            .d$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
     $$$$$$$$b          d$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
      *$$$$$$$$r      d$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Gilo94'
          """"""      """"""""""""""""""""""""""""""""""""
  __________________________________________________________________________
Warwasus
  __________________________________________________________________________
      ''')

print('Welcome to Tresure Island. \n'
    'Your mission is to find the treasure.' )
answer = input('left of right?').lower()

if answer == 'left':
    answer = input('swim or wait?').lower()
    if answer == 'swim':
        print('Game Over.')
    elif answer == 'wait':
        answer = input('Which door?').lower()
        if( answer == 'red'):
            print('Game Over.')
        elif( answer == 'blue'):
            print('Game Over.')
        elif( answer == 'yellow'):
            print('You win!')
        else :
            print('Game OVer')
else:
    print('Game Over.')



