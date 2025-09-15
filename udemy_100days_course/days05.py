#파이썬은 숫자 친화적임

student_scores = [ 120, 142, 134, 149, 122, 118 ]

total_exam_score = sum( student_scores )
# print( total_exam_score )

max_score = 0

for score in student_scores:
    if score > max_score:
        max_score = score
        
# print( max_score ) 

for num in range(1, 101):
    res = num
    if num%3 == 0:
        res = 'Fizz'
    if num%5 == 0:
        res = 'Buzz'
    if num%3 == 0 and num%5 == 0:
        res = "FizzBuzz"
    
    print(res)   