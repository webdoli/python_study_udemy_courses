import random

num = random.randint(1,100)
print(num)

random_ = random.random()
print(random_)
print(int(random_ *10))

# List
list01 = ['서울', '부산', '대구', '인천', '대전', '문경', '광주']
rand_city_num = random.randint( 0, len(list01) )
print( list01[rand_city_num])


scissors = '''
          _______
      ---'   ____)____
                ______)
             __________)
            (____)
      ---.__(___)
            '''
            
fist = '''
       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
       ''' 
       
paper = '''
          _______
      ---'   ____)____
                ______)
                _______)
               _______)
      ---.__________)
      '''
      

user_choice = int(input(
    'What do you choose? \nType 0 for scissors, \n1 for fist \n2 for paper:',
    ))

print('user_choice:', type(user_choice))

com_choice = random.randint(0, 2)
com_list = [scissors, fist, paper ]
result = 0

print(com_list[user_choice])
print('Computer choose:\n'+com_list[com_choice])

while result != 1:

    if user_choice == 0: # 가위
        if com_choice == 1:
            print('패배')
            result = 1
        if com_choice == 0:
            print('비김')
            break
        if com_choice == 2:
            print('승리')
            result = 1
    
    if user_choice == 1: # 주먹
        if com_choice == 2:
            print('승리')
            result = 1
        if com_choice == 1:
            print('비김')
            break
        if com_choice == 1:
            print('패배')
            result = 1
    
    if user_choice == 2: # 보
        if com_choice == 0:
            print('패배')
            result = 1
        if com_choice == 2:
            print('비김')
            break
        if com_choice == 1:
            print('승리')
            result = 1
    
