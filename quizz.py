score = 0
ans_1 = input('What is the capital of Nigeria: ').capitalize()
if ans_1 == 'Abuja':
    score += 1
    print(f'correct you have {score}')
else:
    print("not exactly try again....")
    ans_1 = input('What is the capital of Nigeria: ').capitalize()
if ans_1 == 'Abuja':
    score += .5

ans_2 = int(input('How many States are in Nigeria? '))
if ans_2 == 36:
    score += 1
    print(f'correct you have {score}')
else:
    print('not exactly try again....')
    ans_2 = int(input('How many States are in Nigeria? '))
if ans_2 == 36:
    score += .5

ans_3 = int(input('A year has how many months? '))
if ans_3 == 12:
    score += 1
    print(f'correct you have {score}')
else:
    print('not exactly try again....')
    ans_3 = int(input('A year has how many months? '))
if ans_3 == 12:
    score += .5
print(f'The end you have {score}points')